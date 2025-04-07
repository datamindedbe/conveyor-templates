FROM gitpod/workspace-python

RUN sudo apt-get update \
  && sudo apt-get dist-upgrade -y \
  && sudo apt-get install -y --no-install-recommends \
    git \
    ssh-client \
    software-properties-common \
    make \
    build-essential \
    ca-certificates \
    libpq-dev \
  && sudo apt-get clean \
  && sudo rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*

RUN wget "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -O "awscliv2.zip" && \
    unzip awscliv2.zip && \
    sudo ./aws/install --install-dir /opt/aws-cli --bin-dir /usr/local/bin/ && \
    sudo chmod a+x /opt/
# Env vars
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8

# Update python and install
COPY .python-version .python-version
RUN cd /home/gitpod/.pyenv && git fetch && git checkout v2.3.24 #Update pyenv
RUN pyenv install
RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir

# install sqlfluff (optional, but recommended)
RUN python -m pip install --no-cache sqlfluff