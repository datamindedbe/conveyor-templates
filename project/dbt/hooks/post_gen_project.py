#!/usr/bin/env python
import os
import shutil
import dbt.task.init as init_task
from distutils.util import strtobool

from dataclasses import dataclass

project_name = "{{ cookiecutter.project_name }}".replace(
    "-", "_"
)  # dbt does not like projects with -
conveyor_managed_role = "{{ cookiecutter.conveyor_managed_role }}"
cloud = "{{ cookiecutter.cloud }}"
database_type = "{{ cookiecutter.database_type }}"
available_adapters = ["bigquery", "postgres", "redshift", "snowflake"]


@dataclass
class InitArguments:
    project_dir: str
    project_name: str
    skip_profile_setup: bool


def initialize_dbt():
    dbt_dir = os.path.join(os.getcwd(), "dbt")
    initialize_dbt_in_dir(dbt_dir, project_name)
    create_profile_from_samples(dbt_dir, database_type)


def initialize_dbt_in_dir(project_dir: str, project: str):
    current_dir = os.getcwd()
    os.chdir(project_dir)
    try:
        task = init_task.InitTask(
            args=InitArguments(project_dir=project_dir, project_name=project, skip_profile_setup=True), config=None
        )
        task.run()
    finally:
        os.chdir(current_dir)


def create_profile_from_samples(target_dir: str, adapter: str):
    sample_file = os.path.join(target_dir, f"{adapter}.yml")
    target_file = os.path.join(target_dir, "profiles.yml")
    shutil.copy(sample_file, target_file)
    for a in available_adapters:
        os.remove(os.path.join(target_dir, f"{a}.yml"))


def cleanup_resources():
    if not bool(strtobool(conveyor_managed_role)) or cloud == "azure":
        shutil.rmtree("resources")


if __name__ == "__main__":
    initialize_dbt()
    cleanup_resources()
