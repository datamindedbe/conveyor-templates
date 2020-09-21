#!/usr/bin/env python
import os
import shutil
import yaml

MANIFEST = "manifest.yml"

pip_env_files = [
    "Pipfile",
    "Pipfile.lock",
]

pip_tools_files = [
    "dev-requirements.in",
    "dev-requirements.txt",
    "requirements.in",
    "requirements.txt",
]

python_mgt = "{{ cookiecutter.python_package_management }}"
role_creation = "{{ cookiecutter.role_creation }}"


def delete_files(files):
    for file in files:
        os.remove(file)


def delete_folder(folder):
    shutil.rmtree(folder)


if __name__ == "__main__":
    if python_mgt == "pipenv":
        delete_files(pip_tools_files)
    elif python_mgt == "pip-tools":
        delete_files(pip_env_files)
    if role_creation == "none":
        delete_folder("resources")
