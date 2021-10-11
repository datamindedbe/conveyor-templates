package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common

import java.sql.Date

import org.apache.commons.lang3.StringUtils
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.catalyst.util.DateTimeUtils

import java.sql.Date
import java.text.SimpleDateFormat
import java.util.{Locale, TimeZone}

object DataFramePrettyPrinter {
  val dateFormat = new SimpleDateFormat("yyyy-MM-dd", Locale.US)
  dateFormat.setTimeZone(TimeZone.getDefault)

  def prettyPrintDataFrame(df: DataFrame, number: Int, truncate: Int = 20): String = {
    val numRows = number.max(0)
    val takeResult = df.take(numRows + 1)
    val hasMoreData = takeResult.length > numRows
    val data = takeResult.take(numRows)

    val header = df.schema.fieldNames.toSeq

    def asReadableRows = {
      data.map { row =>
        row.toSeq.map { cell =>
          val str = cell match {
            case null => "null"
            case binary: Array[Byte] => binary.map("%02X".format(_)).mkString("[", " ", "]")
            case array: Array[_] => array.mkString("[", ", ", "]")
            case seq: Seq[_] => seq.mkString("[", ", ", "]")
            case d: Date => dateFormat.format(d)
            case _ => cell.toString
          }
          if (truncate > 0 && str.length > truncate) {
            // do not show ellipses for strings shorter than 4 characters.
            if (truncate < 4) str.substring(0, truncate)
            else str.substring(0, truncate - 3) + "..."
          } else {
            str
          }
        }: Seq[String]
      }
    }

    // For array values, replace Seq and Array with square brackets
    // For cells that are beyond `truncate` characters, replace it with the
    // first `truncate-3` and "..."
    val rows: Seq[Seq[String]] = header +: asReadableRows

    val sb = new StringBuilder

    // Initialise the width of each column to a minimum value of '3'
    val colWidths = Array.fill(header.length)(3)

    // Compute the width of each column
    for (row <- rows) {
      for ((cell, i) <- row.zipWithIndex) {
        colWidths(i) = math.max(colWidths(i), cell.length)
      }
    }

    // Create SeparateLine
    val sep: String = colWidths.map("-" * _).addString(sb, "+", "+", "+\n").toString()

    // column names
    rows.head.zipWithIndex
      .map {
        case (cell, i) =>
          if (truncate > 0) {
            StringUtils.leftPad(cell, colWidths(i))
          } else {
            StringUtils.rightPad(cell, colWidths(i))
          }
      }
      .addString(sb, "|", "|", "|\n")

    sb.append(sep)

    // data
    rows.tail.map {
      _.zipWithIndex
        .map {
          case (cell, i) =>
            if (truncate > 0) {
              StringUtils.leftPad(cell.toString, colWidths(i))
            } else {
              StringUtils.rightPad(cell.toString, colWidths(i))
            }
        }
        .addString(sb, "|", "|", "|\n")
    }

    sb.append(sep)

    // For Data that has more than "numRows" records
    if (hasMoreData) {
      val rowsString = if (numRows == 1) "row" else "rows"
      sb.append(s"only showing top $numRows $rowsString\n")
    }

    sb.toString()
  }
}
