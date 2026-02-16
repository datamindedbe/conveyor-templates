env:
	python -m venv .venv
	source .venv/bin/activate

install:
	pip install sqlmesh

show: # Display the full model
	sqlmesh fetchdf "select * from sqlmesh_example.full_model"

init: # Initialize the SQLMesh project in duckdb?
	sqlmesh init duckdb

deploy_dev:
	sqlmesh plan dev 

deploy:
	sqlmesh plan

test:
	sqlmesh test
