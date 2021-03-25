# Copyright (c) 2016 - present
# QuantumBlack Visual Analytics Ltd (a McKinsey company).
# All rights reserved.
#
# This software framework contains the confidential and proprietary information
# of QuantumBlack, its affiliates, and its licensors. Your use of these
# materials is governed by the terms of the Agreement between your organisation
# and QuantumBlack, and any unauthorised use is forbidden. Except as otherwise
# stated in the Agreement, this software framework is for your internal use
# only and may only be shared outside your organisation with the prior written
# permission of QuantumBlack.

"""Entry point for running a Kedro pipeline as a Python package."""
from pathlib import Path

from kedro.framework.project import configure_project
from kedro.framework.session import KedroSession


def run_package():
    """Entry point for kedro project."""
    # Entry point for running a Kedro project packaged with `kedro package`
    # using `python -m <project_package>.run` command.
    package_name = Path(__file__).resolve().parent.name
    configure_project(package_name)
    with KedroSession.create(package_name) as session:
        session.run()


if __name__ == "__main__":
    run_package()
