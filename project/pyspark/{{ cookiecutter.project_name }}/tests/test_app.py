from datetime import datetime

from {{ cookiecutter.module_name }}.app import transform_data
from tests.common.spark import get_test_spark_session, assert_frame_equal_with_sort

spark = get_test_spark_session()


def test_ds_is_added():
    date_string = "2020-01-01"
    date = datetime.strptime(date_string, "%Y-%m-%d").date()
    source_df = spark.createDataFrame(
        [("issue1", "high"), ("issue2", "low")], ["issue", "prio"]
    )
    expected = spark.createDataFrame(
        [("issue1", "high", date), ("issue2", "low", date)], ["issue", "prio", "ds"]
    )
    result = transform_data(source_df, date_string)
    assert_frame_equal_with_sort(result, expected)


def test_duplicates_are_removed():
    date_string = "2020-01-01"
    source_df = spark.createDataFrame(
        [("issue1", "high"), ("issue1", "high")], ["issue", "prio"]
    )

    result = transform_data(source_df, date_string)
    assert result.count() == 1
