#!/usr/bin/env python
import os
import shutil
from distutils.util import strtobool

import yaml
import logging

MANIFEST = "manifest.yml"
GROUP_ID = "{{ cookiecutter.group_id }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"
conveyor_managed_role = "{{ cookiecutter.conveyor_managed_role }}"
cloud = "{{ cookiecutter.cloud }}"
project_type = "{{ cookiecutter.project_type }}"
dev_environment = "{{ cookiecutter.dev_environment }}"


def delete_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
    elif os.path.isdir(resource):
        shutil.rmtree(resource)


def source_directory():
    return os.path.join("src", "main", "scala", *GROUP_ID.split("."), MODULE_NAME)


def create_group_id_directory(source_path):
    destination_path = os.path.join(source_path, *GROUP_ID.split("."))
    shutil.copytree(source_path, destination_path)
    shutil.rmtree(os.path.join(source_path, MODULE_NAME))


def create_group_id_directories():
    logging.debug("Creating group directories")
    create_group_id_directory(os.path.join("src", "main", "scala"))
    create_group_id_directory(os.path.join("src", "test", "scala"))


def cleanup_resources():
    if not bool(strtobool(conveyor_managed_role)) or cloud == "azure":
        shutil.rmtree("resources")


def cleanup_streaming_resources():
    if "streaming" in project_type:
        return
    delete_resource("streaming.yaml")
    delete_resource(os.path.join(source_directory(), "StreamingApp.scala"))


def cleanup_batch_resources():
    if "batch" in project_type:
        return
    delete_resource("dags")
    delete_resource(os.path.join("src", "test"))
    delete_resource(os.path.join(source_directory(), "transformations"))
    delete_resource(os.path.join(source_directory(), "SampleJob.scala"))


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
    create_group_id_directories()
    cleanup_resources()
    cleanup_streaming_resources()
    cleanup_batch_resources()
    cleanup_development_environment()
