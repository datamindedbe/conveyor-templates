package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.transformations

import java.sql.Date
import java.time.LocalDate

import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common.{DatasetComparer, SharedSparkSession}
import org.scalatest.{FunSuite, Matchers}

class SharedTransformationsTest extends FunSuite with SharedSparkSession with Matchers with DatasetComparer {

  import spark.implicits._

  test("A datestamp can be added to a dataframe") {
    val localDate = LocalDate.of(2010, 1, 1)
    val sqlDate = Date.valueOf(localDate)

    val input = Seq(("issue1", "high"), ("issue2", "low")).toDF("issue", "prio")
    val expected = Seq(("issue1", "high", sqlDate), ("issue2", "low", sqlDate))
      .toDF("issue", "prio", "ds")

    val actual = input.transform(SharedTransformations.addDatestamp(localDate))
    assertDatasetEquality(actual, expected)
  }

}
