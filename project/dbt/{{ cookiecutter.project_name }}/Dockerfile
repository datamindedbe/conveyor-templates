FROM fishtownanalytics/dbt:0.21.0

WORKDIR /app
COPY . .
WORKDIR /app/dbt/{{ cookiecutter.project_name|replace("-", "_") }}

# install dependencies
RUN dbt deps
