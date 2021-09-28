#!/usr/bin/env python

spark_version = "{{ cookiecutter.spark_version }}"
project_type = "{{ cookiecutter.project_type }}"
scala_version = "{{ cookiecutter.scala_version }}"


if __name__ == "__main__":
    if "streaming" in project_type and spark_version != "3.0":
        raise Exception("Streaming is only supported when using spark 3")
    if "2.11" == scala_version and spark_version == "3.0":
        raise Exception("Scala 2.11 is only supported with spark 2")

