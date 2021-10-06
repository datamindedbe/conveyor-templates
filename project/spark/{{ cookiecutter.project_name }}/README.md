# {{ cookiecutter.project_name|capitalize}}

## Prerequisites

- [sdkman](https://sdkman.io/) (recommended)
- [java8](https://docs.scala-lang.org/overviews/jdk-compatibility/overview.html)


## Project Structure

```bash
root/
 |-- dags/
 |   |-- project.py
 |-- src/
 |   |-- main/
 |   |-- |-- scala/
 |   |-- |-- | -- group_id.nodule_name/
 |   |-- |-- | -- | -- common/
 |   |-- |-- | -- | -- config/
{%- if "batch" in cookiecutter.project_type %}
 |   |-- |-- | -- | -- jobs/
 |   |-- |-- | -- | -- transformations/
 |   |-- |-- |--  | -- RouterApp.sala
{%- endif %}
{%- if "streaming" in cookiecutter.project_type %}
 |   |-- |-- |--  | -- StreamingApp.sala
{%- endif %}
{%- if "batch" in cookiecutter.project_type %}
 |-- test/
 |   |-- scala/
 |   |-- | -- group_id.nodule_name/
 |   |-- |-- | -- common/
 |   |-- |-- | -- jobs/
 |   |-- |-- | -- transformations/
{%- endif %}
 |   Dockerfile
```

The main module contains the ETL job `RouterApp`. By default `RouterApp` accepts a number of arguments:
- `--date` the execution date
- `--env` the environment we are executing in
- `--jobs` one or more jobs that needs to be executed

## Concepts

## Commands
- `./gradlew test` to run all the tests
- `./gradlew clean shadowJar` to create the fat jar

{%- if "streaming" in cookiecutter.project_type %}

## Streaming in production

Streaming was enabled when rendering the template. To make your project run reliably in production there is
one important thing you need to change. You should always enable a checkpoint location for every query
you are running. The checkpoint location allows your application to recover in the event of a failure or
intentional shutdown (For example when doing a deploy of a new version). To know more about checkpointing
and its limitations check the spark document about it:
[https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing)

{%- endif %}
