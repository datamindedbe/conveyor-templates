# {{ cookiecutter.package_name|capitalize}}

## Prerequisites

- [pyenv](https://github.com/pyenv/pyenv) (recommended)
- setting up slack alerting (optional)

### Configuring slack alerting
Before you can test this package, you need to have access to a Slack workspace and be able to create a channel and an application with incoming webhook.

- From your Slack workspace, create a channel you want to use to receive notification conveyor-notifications. The Slack documentation [here](https://slack.com/help/articles/201402297-Create-a-channel) walks you though it.
- From your Slack workspace, create a Slack app and an incoming Webhook. The Slack documentation [here](https://api.slack.com/messaging/webhooks) walks through the necessary steps. Take note of the Incoming Slack Webhook URL.

### Configuring a slack connection in Airflow
First we need to create an Airflow connection to provide your Incoming Slack Webhook URL to airflow.
You can do this using the Airflow UI or by using the secrets backend configuration feature of Conveyor, which is described [here](https://docs.dev.conveyordata.com/how-to-guides/working-with-airflow/airflow-secrets-backend).

- Navigate to https://app.conveyordata.com/environments and select the samples environment
- Navigate to Admin > Connections in airflow
- Add a connection of type HTTP
  - Enter slack_webhook as the connection id
  - Enter https://hooks.slack.com/services/ as the Host
  - Enter the remainder of your Webhook URL as the Password (formatted as T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX)
- Save


## Package Structure

```bash
root/
 |-- dags/
 |   |-- example_dag_alerts.py
 |-- pkgs/
 |   |-- alert.py
 |   |-- complex_alert.py
 |-- src/
 |   |-- alerting/
 |   |    |-- app.py
 |-- README.md
 |-- Dockerfile 
```

The package code is separated over 3 directories, each with their specific purpose:
- `pkgs`: this directory contains utility functions that you can call from your Airflow dags
- `src`: this contains directory contains more complex source code that you want to use across projects. 
  This code is packaged in a docker container and can be triggered in Airflow by defining a custom task or by adding a failure callback to your DAG.
- `dags`: this directory is actually *not* used for Conveyor packages but rather for Conveyor projects. Adding this in the same directory allows you to easily develop your package.
  Working with both a project and a package in the same directory is described in more detail [here](https://docs.conveyordata.com/how-to-guides/conveyor-packages/best-practices). You can remove the dags directory if you do not need it.

## Getting started
Start using this template as follows:
- create a trial version of your package: `conveyor package trail --version 0.0.1`
- test your package code in a Conveyor project:
  - create a sample project in your package directory: `conveyor project create --name testproject`. For more details look [here](https://docs.conveyordata.com/how-to-guides/conveyor-packages/best-practices)
  - add the package dependency in your `.conveyor/project.yaml` with content: 
  ```yaml
    dependencies:
      packages:
        - name: <packagename>
          versions: [0.0.1]
  ```
  - build and deploy your project to an environment: `conveyor project build && conveyor project deploy --env <some-environment>`. 
    If you are developing Airflow tasks in your package, you can also use `conveyor run` to test them.
  - trigger the `example-dag-alert-simple-callback` or the `example-dag-alert-complex-callback` dag in Airflow
- make changes to your package and run `conveyor package trial --version 0.0.1` to update the version in Airflow
- when you are happy with the current version, you can create a release of your package using: `conveyor package release --version 0.0.1`

## Concepts
This template package is created to show how packages can be used to create reusable code across 
projects within your organisation. One of the most popular usecases is: adding alerts to dags.

In a package you have 2 places to add common code, namely: `pkgs` directory and `src` directory.
In the next sections, we provide some guidance on when to use which directory.

### when to add functions to pkgs directory
Add functions to the `pkgs` directory when they are simple and can execute within an Airflow worker.
Typical usecases are wrapper functions/operators that abstract away some Airflow logic.
If you need additional python dependencies to execute your logic, this approach will not work as you cannot customize the Airflow python environment.

#### Steps
- Create python functions in your package that will be processed by Airflow
- trail/release your package
- Refer to your package in the Airflow dag code as follows: `common_alert = packages.load("common.alert", version=1.0.0, trial=True)`

### creating a docker image with common functionality
For more advanced usecases it might be needed to run it using a custom container.
Here you have full flexibility on which python dependencies that you want to use.
A typical usecase here is to add code for loading data from your datawarehouse.
Using this common logic, every project can create a task to copy the necessary data as a starting point of the pipeline.

#### Steps
- Write the necessary source code for your package
- Make sure you have a `Dockerfile` and package your src code in the Docker image
- Write a python function in the `pkgs` directory. This will run a container to execute your package source code using a Docker image as follows: `packages.image()`.
- trail/release your package
- Refer to your package in project dag code using: `common_alert = packages.load("common.alert", version=1.0.0, trial=True)` and trigger one of your common functions
