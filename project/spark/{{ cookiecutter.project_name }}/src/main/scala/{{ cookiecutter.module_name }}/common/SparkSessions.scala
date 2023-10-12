package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common

import org.apache.spark.sql.SparkSession

/**
 * Mixin provides the application with a [[org.apache.spark.sql.SparkSession]].
 */
trait SparkSessions {

  /**
   * Custom Spark configuration for the job.
   */
  val sparkOptions: Map[String, String] = Map.empty

  {% if cookiecutter.cloud == "aws" -%}
  private val defaultConfiguration: Map[String, String] = Map(

    "spark.serializer" -> "org.apache.spark.serializer.KryoSerializer",
    "spark.sql.sources.partitionOverwriteMode" -> "dynamic",
  )

  val spark: SparkSession = {
    (defaultConfiguration ++ sparkOptions)
      .foldLeft(SparkSession.builder()) {
        case (b, (key, value)) => b.config(key, value)
      }
      .enableHiveSupport()
      .getOrCreate()
  }

  {%- elif cookiecutter.cloud == "azure" -%}
  val spark: SparkSession = {
    SparkSession.builder().getOrCreate()
  }
  {%- endif %}
}

trait SparkApplication extends SparkSessions with App
