#!/usr/bin/env python
import os
import shutil


python_mgt = "{{ cookiecutter.python_package_management }}"
spark_version = "{{ cookiecutter.spark_version }}"


def delete_resources_for_disabled_features():
    if python_mgt == "pip-tools":
        delete_resource("Pipfile")
        delete_resource("Pipfile-3.0.lock")
        delete_resource("Pipfile-2.4.lock")
    elif python_mgt == "pipenv":
        delete_resource("dev-requirements.in")
        delete_resource("dev-requirements.txt")
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


if __name__ == "__main__":
    delete_resources_for_disabled_features()
