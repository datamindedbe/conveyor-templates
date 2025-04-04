#!/usr/bin/env python
import os
import shutil
from distutils.util import strtobool

conveyor_managed_role = "{{ cookiecutter.conveyor_managed_role }}"
cloud = "{{ cookiecutter.cloud }}"
project_type = "{{ cookiecutter.project_type }}"
dev_environment = "{{ cookiecutter.dev_environment }}"

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
    cleanup_resources()
    cleanup_development_environment()
    # TODO: what is expected post-generation behavior?