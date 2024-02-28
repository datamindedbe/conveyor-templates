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
    dbt_dir = os.getcwd()
    initialize_dbt_in_dir(dbt_dir)
    create_profile_from_samples(dbt_dir, database_type)
    remove_python_script(database_type)


def initialize_dbt_in_dir(dir: str):
    os.chdir(dir)
    try:
        res = dbtRunner().invoke(["init", "--skip-profile-setup", f"--project-dir={dir}", f"--profiles-dir={dir}", 'temp'])
        if not res.success:
            raise Exception(res.exception)
    finally:
        os.chdir(dir)


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
    root_dir = os.getcwd()
    dbt_dir = os.path.join(root_dir,'temp')
    files = os.listdir(dbt_dir)
    for file in files:
        if file == 'README.md' or file == '.gitignore':
            continue
        file_name = os.path.join(dbt_dir, file)
        shutil.move(file_name, root_dir)
    shutil.rmtree(dbt_dir)
    with open(f'./dbt_project.yml', "rt") as f:
        data = f.read()
        data = data.replace(f"profile: 'temp'", "profile: 'default'")
        data = data.replace("temp", f"{project_name}")
    with open(f'./dbt_project.yml', "wt") as f:
        f.write(data)


if __name__ == "__main__":
    initialize_dbt()
    cleanup_resources()
    cleanup_development_environment()
    fix_dbt_project()
