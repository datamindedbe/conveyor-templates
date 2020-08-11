package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}

import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common.SparkApplication
import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.config.{ApplicationConfig, ConfigurationException}
import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.jobs.EntryPointMapper
import com.typesafe.scalalogging.LazyLogging

object RouterApp extends SparkApplication with LazyLogging {

  try {
    // parse command line params
    val cliParams = ApplicationConfig.parse(args) match {
      case Some(value) => value
      case None => throw ConfigurationException("Arguments could not be parsed")
    }

    // route to the correct jobs
    cliParams.jobs.foreach(
      entryPoint => {
        val job = EntryPointMapper.mapEntryPointToJob(entryPoint)
        job.run(cliParams.environment, cliParams.date)
      }
    )
  } finally {
    spark.close()
  }
}
