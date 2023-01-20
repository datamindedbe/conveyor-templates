FROM public.ecr.aws/dataminded/dbt:v1.3.2

WORKDIR /app
COPY . .
WORKDIR /app/dbt/{{ cookiecutter.project_name|replace("-", "_") }}

# install dependencies
RUN dbt deps
