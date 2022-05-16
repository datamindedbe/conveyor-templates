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

    "fs.s3.impl" -> "org.apache.hadoop.fs.s3a.S3AFileSystem",
    "spark.serializer" -> "org.apache.spark.serializer.KryoSerializer",
    "spark.sql.sources.partitionOverwriteMode" -> "dynamic",

    // These values are set because of an issue with the current spark hive, glue connection
    // For more info see the conveyor docs:
    //https://docs.conveyordata.com/how-to-guides/troubleshooting/spark-pyspark-issues/#glue-orgapachehadoophivemetastoreapiinvalidobjectexception
    "spark.sql.hive.metastorePartitionPruning" -> "false",
    "spark.sql.hive.convertMetastoreParquet" -> "false"
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
