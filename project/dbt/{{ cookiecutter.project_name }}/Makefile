current_dir:=$(shell pwd)
project_name:={{ cookiecutter.project_name|replace("-", "_") }}
project_dir:=$(current_dir)/dbt/$(project_name)
profiles_dir:=$(current_dir)/dbt
env_file:=$(current_dir)/.env
dbt_version:=0.21.0
docker_dbt_command:=docker run --rm --env-file $(env_file) --entrypoint /bin/bash --privileged -it -e NO_DOCKER=1 -p 8080:8080 -v $(current_dir):/workspace -w /workspace fishtownanalytics/dbt:$(dbt_version)

env:
	touch $(current_dir)/.env

shell: env
	eval "$(docker_dbt_command)"

deps:
	dbt deps --profiles-dir $(profiles_dir) --project-dir $(project_dir)

manifest:
	dbt compile --profiles-dir $(profiles_dir) --project-dir $(project_dir)
	cp $(project_dir)/target/manifest.json $(current_dir)/dags/manifest.json

debug:
	dbt debug --profiles-dir $(profiles_dir) --project-dir $(project_dir)

test:
	dbt test --profiles-dir $(profiles_dir) --project-dir $(project_dir)

run:
	dbt run --profiles-dir $(profiles_dir) --project-dir $(project_dir)

docs:
	dbt docs serve --profiles-dir $(profiles_dir) --project-dir $(project_dir)
