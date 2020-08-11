#!/usr/bin/env python
import os
import shutil
import yaml
import logging

MANIFEST = "manifest.yml"
GROUP_ID = "{{ cookiecutter.group_id }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"


def delete_resources_for_disabled_features():
    logging.debug("Delete resources from disabled features")
    with open(MANIFEST) as manifest_file:
        manifest = yaml.safe_load(manifest_file)
        for feature in manifest["features"]:
            if not feature["enabled"]:
                for resource in feature["resources"]:
                    delete_resource(resource)
    delete_resource(MANIFEST)


def delete_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
    elif os.path.isdir(resource):
        shutil.rmtree(resource)


def create_group_id_directory(source_path):
    destination_path = os.path.join(source_path, *GROUP_ID.split("."))
    shutil.copytree(source_path, destination_path)
    shutil.rmtree(os.path.join(source_path, MODULE_NAME))


def create_group_id_directories():
    logging.debug("Creating group directories")
    create_group_id_directory("src/main/scala")
    create_group_id_directory("src/test/scala")


if __name__ == "__main__":
    delete_resources_for_disabled_features()
    create_group_id_directories()
