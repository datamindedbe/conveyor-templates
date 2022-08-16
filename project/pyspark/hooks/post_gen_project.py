#!/usr/bin/env python
import os
import shutil
from distutils.util import strtobool

spark_version = "{{ cookiecutter.spark_version }}"
conveyor_managed_role = "{{ cookiecutter.conveyor_managed_role }}"
cloud = "{{ cookiecutter.cloud }}"
project_type = "{{ cookiecutter.project_type }}"
dev_environment = "{{ cookiecutter.dev_environment }}"


def conveyor_managed_role_enabled():
    return bool(strtobool(conveyor_managed_role))


def delete_resources_for_disabled_features():
    if spark_version == "2.4":
        os.rename("dev-requirements-2.txt", "dev-requirements.txt")
        delete_resource("dev-requirements-3.txt")
    elif spark_version == "3.0":
        os.rename("dev-requirements-3.txt", "dev-requirements.txt")
        delete_resource("dev-requirements-2.txt")
    else:
        raise Exception("Unknown spark version: " + spark_version)


def delete_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
    elif os.path.isdir(resource):
        shutil.rmtree(resource)


def cleanup_resources():
    if not conveyor_managed_role_enabled() or cloud == "azure":
        shutil.rmtree("resources")


def cleanup_streaming_resources():
    if "streaming" in project_type:
        return
    delete_resource("streaming.yaml")
    delete_resource("src/{{ cookiecutter.project_name }}/streaming_app.py")


def cleanup_batch_resources():
    if "batch" in project_type:
        return
    delete_resource("dags")
    delete_resource("tests")
    delete_resource("src/{{ cookiecutter.project_name }}/transformations")
    delete_resource("src/{{ cookiecutter.project_name }}/app.py")


def cleanup_development_environment():
    match dev_environment:
        case "local":
            os.remove(".gitpod.yml")
            shutil.rmtree(".devcontainer")
        case "gitpod":
            shutil.rmtree(".devcontainer")
        case "codespaces":
            os.remove(".gitpod.yml")
        case "all":
            pass


if __name__ == "__main__":
    delete_resources_for_disabled_features()
    cleanup_resources()
    cleanup_streaming_resources()
    cleanup_batch_resources()
    cleanup_development_environment()
