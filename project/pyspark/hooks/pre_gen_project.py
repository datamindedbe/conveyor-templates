#!/usr/bin/env python

spark_version = "{{ cookiecutter.spark_version }}"
project_type = "{{ cookiecutter.project_type }}"


if __name__ == "__main__":
    if "streaming" in project_type and spark_version != "3.0":
        raise Exception("Streaming is only supported when using spark 3")
