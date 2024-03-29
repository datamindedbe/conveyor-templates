package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.config

import java.time.LocalDate


case class ConfigurationException(private val message: String = "",
                                  private val cause: Throwable = None.orNull)
  extends Exception(message, cause)

case class ApplicationConfig(date: LocalDate = LocalDate.now(), environment: String = "test")

object ApplicationConfig {
  def parse(args: Array[String]): Option[ApplicationConfig] = {
    val parser = new scopt.OptionParser[ApplicationConfig]("scalatest2") {
      opt[LocalDate]('d', "date")
        .action((localDate, config) => config.copy(date = localDate))
        .text("date in format YYYY-mm-dd")
        .optional()

      opt[String]('e', "environment")
        .action((environment, config) => config.copy(environment = environment))
        .text("environment we are executing in")
        .required()
    }
    parser.parse(args, ApplicationConfig())
  }
}
