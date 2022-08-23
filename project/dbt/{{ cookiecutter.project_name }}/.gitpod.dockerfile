FROM gitpod/workspace-python

ARG dbt_core_ref=dbt-core@v1.1.0
ARG dbt_postgres_ref=dbt-core@v1.1.0
ARG dbt_redshift_ref=dbt-redshift@v1.1.0
ARG dbt_bigquery_ref=dbt-bigquery@v1.1.0
ARG dbt_snowflake_ref=dbt-snowflake@v1.1.0

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
RUN pyenv install
RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir
RUN python -m pip install --no-cache "git+https://github.com/dbt-labs/${dbt_redshift_ref}#egg=dbt-redshift"
RUN python -m pip install --no-cache "git+https://github.com/dbt-labs/${dbt_bigquery_ref}#egg=dbt-bigquery"
RUN python -m pip install --no-cache "git+https://github.com/dbt-labs/${dbt_snowflake_ref}#egg=dbt-snowflake"
RUN python -m pip install --no-cache "git+https://github.com/dbt-labs/${dbt_postgres_ref}#egg=dbt-postgres&subdirectory=plugins/postgres"

# install sqlfluff (optional, but recommended)
RUN python -m pip install --no-cache sqlfluff