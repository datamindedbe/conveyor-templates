package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}

import java.time.LocalDate
import java.time.format.DateTimeFormatter

import scopt.Read
import scopt.Read.reads

import scala.util.{Failure, Success, Try}

package object config {
  implicit val LocalDateSupport: Read[LocalDate] = reads { timestamp =>
    tryParseLocalDate(timestamp) match {
      case Success(localDate) => localDate
      case Failure(e) => throw new IllegalArgumentException(s"The given timestamp: [$timestamp] could not be parsed", e)
    }
  }

  private def tryParseLocalDate(timestamp: String): Try[LocalDate] = {
    Try {
      LocalDate.parse(timestamp, DateTimeFormatter.ISO_LOCAL_DATE)
    } recover {
      case _ =>
        LocalDate.parse(timestamp, DateTimeFormatter.ofPattern("yyyy/MM/dd"))
    }
  }
}
