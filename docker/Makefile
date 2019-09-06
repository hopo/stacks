.PHONY: all help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'



run-local-db:  # Run Mysql for local environment
	docker-compose up -d

stop-local-db:  # Stop Mysql for local environment
	docker-compose down


local-migrate:
	DJANGO_SETTINGS_MODULE='mushroom.settings_local' python3 manage.py migrate

local-make-migrate:
	DJANGO_SETTINGS_MODULE='mushroom.settings_local' python3 manage.py makemigrations

local: # Run local server
	DJANGO_SETTINGS_MODULE='mushroom.settings_local' python3 manage.py runserver
