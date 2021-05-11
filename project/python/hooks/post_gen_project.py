#!/usr/bin/env python
from distutils.util import strtobool
import os
import shutil

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
datafy_managed_role = "{{ cookiecutter.datafy_managed_role }}"


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
    if not bool(strtobool(datafy_managed_role)):
        delete_folder("resources")
