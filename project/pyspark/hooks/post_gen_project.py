#!/usr/bin/env python
import os
import shutil
from distutils.util import strtobool

conveyor_managed_role = "{{ cookiecutter.conveyor_managed_role }}"
cloud = "{{ cookiecutter.cloud }}"
project_type = "{{ cookiecutter.project_type }}"
dev_environment = "{{ cookiecutter.dev_environment }}"


def conveyor_managed_role_enabled():
    return bool(strtobool(conveyor_managed_role))


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
            os.remove(".gitpod.dockerfile")
        case "gitpod":
            shutil.rmtree(".devcontainer")
        case "codespaces":
            os.remove(".gitpod.yml")
            os.remove(".gitpod.dockerfile")
        case "all":
            pass


if __name__ == "__main__":
    cleanup_resources()
    cleanup_streaming_resources()
    cleanup_batch_resources()
    cleanup_development_environment()
