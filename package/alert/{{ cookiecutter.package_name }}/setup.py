from glob import glob
from codecs import open
from os import path
from os.path import basename
from os.path import splitext

from setuptools import find_packages, setup

name = "{{ cookiecutter.package_name }}"
here = path.abspath(path.dirname(__file__))

# get the dependencies and installs
with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = [x.strip() for x in f if x.strip()]

setup(
    name=name,
    version="0.1.4",
    python_requires=">=3.10, <3.12",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    install_requires=requires,
    author="Data Minded",
    entry_points={},
    zip_safe=False,
    keywords="data pipelines, data engineering",
)
