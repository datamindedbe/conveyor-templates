FROM gitpod/workspace-python

RUN sudo apt-get update \
  && sudo apt-get dist-upgrade -y \
  && sudo apt-get install -y --no-install-recommends \
    git ssh-client software-properties-common make \
    build-essential ca-certificates libpq-dev \
  && sudo apt-get clean \
  && sudo rm -rf \
    /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Update python and install
COPY .python-version .python-version
RUN pyenv install
RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir