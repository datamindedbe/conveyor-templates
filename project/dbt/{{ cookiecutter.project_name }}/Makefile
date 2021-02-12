current_dir:=$(shell pwd)
project_dir:=$(current_dir)/dbt/{{ cookiecutter.project_name }}
profiles_dir:=$(current_dir)/dbt

debug:
	dbt debug --profiles-dir $(profiles_dir) --project-dir $(project_dir)

test:
	dbt test --profiles-dir $(profiles_dir) --project-dir $(project_dir)

run:
	dbt run --profiles-dir $(profiles_dir) --project-dir $(project_dir)

docs:
	dbt docs serve --profiles-dir $(profiles_dir) --project-dir $(project_dir)
