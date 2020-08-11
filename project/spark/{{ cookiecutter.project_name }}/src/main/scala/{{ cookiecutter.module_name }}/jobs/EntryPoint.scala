package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.jobs

import java.time.LocalDate

import org.reflections.Reflections

import scala.collection.JavaConverters._
import scala.reflect.runtime.{universe => ru}
import ru._

class EntryPoint(runnerType: String) extends scala.annotation.StaticAnnotation

case class EntryPointException(private val message: String = "",
                               private val cause: Throwable = None.orNull)
  extends Exception(message, cause)

object EntryPointMapper {

  private lazy val entryPoints: Map[String, Job] = {
    val rm: ru.Mirror = ru.runtimeMirror(getClass.getClassLoader)

    val reflections = new Reflections("{{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.jobs")
    val jobClasses = reflections.getSubTypesOf(classOf[Job]).asScala
    val annotationName = typeOf[EntryPoint].typeSymbol.name.toString

    jobClasses.flatMap(jobClass => {
      val moduleSym = rm.staticModule(jobClass.getName.replace("$", ""))
      val annotations = moduleSym.annotations.filter(annotation => reflectAnnotationTypeName(annotation) == annotationName)
      val job = rm.reflectModule(moduleSym).instance.asInstanceOf[Job]
      annotations.map(annotation => (reflectRunnerType(annotation), job))
    }).toMap
  }

  private def reflectAnnotationTypeName(annotation: Annotation) = {
    annotation.tree.tpe.typeSymbol.name.toString
  }

  private def reflectRunnerType(annotation: Annotation) = {
    annotation.tree.children.tail.collectFirst { case Literal(Constant(runnerType: String)) => runnerType }.get
  }

  def mapEntryPointToJob(runnerType: String): Job = {
    entryPoints.get(runnerType) match {
      case Some(job) => job
      case None => throw new EntryPointException(f"Entrypoint ${runnerType} not found")
    }
  }
}

trait Job {
  def run(environment: String, date: LocalDate)
}
