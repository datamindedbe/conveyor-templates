#!/usr/bin/env python
import os
import dbt.task.init as init_task
from dataclasses import dataclass

project_name = "{{ cookiecutter.project_name }}"


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
    os.chdir('dbt')
    os.environ["DBT_PROFILES_DIR"] = os.getcwd()
    task = init_task.InitTask(args=InitArguments(project_name), config=None)
    task.run()
    fix_dbt_project()


if __name__ == "__main__":
    initialize_dbt()
