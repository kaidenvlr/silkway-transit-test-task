.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start:	## Start project with compose
	docker-compose build
	docker-compose up

.PHONY: force-start
force-start:	## Run project with setted Postgres on local machine
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py create_superuser
	python3 manage.py runserver 8000
