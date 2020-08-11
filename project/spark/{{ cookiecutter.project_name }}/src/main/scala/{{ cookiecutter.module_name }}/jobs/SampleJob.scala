package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.jobs

import java.time.LocalDate

import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common.SparkSessions
import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.transformations.SharedTransformations
import org.apache.spark.sql.DataFrame


@EntryPoint(runnerType = "sample")
object SampleJob extends Job with SparkSessions {

  import spark.implicits._

  override def run(environment: String, date: LocalDate): Unit = {
    // execute ETL pipeline
    val data = extract(environment)
    val transformed = transform(data, date)
    load(transformed, environment)
  }

  def extract(env: String): DataFrame = {
    Seq(
      (1, "login", "safari"),
      (2, "login", "chrome"),
      (1, "logout", "safari"),
      (1, "logout", "safari"),
      (2, "expired", "IE6"),
      (3, "login", "firefox"))
      .toDF("user_id", "event", "browser")
  }

  def transform(data: DataFrame, date: LocalDate): DataFrame = {
    data
      .transform(SharedTransformations.addDatestamp(date))
      .transform(x => x.dropDuplicates())
  }

  def load(data: DataFrame, environment: String) = {
    data.show()

    // Uncomment the following block to write to a compatible catalog
    //    spark.catalog.setCurrentDatabase("DEFAULT_DB")
    //    data
    //      .coalesce(1)
    //      .write.partitionBy("ds")
    //      .mode("overwrite")
    //      .format("parquet")
    //      .saveAsTable("sample")

  }

}
