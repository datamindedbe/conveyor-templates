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
    "fs.s3.impl" -> "org.apache.hadoop.fs.s3a.S3AFileSystem",
    "spark.serializer" -> "org.apache.spark.serializer.KryoSerializer",
    "spark.sql.sources.partitionOverwriteMode" -> "dynamic"
  )

  val spark: SparkSession = {
    (defaultConfiguration ++ sparkOptions)
      .foldLeft(SparkSession.builder()) {
        case (b, (key, value)) => b.config(key, value)
      }
      .enableHiveSupport()
      .getOrCreate()
  }
}

trait SparkApplication extends SparkSessions with App
