package {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.jobs

import {{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.common.SharedSparkSession
import org.scalatest.{FunSuite, Matchers}

class EntryPointTest extends FunSuite with SharedSparkSession with Matchers {

  test("A job can be discovered by its entry point name") {
    val test = EntryPointMapper.mapEntryPointToJob("sample")
    test should not be null
  }

  test("When an entry point cannot be found, an exception is thrown") {
    an [EntryPointException] should be thrownBy EntryPointMapper.mapEntryPointToJob("foobar")
  }

}
