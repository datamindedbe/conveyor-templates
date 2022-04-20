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

  private val defaultConfiguration: Map[String, String] = Map(

    {% if cookiecutter.cloud == "aws" -%}
    "fs.s3.impl" -> "org.apache.hadoop.fs.s3a.S3AFileSystem",
    "spark.serializer" -> "org.apache.spark.serializer.KryoSerializer",
    "spark.sql.sources.partitionOverwriteMode" -> "dynamic",

    // These values are set because of an issue with the current spark hive, glue connection
    // For more info see the datafy docs:
    //https://docs.datafy.cloud/how-to-guides/troubleshooting/spark-pyspark-issues/#glue-orgapachehadoophivemetastoreapiinvalidobjectexception
    "spark.sql.hive.metastorePartitionPruning" -> "false",
    "spark.sql.hive.convertMetastoreParquet" -> "false"
    {%- endif %}
  )

  val spark: SparkSession = {
    (defaultConfiguration ++ sparkOptions)
      .foldLeft(SparkSession.builder()) {
        case (b, (key, value)) => b.config(key, value)
      }

      {% if cookiecutter.cloud == "aws" -%}
      .enableHiveSupport()
      {%- endif %}
      .getOrCreate()
  }
}

trait SparkApplication extends SparkSessions with App
