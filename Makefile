SHELL := /bin/bash

.PHONY: run_virtualenv, deploy, migrate, run_server, prod_deploy

run_virtualenv:
	source myenv/bin/activate;

prod_deploy:
	git checkout master;
	git pull;
	git checkout Production;
	git merge master;
	python3 app/manage.py makemigrations;
	python3 app/manage.py migrate;
	python3 app/manage.py collectstatic

migrate:
	make run_virtualenv
	python3 app/manage.py makemigrations;
	python3 app/manage.py migrate;

run_server:
	make migrate
	python3 app/manage.py runserver
