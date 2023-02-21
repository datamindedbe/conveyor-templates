#!/usr/bin/env python
import os
import shutil
import logging

RESOURCE_SOURCE = "./../{{ cookiecutter.resource_name }}"
RESOURCE_DESTINATION = "./../{{ cookiecutter.resource_path }}"


def move_to_resources_path():
    logging.info("Moving resources")
    if not os.path.exists(RESOURCE_DESTINATION):
        os.mkdir(RESOURCE_DESTINATION)

    files = os.listdir(RESOURCE_SOURCE)
    for f in files:
        destination_file = os.path.join(RESOURCE_DESTINATION, f)
        if os.path.exists(destination_file):
            os.remove(destination_file)
        shutil.move(os.path.join(RESOURCE_SOURCE, f), RESOURCE_DESTINATION)
    shutil.rmtree(RESOURCE_SOURCE)


if __name__ == "__main__":
    move_to_resources_path()
