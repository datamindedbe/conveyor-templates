package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}

import java.time.LocalDate

import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common.SparkApplication
import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.config.{ApplicationConfig, ConfigurationException}
import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.transformations.SharedTransformations

import com.typesafe.scalalogging.LazyLogging
import org.apache.spark.sql.{DataFrame, SparkSession}

class SampleJob(spark: SparkSession) extends LazyLogging {

  import spark.implicits._

  def run(environment: String, date: LocalDate): Unit = {
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

    {% if cookiecutter.cloud == "aws" -%}
    //Uncomment the following block to write to a compatible catalog
    //spark.catalog.setCurrentDatabase("DEFAULT_DB")
    //(
    //    data.coalesce(1)
    //    .write.partitionBy("ds")
    //    .mode("overwrite")
    //    .format("parquet")
    //    .saveAsTable("sample")
    //)
    {%- elif cookiecutter.cloud == "azure" -%}
    // Uncomment the following block to write to a storage account
    // data.write.mode("overwrite")
    // .parquet(f"abfs://{storageContainer}@{storageAccount}.dfs.core.windows.net/{path}")
    {%- endif %}

  }

}

object SampleJob extends SparkApplication {

  try {
    // parse command line params
    val cliParams = ApplicationConfig.parse(args) match {
      case Some(value) => value
      case None => throw ConfigurationException("Arguments could not be parsed")
    }
    new SampleJob(spark).run(cliParams.environment, cliParams.date)
  } finally {
    spark.close()
  }
}


