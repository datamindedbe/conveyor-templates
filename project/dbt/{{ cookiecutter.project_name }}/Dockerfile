FROM public.ecr.aws/dataminded/dbt:v1.4.0

WORKDIR /app
COPY . .
WORKDIR /app/dbt/{{ cookiecutter.project_name|replace("-", "_") }}

# install dependencies
RUN dbt deps

ENV DBT_PROFILES_DIR="/app/dbt"
ENV DBT_PROJECT_DIR="/app/dbt/{{ cookiecutter.project_name|replace("-", "_") }}"

# Using DBT ls makes sure that the DBT cache is populated, this allows DBT to use the cache every time it is started up, this will significantly reduce the startup latency of DBT jobs with many models
RUN dbt ls