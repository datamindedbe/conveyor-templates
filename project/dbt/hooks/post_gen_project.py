#!/usr/bin/env python
import os
import shutil
from distutils.util import strtobool

from dataclasses import dataclass

project_name = "{{ cookiecutter.project_name }}".replace(
    "-", "_"
)  # dbt does not like projects with -
conveyor_managed_role = "{{ cookiecutter.conveyor_managed_role }}"
cloud = "{{ cookiecutter.cloud }}"
database_type = "{{ cookiecutter.database_type }}"


@dataclass
class InitArguments:
    project_name: str
    adapter: str


def fix_dbt_project():
    with open(f"./{project_name}/dbt_project.yml", "rt") as f:
        data = f.read()
        data = data.replace("my_new_project", project_name)
    with open(f"./{project_name}/dbt_project.yml", "wt") as f:
        f.write(data)


def initialize_dbt():
    initialize_dbt_in_dir(os.getcwd(), database_type)


def initialize_dbt_in_dir(dir: str, db_type: str):
    dbt_dir = os.path.join(dir, "dbt")
    os.mkdir(dbt_dir)
    os.chdir(dbt_dir)
    try:
        os.environ["DBT_PROFILES_DIR"] = os.getcwd()
        import dbt.task.init as init_task  # late import so the environment variable is taken into account

        task = init_task.InitTask(
            args=InitArguments(project_name, db_type), config=None
        )
        task.run()
        fix_dbt_project()
    finally:
        os.chdir(dir)


def cleanup_resources():
    if not bool(strtobool(conveyor_managed_role)) or cloud == "azure":
        shutil.rmtree("resources")


if __name__ == "__main__":
    initialize_dbt()
    cleanup_resources()
