#!/usr/bin/env python
from distutils.util import strtobool
import os
import shutil

MANIFEST = "manifest.yml"

conveyor_managed_role = "{{ cookiecutter.conveyor_managed_role }}"
cloud = "{{ cookiecutter.cloud }}"


def delete_files(files):
    for file in files:
        os.remove(file)


def delete_folder(folder):
    shutil.rmtree(folder)


if __name__ == "__main__":
    if not bool(strtobool(conveyor_managed_role)) or cloud == "azure":
        delete_folder("resources")
