package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.transformations

import java.sql.Date

import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions._
import java.time.LocalDate

object SharedTransformations {

  def addDatestamp(date: LocalDate)(df: DataFrame): DataFrame = {
    df.withColumn("ds", lit(Date.valueOf(date)))
  }

}
