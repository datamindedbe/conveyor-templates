#!/usr/bin/env python
import os
import shutil

from dataclasses import dataclass

project_name = "{{ cookiecutter.project_name }}"
role_creation = "{{ cookiecutter.role_creation }}"


@dataclass
class InitArguments:
    project_name: str


def fix_dbt_project():
    with open(f'./{project_name}/dbt_project.yml', "rt") as f:
        data = f.read()
        data = data.replace('my_new_project', project_name)
    with open(f'./{project_name}/dbt_project.yml', "wt") as f:
        f.write(data)


def initialize_dbt():
    os.mkdir('dbt')
    previous_dir = os.getcwd()
    os.chdir('dbt')
    try:
        os.environ["DBT_PROFILES_DIR"] = os.getcwd()
        import dbt.task.init as init_task  # late import so the environment variable is take into account
        task = init_task.InitTask(args=InitArguments(project_name), config=None)
        task.run()
        fix_dbt_project()
    finally:
        os.chdir(previous_dir)


def cleanup_resources():
    if role_creation == "none":
        shutil.rmtree("resources")


if __name__ == "__main__":
    initialize_dbt()
    cleanup_resources()

