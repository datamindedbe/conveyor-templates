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
 |   |-- |-- | -- | -- jobs/
 |   |-- |-- | -- | -- transformations/
 |   |-- |-- |--  | -- RouterApp.sala
 |-- test/
 |   |-- scala/
 |   |-- | -- group_id.nodule_name/
 |   |-- |-- | -- common/
 |   |-- |-- | -- jobs/
 |   |-- |-- | -- transformations/
 |   Dockerfile
```

The main module contains the ETL job `RouterApp`. By default `RouterApp` accepts a number of arguments:
- `--date` the execution date
- `--env` the environment we are executing in
- `--jobs` one or more jobs that needs to be executed

## Concepts

### Separate job breakdown from scheduling
Jobs can be found in the `jobs/` directory. A job function needs to be annotated with `@EntryPoint(runnerType = "sample")`.
This approach is based on the article [Scaling a Mature Data Pipeline](https://medium.com/airbnb-engineering/scaling-a-mature-data-pipeline-managing-overhead-f34835cbc866)
 and can be used to manage scheduling overhead.

## Commands
{%- if cookiecutter.build_tool == "gradle" %}
- `./gradlew test` to run all the tests
- `./gradlew clean shadowJar` to create the fat jar
{%- endif %}
