<a name="unreleased"></a>
## [Unreleased]

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

[Unreleased]: https://github.com/datamindedbe/datafy-templates/compare/0.3.0...HEAD
[0.3.0 - 2020-10-09]: https://github.com/datamindedbe/datafy-templates/compare/0.2.2...0.3.0
[0.2.2 - 2020-09-24]: https://github.com/datamindedbe/datafy-templates/compare/0.2.1...0.2.2
[0.2.1 - 2020-09-17]: https://github.com/datamindedbe/datafy-templates/compare/0.2.0...0.2.1
[0.2.0 - 2020-09-09]: https://github.com/datamindedbe/datafy-templates/compare/0.1.0...0.2.0
