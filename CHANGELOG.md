<a name="unreleased"></a>
## unreleased

## [1.5.0 - 2023-11-20]

### features
- Upgrade to spark 3.5.0

## [1.4.1 - 2023-11-06]

### features
- Remove the env_worker_role tf variable as it is not supported anymore
- Remove unnecessary Spark configuration as it is fixed in Spark

## [1.4.0 - 2023-08-21]
### features
- Upgrade dbt to version 1.6.0
- Replace gitpod install scripts to our static scripts site
- Upgrade cryptography and certifi to latest version without security issues
- Regenerate dependencies to fix a mix of security issues

## [1.3.2 - 2023-08-07]
### features
- Upgrade to spark 3.4.1

## [1.3.1 - 2023-07-18]

### features
- Fix small typo in spark-iam-glue-role

## [1.3.0 - 2023-05-02]

### features
- Upgrade dbt to 1.5.0

## [1.2.1 - 2023-03-08]

### features
- Support duckdb when creating dbt projects
- Upgrade the dbt image to use dbt 1.4.0-1
- Add a dbt resources template
- Improve the DBT startup latency, by running `dbt ls` in the docker image

## [1.2.0 - 2023-02-01]

### features
- Upgrade the python template dependencies
- Upgrade the pyspark template to spark 3.3.1, also upgrade the dependencies
- Upgrade the spark template to spark 3.3.1, also upgrade the dependencies
- Upgrade spark template gradle version to 7.6
- Upgrade DBT support to v1.3.2
- Change manifest generation such that it does not require a connection to the database
- Change the dbt template to make it easier to get started

### removals
- Remove support for pyspark 2.x support from the pyspark template
- Remove support for spark 2.x support from the spark template

## [1.1.1 - 2022-08-23]

### features
- Improve gitpod setup to install requirements/dependencies when starting workspace

## [1.1.0 - 2022-08-16]

### features
- Use strict uuid pattern matching in the resources. (@stijndehaes)
- Upgrade the resource folder assume role policies to use the service account. (@stijndehaes)
- Upgrade spark images to our latest releases. (@stijndehaes)
- Upgrade to DBT 1.1.0 (@pascal-knapen)
- Add gitpod and codespaces configuration (@pascal-knapen)

## [1.0.0 - 2022-05-19]

### features

- Rename datafy to conveyor. (@nclaeys)

### bugfixes

- fixed a typo in the cookiecutter.json files such that datafy_managed_role is correctly set. (@nclaeys)

## [0.16.1 - 2022-05-10]

### features

- use new spark image which supports both azure and aws. (@nclaeys)

## [0.16.0 - 2022-05-05]

### features

- Make the templates work for both azure and aws.
- use newest spark version: 3.2.1 in the templates

### bugfixes

- update python versions such that they work with Apple Clang 13+ (@nclaeys)

### bugfixes

## [0.15.5 - 2022-03-16]

- Update the spark settings so the aws glue integration works again (@stijndehaes)
- Use dots instead of underscores for specifying the Datafy_instance_type. (@nclaeys)

## [0.15.4 - 2022-01-07]

### bugfixes

- Update spark3 image versions such that they are protected against a vulnerability with log4j 1.x (@nclaeys)
- Update spark3 images such that setuptools installs python packages in the correct directory, after a breaking change in release 60.0.0 (@nclaeys)
- Change pyspark template to not install python projects in editable mode (@nclaeys)

## [0.15.3 - 2021-11-30]

### features
- dbt template to use the official dbt image
- dbt template to use the DatafyDbtTaskFactory
- dbt template with update makefile and readme

## [0.15.2 - 2021-11-19]

### bugfixes

- Correct resources s3 template to use like instead of equals in trust relationship condition (@nclaeys)

## [0.15.1 - 2021-11-05]

### bugfixes
- Use the spark 3.2.0 scala 2.13 image (@stijndehaes)

## [0.15.0 - 2021-10-28]

### features
- Upgrade spark to 3.2.0 (@stijndehaes)
- Remove pipenv support from the pyspark template as it was hardly used and hard to maintain (@stijndehaes)
- Upgrade python project to python 3.9 (@nclaeys)
- Remove pipenv support from the python template as it was hardly used and hard to maintain (@nclaeys)
- Upgrade dbt to 0.21.0 (@stijndehaes)

## [0.14.0 - 2021-10-13]

### features
- Added streaming support to the spark project (@stijndehaes)
- Extend docker ignore to ignore more of the common virtual env locations (@stijndehaes)

### bugfix
- Fixed an issue in the `streaming.yaml` file of the pyspark template where the project name instead of the module name was used.

## [0.13.0 - 2021-09-27]

### features
- Added streaming support to the pyspark project (@stijndehaes)

### bugfixes
- Updating the python version when using pyenv in the python template (@pascal-knapen)

## [0.12.1 - 2021-08-12]

### bugfixes
- Fixed import issues in the pyspark template (@nclaeys)

