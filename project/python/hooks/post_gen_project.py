#!/usr/bin/env python
import os
import shutil
import yaml

MANIFEST = "manifest.yml"


def delete_resources_for_disabled_features():
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


if __name__ == "__main__":
    delete_resources_for_disabled_features()
