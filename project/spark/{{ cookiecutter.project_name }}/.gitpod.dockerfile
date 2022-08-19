FROM gitpod/workspace-java-11

RUN sudo apt-get update \
  && sudo apt-get dist-upgrade -y \
  && sudo apt-get install -y --no-install-recommends \
    git ssh-client software-properties-common make \
    build-essential ca-certificates libpq-dev \
  && sudo apt-get clean \
  && sudo rm -rf \
    /var/lib/apt/lists/* /tmp/* /var/tmp/*