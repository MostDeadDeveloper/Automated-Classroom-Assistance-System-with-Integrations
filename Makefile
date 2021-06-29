SHELL := /bin/bash

.PHONY: run_virtualenv, deploy, migrate, run_server

run_virtualenv:
	source myenv/bin/activate;


migrate:
	make run_virtualenv
	python3 app/manage.py makemigrations;
	python3 app/manage.py migrate;

run_server:
	make migrate
	python3 app/manage.py runserver
