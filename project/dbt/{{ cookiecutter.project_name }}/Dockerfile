FROM public.ecr.aws/dataminded/dbt:v1.4.0-1

WORKDIR /app
COPY . .
WORKDIR /app/dbt/{{ cookiecutter.project_name|replace("-", "_") }}

# install dependencies
RUN dbt deps

ENV DBT_PROFILES_DIR="/app/dbt"
ENV DBT_PROJECT_DIR="/app/dbt/{{ cookiecutter.project_name|replace("-", "_") }}"