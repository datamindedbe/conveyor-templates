#!/usr/bin/env python
import os
import shutil
from distutils.util import strtobool
import subprocess
from subprocess import CalledProcessError

conveyor_managed_role = "{{ cookiecutter.conveyor_managed_role }}"
cloud = "{{ cookiecutter.cloud }}"
dev_environment = "{{ cookiecutter.dev_environment }}"
database_type = "{{ cookiecutter.database_type }}"

def initialize_sqlmesh():
    try:
        subprocess.run(["sqlmesh", "init", database_type], check=True, capture_output=True)
    except CalledProcessError as e:
        raise Exception(f"Failed to initialize SQLMesh: {e.stderr.decode()}") from e


def cleanup_resources():
    if not bool(strtobool(conveyor_managed_role)) or cloud == "azure":
        shutil.rmtree("resources")


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
    initialize_sqlmesh()
    cleanup_resources()
    cleanup_development_environment()
    # TODO: what is expected post-generation behavior?