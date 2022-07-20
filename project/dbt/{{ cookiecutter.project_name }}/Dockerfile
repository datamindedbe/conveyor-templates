FROM python:3.10.2-slim-bullseye as dbt-all

ARG dbt_core_ref=dbt-core@v1.1.0
ARG dbt_postgres_ref=dbt-core@v1.1.0
ARG dbt_redshift_ref=dbt-redshift@v1.1.0
ARG dbt_bigquery_ref=dbt-bigquery@v1.1.0
ARG dbt_snowflake_ref=dbt-snowflake@v1.1.0

RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y --no-install-recommends \
    git \
    ssh-client \
    software-properties-common \
    make \
    build-essential \
    ca-certificates \
    libpq-dev \
  && apt-get clean \
  && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*

# Env vars
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8

# Update python and install
RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir
RUN python -m pip install --no-cache "git+https://github.com/dbt-labs/${dbt_redshift_ref}#egg=dbt-redshift"
RUN python -m pip install --no-cache "git+https://github.com/dbt-labs/${dbt_bigquery_ref}#egg=dbt-bigquery"
RUN python -m pip install --no-cache "git+https://github.com/dbt-labs/${dbt_snowflake_ref}#egg=dbt-snowflake"
RUN python -m pip install --no-cache "git+https://github.com/dbt-labs/${dbt_postgres_ref}#egg=dbt-postgres&subdirectory=plugins/postgres"

# Set docker basics
WORKDIR /usr/app/dbt/
VOLUME /usr/app
ENTRYPOINT ["dbt"]

FROM dbt-all

WORKDIR /app
COPY . .
WORKDIR /app/dbt/{{ cookiecutter.project_name|replace("-", "_") }}

# install dependencies
RUN dbt deps
