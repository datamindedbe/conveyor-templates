import argparse

from pyspark.sql import SparkSession

from {{ cookiecutter.module_name }}.common.spark import ClosableSparkSession, SparkLogger


def main():
    parser = argparse.ArgumentParser(description="{{ cookiecutter.project_name }}")
    parser.add_argument(
        "-e", "--env", dest="env", help="environment we are executing in", required=True
    )
    args = parser.parse_args()

    with ClosableSparkSession("{{ cookiecutter.project_name }}") as session:
        run(session, args.env)


def run(spark: SparkSession, environment: str):
    """Runs the streaming application

    :return: None
    """
    logger = SparkLogger(spark)
    logger.info(f"Executing streaming job for {environment}")
    (
        spark.readStream.format("rate")
            .option("rowsPerSecond", "10")
            .load()
            .writeStream
            #In Production it is highly recommended to set a checkpoint location for your query
            #See Spark Structured Streaming documentation: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing
            #.option(
            #"checkpointLocation",
            #"s3://YOURBUCKET/checkpoints/YOUR_APPLICATION/YOUR_QUERY",
            #"abfs://YOURCONTAINER@YOURSTORAGEACCOUNT.dfs.core.windows.net/checkpoints/YOUR_APPLICATION/YOUR_QUERY"
            #)
            .outputMode("append")
            .format("console")
            .option("numRows", "100")
            .start()
            .awaitTermination()
    )


if __name__ == "__main__":
    main()