## [0.12.0 - 2021-07-27]

### features

- Add `.gitignore` file to dbt project template (@jvanbuel)
- Upgrade to public.ecr.aws/dataminded/spark-k8s-glue:v3.1.2-hadoop-3.3.1-v2 image (@stijndehaes)

## [0.11.0 - 2021-07-07]

### features

- Upgrade spark images to v2 (@stijndehaes)
- Upgrade spark images to hadoop 3.3.1 (@stijndehaes)
- Simplify the python template (@stijndehaes)
- Simplify the pyspark template (@stijndehaes)

### bugfixes
- Fix the assume role policies (@stijndehaes)

## [0.10.0 - 2021-06-11]

### features:
- Project names with underscores will see their underscores replace with dots in Datafy 0.45.2 for the DatafyContainerOperatorV2 (@stijndehaes)
- Upgrade spark version to 3.1.2 (@stijndehaes)

## [0.9.0 - 2021-05-18]

### features:
- Upgrade to Datafy Operators V2 (@stijndehaes)

### bugfixes:
- Removing absolute `__init__.py` files
- Adding `.python-version` files to match the requirement files

## [0.8.1 - 2021-04-26]

### features:
- Remove the name parameter from the DatafyContainerOperator, from 0.44.0 this will not be required anymore. (@stijndehaes)

## [0.8.0 - 2021-04-12]

### features:
- Change the operator import paths, from datafy 0.42.0 they are exported under `datafy.operator.*` (@stijndehaes)
- For airflow 2.0 the plugin path has to be added to the macro, so added this path to macros to be Airflow 2.0 compliant, only works from datafy 0.42.0 (@stijndehaes)

## [0.7.0 - 2021-03-12]

### features:

- Remove automount_service_account_token which is default true in kubernetes terraform provider version 2 (@stijndehaes)
- Upgrade templates to spark 3.1.1 (@stijndehaes)
- Upgrade spark template to gradle 0.7.2 (@stijndehaes)

## [0.6.0 - 2021-03-01]

### features:
- From datafy version 0.39.0 the image field will not be required anymore (@stijndehaes)
- From datafy version 0.39.0 the path field in the role is not required anymore (@stijndehaes)
- Make pip-compile for dev-requirements use the requirements for production as a constraint, this reduces version conflicts (@stijndehaes)
- Update templates to use spark 3.0.2 (@stijndehaes)

## [0.5.0 - 2021-02-15]

### features:
- Added support for datafy instance types (@stijndehaes)
- Upgrade dbt to 0.19.0 (@stijndehaes)
- Dbt template added makefile with useful dbt commands (@stijndehaes)

## [0.4.0 - 2021-01-15]

### features:
- Update python and pyspark readme to include a section explaining the usage of piptools (@vlieven)
- Update to the new way of importing operators ahead of the airflow 2.0 upgrade (@stijndehaes)

## [0.3.3 - 2020-12-30]

### features:
- Change from docker hub images to public ECR images: https://gallery.ecr.aws/dataminded/spark-k8s-glue (@stijndehaes)

## [0.3.2 - 2020-12-09]

### features:
- Upgrade the spark 2.4.3 images to the latest version. This version only includes one version of the aws sdk. (@stijndehaes)

### bugfixes:
- Make sure the generated service account are kubernetes compliant (@stijndehaes)

## [0.3.1 - 2020-11-06]

### bugfixes:
- Docker image pin python version to 3.9 (@stijndehaes) 

## [0.3.0 - 2020-10-09]

### features:

- In python template configure the logging framework. This adds an example on how to change the logging level (@stijndehaes)

### bugfixes:
- Remove resource in dbt template when role_creation is none (@pascal-knapen)

## [0.2.2 - 2020-09-24]

### bugfixes:
- Fix spark 2.4 support for the pyspark template. Pip3 binary did not exist so created a symlink to the pip3.6 binary to fix this (@stijndehaes)
- Remove resource in python template when role_creation is none (@stijndehaes)
- Upgrade spark 3 support to 3.0.1 and hadoop to 3.3.0 (@stijndehaes)

## [0.2.1 - 2020-09-17]

### docs:
- updated the Development documentations

### features:
- Allow this image to be ran under a non-root user in /app directory. (@stijndehaes)

## [0.2.0 - 2020-09-09]

