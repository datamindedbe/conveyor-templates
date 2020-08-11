import os

from os import path

import yaml


def read_manifest():
    with open("templates.yaml", "r") as stream:
        return yaml.safe_load(stream)


def test_all_projects_in_manifest():
    projects = [p for p in os.listdir("project")]
    manifest = read_manifest()
    assert set(projects) == set(manifest["project"])


def test_projects_in_manifest_sorted_alphabetically():
    projects_sorted = read_manifest()["project"]
    projects_sorted.sort()
    projects_unsorted = read_manifest()["project"]
    assert projects_sorted == projects_unsorted


def test_all_resources_in_manifest():
    resources = []
    for cloud in os.listdir("resource"):
        for r in os.listdir(path.join("resource", cloud)):
            resources.append(f"{cloud}/{r}")
    manifest = read_manifest()
    assert set(resources) == set(manifest["resource"])


def test_resources__in_manifest_sorted_alphabetically():
    resource_sorted = read_manifest()["resource"]
    resource_sorted.sort()
    resource_unsorted = read_manifest()["resource"]
    assert resource_sorted == resource_unsorted
