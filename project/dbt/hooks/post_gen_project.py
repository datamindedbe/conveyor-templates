#!/usr/bin/env python
import os
import shutil
from distutils.util import strtobool
from dbt.cli.main import dbtRunner

from dataclasses import dataclass

project_name = "{{ cookiecutter.project_name }}".replace(
    "-", "_"
)  # dbt does not like projects with -
conveyor_managed_role = "{{ cookiecutter.conveyor_managed_role }}"
cloud = "{{ cookiecutter.cloud }}"
database_type = "{{ cookiecutter.database_type }}"
available_adapters = ["bigquery", "postgres", "redshift", "snowflake", "duckdb"]
dev_environment = "{{ cookiecutter.dev_environment }}"


@dataclass
class InitArguments:
    project_dir: str
    project_name: str
    skip_profile_setup: bool


def remove_python_script(database_type):
    if not database_type == "duckdb":
        current_dir = os.getcwd()
        os.remove(os.path.join(current_dir, "query_duckdb.python"))


def initialize_dbt():
    dbt_dir = os.path.join(os.getcwd(), "dbt")
    initialize_dbt_in_dir(dbt_dir, project_name)
    create_profile_from_samples(dbt_dir, database_type)
    remove_python_script(database_type)


def initialize_dbt_in_dir(project_dir: str, project: str):
    current_dir = os.getcwd()
    os.chdir(project_dir)
    try:
        res = dbtRunner().invoke(["init", "--skip-profile-setup", f"--project-dir={project_dir}", f"--profiles-dir={project_dir}", project])
        if not res.success:
            raise Exception(res.exception)
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


def cleanup_development_environment():
    match dev_environment:
        case "local":
            os.remove(".gitpod.yml")
            os.remove(".gitpod.dockerfile")
            shutil.rmtree(".devcontainer")
        case "gitpod":
            shutil.rmtree(".devcontainer")
        case "codespaces":
            os.remove(".gitpod.yml")
            os.remove(".gitpod.dockerfile")
        case "all":
            pass


def fix_dbt_project():
    with open(f'./dbt/{project_name}/dbt_project.yml', "rt") as f:
        data = f.read()
        data = data.replace(f"profile: '{project_name}'", "profile: 'default'")
    with open(f'./dbt/{project_name}/dbt_project.yml', "wt") as f:
        f.write(data)


if __name__ == "__main__":
    initialize_dbt()
    cleanup_resources()
    cleanup_development_environment()
    fix_dbt_project()
