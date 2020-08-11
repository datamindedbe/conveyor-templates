package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common

import better.files._
import org.apache.spark.sql.SparkSession

trait SharedSparkSession {

  import SharedSparkSession._

  val spark: SparkSession = {
    val session = SparkSession
      .builder()
      .master("local[*]")
      .appName("LocalSparkTesting")
      .config("javax.jdo.option.ConnectionURL",
        s"jdbc:derby:;databaseName=$localMetastorePath;create=true")
      .config("datanucleus.rdbms.datastoreAdapterClassName",
        "org.datanucleus.store.rdbms.adapter.DerbyAdapter")
      .config("spark.sql.streaming.checkpointLocation", checkPointDirectory)
      .config("spark.sql.warehouse.dir", localWarehousePath)
      .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
      .config("spark.sql.avro.compression.codec", "snappy")
      .config("spark.sql.parquet.compression.codec", "snappy")
      .config("spark.ui.enabled", "false")
      .config("spark.hadoop.fs.s3a.connection.maximum", "100")
      .config("spark.hadoop.fs.s3a.experimental.input.fadvise", "random")
      .config("spark.hadoop.fs.s3a.readahead.range", "2048k")
      .config("fs.s3a.aws.credentials.provider",
        "com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
      .enableHiveSupport()
      .getOrCreate()

    session
  }
}

object SharedSparkSession {
  private val tmp = File.newTemporaryDirectory().deleteOnExit()

  val localMetastorePath: String = (tmp / "metastore").pathAsString
  val localWarehousePath: String = (tmp / "warehouse").pathAsString
  val checkPointDirectory: String = (tmp / "checkpoint").pathAsString
}
