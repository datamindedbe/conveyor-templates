#!/usr/bin/env python
import os
import shutil
from distutils.util import strtobool

python_mgt = "{{ cookiecutter.python_package_management }}"
spark_version = "{{ cookiecutter.spark_version }}"
datafy_managed_role = "{{ cookiecutter.datafy_managed_role }}"
project_type = "{{ cookiecutter.project_type }}"


def datafy_managed_role_enabled():
    return bool(strtobool(datafy_managed_role))


def delete_resources_for_disabled_features():
    if python_mgt == "pip-tools":
        delete_resource("Pipfile")
        delete_resource("Pipfile-3.0.lock")
        delete_resource("Pipfile-2.4.lock")
        if spark_version == "2.4":
            os.rename("dev-requirements-2.txt", "dev-requirements.txt")
            delete_resource("dev-requirements-3.txt")
        elif spark_version == "3.0":
            os.rename("dev-requirements-3.txt", "dev-requirements.txt")
            delete_resource("dev-requirements-2.txt")
        else:
            raise Exception("Unknown spark version: " + spark_version)
    elif python_mgt == "pipenv":
        delete_resource("dev-requirements.in")
        delete_resource("dev-requirements-2.txt")
        delete_resource("dev-requirements-3.txt")
        delete_resource("requirements.in")
        delete_resource("requirements.txt")
        if spark_version == "2.4":
            os.rename("Pipfile-2.4.lock", "Pipfile.lock")
            delete_resource("Pipfile-3.0.lock")
        elif spark_version == "3.0":
            os.rename("Pipfile-3.0.lock", "Pipfile.lock")
            delete_resource("Pipfile-2.4.lock")
        else:
            raise Exception("Unknown spark version: " + spark_version)


def delete_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
    elif os.path.isdir(resource):
        shutil.rmtree(resource)


def cleanup_resources():
    if not datafy_managed_role_enabled():
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


if __name__ == "__main__":
    delete_resources_for_disabled_features()
    cleanup_resources()
    cleanup_streaming_resources()
    cleanup_batch_resources()

