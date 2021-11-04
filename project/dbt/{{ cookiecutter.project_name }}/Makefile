current_dir:=$(shell pwd)
project_name:={{ cookiecutter.project_name|replace("-", "_") }}
local_project_dir:=$(current_dir)/dbt/$(project_name)
docker_project_dir:=/workspace/dbt/$(project_name)
profiles_dir:=$(current_dir)/dbt
env_file:=$(current_dir)/.env
dbt_version:=0.21.0
docker_dbt_command:=docker run --env-file $(env_file) --entrypoint /bin/bash --privileged -it -e NO_DOCKER=1 -p 8080:8080 -v $(current_dir):/workspace -w /workspace fishtownanalytics/dbt:$(dbt_version)

env:
	touch $(current_dir)/.env

warning:
	echo "\033[33mThis command needs to be executed in the docker shell. Open the README.md for more info.\033[0m"

shell: env
	eval "$(docker_dbt_command)"

deps: warning
	dbt deps --profiles-dir /workspace/dbt --project-dir $(docker_project_dir)

manifest: warning
	dbt compile --profiles-dir /workspace/dbt --project-dir $(docker_project_dir)
	cp $(docker_project_dir)/target/manifest.json /workspace/dags/manifest.json

debug: warning
	dbt debug --profiles-dir /workspace/dbt --project-dir $(docker_project_dir)

test: warning
	dbt test --profiles-dir /workspace/dbt --project-dir $(docker_project_dir)

run: warning
	dbt run --profiles-dir /workspace/dbt --project-dir $(docker_project_dir)

docs: warning
	dbt docs serve --profiles-dir /workspace/dbt --project-dir $(docker_project_dir)
