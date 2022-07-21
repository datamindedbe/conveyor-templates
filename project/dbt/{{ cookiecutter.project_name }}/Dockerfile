FROM public.ecr.aws/dataminded/dbt:v1.1.0

WORKDIR /app
COPY . .
WORKDIR /app/dbt/{{ cookiecutter.project_name|replace("-", "_") }}

# install dependencies
RUN dbt deps
