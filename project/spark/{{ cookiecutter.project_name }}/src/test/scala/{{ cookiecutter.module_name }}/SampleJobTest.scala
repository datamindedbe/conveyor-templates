package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}

import java.sql.Date
import java.time.LocalDate

import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common.{DatasetComparer, SharedSparkSession}
import org.scalatest.matchers.must.Matchers
import org.scalatest.funsuite.AnyFunSuite
import org.scalatest.matchers.should.Matchers.convertToAnyShouldWrapper

class SampleJobTest extends AnyFunSuite with SharedSparkSession with Matchers with DatasetComparer {
  import spark.implicits._

  test("A datestamp is added to the dataframe") {
    val localDate = LocalDate.of(2010, 1, 1)
    val sqlDate = Date.valueOf(localDate)

    val input = Seq(("issue1", "high"), ("issue2", "low")).toDF("issue", "prio")
    val expected = Seq(("issue1", "high", sqlDate), ("issue2", "low", sqlDate)).toDF("issue", "prio", "ds")

    val actual = new SampleJob(spark).transform(input, localDate)
    assertDatasetEquality(actual, expected)
  }

  test("Duplicates are removed") {
    val localDate = LocalDate.of(2010, 1, 1)

    val input = Seq(("issue1", "high"), ("issue1", "high")).toDF("issue", "prio")

    val actual = new SampleJob(spark).transform(input, localDate)
    actual.count should equal(1)
  }
}
