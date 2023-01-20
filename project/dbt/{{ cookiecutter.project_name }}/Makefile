current_dir:=$(shell pwd)
project_name:={{ cookiecutter.project_name|replace("-", "_") }}
project_dir:=$(current_dir)/dbt/$(project_name)
profiles_dir:=$(current_dir)/dbt
env_file:=$(current_dir)/.env
dbt_version:=v1.3.2
os_docker_flag:=
ifeq ($(shell uname -s),Linux)
	os_docker_flag += --add-host host.docker.internal:host-gateway
endif
docker_dbt_command:=docker run --rm $(os_docker_flag) --env-file $(env_file) --entrypoint /bin/bash --privileged -it -e NO_DOCKER=1 -p 8080:8080 -v $(current_dir):/workspace -w /workspace public.ecr.aws/dataminded/dbt:$(dbt_version)

supported_args=target models select
args = $(foreach a,$(supported_args),$(if $(value $a),--$a "$($a)"))

env:
	touch $(current_dir)/.env

shell: env
	eval "$(docker_dbt_command)"

deps:
	dbt deps --profiles-dir $(profiles_dir) --project-dir $(project_dir) $(call args,$@)

manifest:
	dbt compile --profiles-dir $(profiles_dir) --project-dir $(project_dir) $(call args,$@)
	cp $(project_dir)/target/manifest.json $(current_dir)/dags/manifest.json

debug:
	dbt debug --profiles-dir $(profiles_dir) --project-dir $(project_dir) $(call args,$@)

test:
	dbt test --profiles-dir $(profiles_dir) --project-dir $(project_dir) $(call args,$@)

run:
	dbt run --profiles-dir $(profiles_dir) --project-dir $(project_dir) $(call args,$@)

docs:
	dbt docs serve --profiles-dir $(profiles_dir) --project-dir $(project_dir) $(call args,$@)
