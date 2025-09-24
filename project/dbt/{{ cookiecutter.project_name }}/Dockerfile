FROM public.ecr.aws/dataminded/dbt:v1.10.11

WORKDIR /app
COPY . .
WORKDIR /app

# install dependencies
RUN dbt deps

ENV DBT_PROFILES_DIR="/app"
ENV DBT_PROJECT_DIR="/app"

# Using dbt ls makes sure that the dbt cache is populated, this allows dbt to use the cache every time it is started up.
# This will significantly reduce the startup latency of dbt jobs with many models.
RUN dbt ls
