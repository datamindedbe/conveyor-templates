package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}

import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common.SparkApplication
import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.config.{ApplicationConfig, ConfigurationException}

import com.typesafe.scalalogging.LazyLogging
import org.apache.spark.sql.SparkSession


class StreamingApp(spark: SparkSession) extends LazyLogging {
  import spark.implicits._
  def run(env: String): Unit = {

    spark.readStream
      .format("rate")
      .option("rowsPerSecond", "10")
      .load
      .select("value")
      .map(_.toString())
      .writeStream
      //In Production it is highly recommended to set a checkpoint location for your query
      //See Spark Structured Streaming documentation: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing
      //.option(
      //"checkpointLocation",
      //"s3://YOURBUCKET/checkpoints/YOUR_APPLICATION/YOUR_QUERY",
      //"abfs://YOURCONTAINER@YOURSTORAGEACCOUNT.dfs.core.windows.net/checkpoints/YOUR_APPLICATION/YOUR_QUERY"
      //)
      .outputMode("append")
      .format("console")
      .option("numRows", "100")
      .start()
      .awaitTermination()
  }
}

object StreamingApp extends SparkApplication {

  try {
    val cliParams = ApplicationConfig.parse(args) match {
      case Some(value) => value
      case None => throw ConfigurationException("Arguments could not be parsed")
    }
    new StreamingApp(spark).run(cliParams.environment)
  } finally {
    spark.close()
  }

}
