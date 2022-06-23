import argparse

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.dataframe import DataFrame

from {{ cookiecutter.module_name }}.common.spark import ClosableSparkSession, transform, SparkLogger
from {{ cookiecutter.module_name }}.transformations.shared import add_ds


DataFrame.transform = transform


def main():
    parser = argparse.ArgumentParser(description="{{ cookiecutter.project_name }}")
    parser.add_argument(
        "-d", "--date", dest="date", help="date in format YYYY-mm-dd", required=True
    )
    parser.add_argument(
        "-e", "--env", dest="env", help="environment we are executing in", required=True
    )
    args = parser.parse_args()

    with ClosableSparkSession("{{ cookiecutter.project_name }}") as session:
        run(session, args.env, args.date)


def run(spark: SparkSession, environment: str, date: str):
    """Main ETL script definition.

    :return: None
    """
    # execute ETL pipeline
    logger = SparkLogger(spark)
    logger.info(f"Executing job for {environment} on {date}")
    data = extract_data(spark, date)
    transformed = transform_data(data, date)
    load_data(spark, transformed)


def extract_data(spark: SparkSession, date: str) -> DataFrame:
    """Load data from a source

    :param spark: Spark session object.
    :return: Spark DataFrame.
    """
    local_records = [
        Row(user_id=1, event="login", browser="safari"),
        Row(user_id=2, event="login", browser="chrome"),
        Row(user_id=1, event="logout", browser="safari"),
        Row(user_id=1, event="logout", browser="safari"),
        Row(user_id=2, event="expired", browser="IE6"),
        Row(user_id=3, event="login", browser="firefox"),
    ]
    return spark.createDataFrame(local_records)


def transform_data(data: DataFrame, date: str) -> DataFrame:
    """Transform original dataset.

    :param data: Input DataFrame.
    :param date: The context date
    :return: Transformed DataFrame.
    """
    return data.transform(add_ds(date)).dropDuplicates()


def load_data(spark: SparkSession, data: DataFrame):
    """Writes the output dataset to some destination

    :param data: DataFrame to write.
    :return: None
    """
    data.show()

    {% if cookiecutter.cloud == "aws" -%}
    # Uncomment the following block to write to a compatible catalog
    # spark.catalog.setCurrentDatabase("DEFAULT_DB")
    # (
    #     data.coalesce(1)
    #     .write.partitionBy("ds")
    #     .mode("overwrite")
    #     .format("parquet")
    #     .saveAsTable("sample")
    # )
    {%- elif cookiecutter.cloud == "azure" -%}
    # Uncomment the following block to write to a storage account
    # data.write.mode("overwrite")
    # .parquet(f"abfs://{storageContainer}@{storageAccount}.dfs.core.windows.net/{path}")
    {%- endif %}


if __name__ == "__main__":
    main()