### features:
- A project template for [dbt](https://www.getdbt.com/) projects (@pascal-knapen).

### bugfixes:
- In the spark template there was a lingering enable_glue setting that was unused. It is now removed (@stijndehaes)

## 0.1.0 - 2020-08-11

First release of the templates

[Unreleased]: https://github.com/datamindedbe/datafy-templates/compare/1.5.0...HEAD
[1.4.1 - 2023-08-21]: https://github.com/datamindedbe/datafy-templates/compare/1.4.1...1.5.0
[1.4.1 - 2023-08-21]: https://github.com/datamindedbe/datafy-templates/compare/1.4.0...1.4.1
[1.4.0 - 2023-08-21]: https://github.com/datamindedbe/datafy-templates/compare/1.3.2...1.4.0
[1.3.2 - 2023-08-07]: https://github.com/datamindedbe/datafy-templates/compare/1.3.1...1.3.2
[1.3.1 - 2023-07-18]: https://github.com/datamindedbe/datafy-templates/compare/1.3.0...1.3.1
[1.3.0 - 2023-05-02]: https://github.com/datamindedbe/datafy-templates/compare/1.2.1...1.3.0
[1.2.1 - 2023-03-08]: https://github.com/datamindedbe/datafy-templates/compare/1.2.0...1.2.1
[1.2.0 - 2023-02-01]: https://github.com/datamindedbe/datafy-templates/compare/1.1.1...1.2.0
[1.1.1 - 2022-08-23]: https://github.com/datamindedbe/datafy-templates/compare/1.1.0...1.1.1
[1.1.0 - 2022-08-16]: https://github.com/datamindedbe/datafy-templates/compare/1.0.0...1.1.0
[1.0.0 - 2022-05-19]: https://github.com/datamindedbe/datafy-templates/compare/0.16.1...1.0.0
[0.16.1 - 2022-05-10]: https://github.com/datamindedbe/datafy-templates/compare/0.16.0...0.16.1
[0.16.0 - 2022-05-05]: https://github.com/datamindedbe/datafy-templates/compare/0.15.5...0.16.0
[0.15.5 - 2022-03-16]: https://github.com/datamindedbe/datafy-templates/compare/0.15.4...0.15.5
[0.15.4 - 2022-01-07]: https://github.com/datamindedbe/datafy-templates/compare/0.15.3...0.15.4
[0.15.3 - 2021-11-30]: https://github.com/datamindedbe/datafy-templates/compare/0.15.2...0.15.3
[0.15.2 - 2021-11-19]: https://github.com/datamindedbe/datafy-templates/compare/0.15.1...0.15.2
[0.15.1 - 2021-11-05]: https://github.com/datamindedbe/datafy-templates/compare/0.15.0...0.15.1
[0.15.0 - 2021-10-28]: https://github.com/datamindedbe/datafy-templates/compare/0.14.0...0.15.0
[0.14.0 - 2021-10-13]: https://github.com/datamindedbe/datafy-templates/compare/0.13.0...0.14.0
[0.13.0 - 2021-09-27]: https://github.com/datamindedbe/datafy-templates/compare/0.12.1...0.13.0
[0.12.1 - 2021-08-12]: https://github.com/datamindedbe/datafy-templates/compare/0.12.0...0.12.1
[0.12.0 - 2021-07-27]: https://github.com/datamindedbe/datafy-templates/compare/0.11.0...0.12.0
[0.11.0 - 2021-07-07]: https://github.com/datamindedbe/datafy-templates/compare/0.10.0...0.11.0
[0.10.0 - 2021-06-11]: https://github.com/datamindedbe/datafy-templates/compare/0.9.0...0.10.0
[0.9.0 - 2021-05-18]: https://github.com/datamindedbe/datafy-templates/compare/0.8.1...0.9.0
[0.8.1 - 2021-04-26]: https://github.com/datamindedbe/datafy-templates/compare/0.8.0...0.8.1
[0.8.0 - 2021-04-12]: https://github.com/datamindedbe/datafy-templates/compare/0.7.0...0.8.0
[0.7.0 - 2021-03-12]: https://github.com/datamindedbe/datafy-templates/compare/0.6.0...0.7.0
[0.6.0 - 2021-03-01]: https://github.com/datamindedbe/datafy-templates/compare/0.5.0...0.6.0
[0.5.0 - 2021-02-15]: https://github.com/datamindedbe/datafy-templates/compare/0.4.0...0.5.0
[0.4.0 - 2021-01-15]: https://github.com/datamindedbe/datafy-templates/compare/0.3.3...0.4.0
[0.3.3 - 2020-12-30]: https://github.com/datamindedbe/datafy-templates/compare/0.3.2...0.3.3
[0.3.2 - 2020-12-09]: https://github.com/datamindedbe/datafy-templates/compare/0.3.1...0.3.2
[0.3.1 - 2020-11-06]: https://github.com/datamindedbe/datafy-templates/compare/0.3.0...0.3.1
[0.3.0 - 2020-10-09]: https://github.com/datamindedbe/datafy-templates/compare/0.2.2...0.3.0
[0.2.2 - 2020-09-24]: https://github.com/datamindedbe/datafy-templates/compare/0.2.1...0.2.2
[0.2.1 - 2020-09-17]: https://github.com/datamindedbe/datafy-templates/compare/0.2.0...0.2.1
[0.2.0 - 2020-09-09]: https://github.com/datamindedbe/datafy-templates/compare/0.1.0...0.2.0
