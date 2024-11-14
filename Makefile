DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
BROCKER_FILE = docker_compose/broker.yaml
APP_FILE = docker_compose/app.yaml
MANAGE_PY = python manage.py
APP_CONTAINER = admin-app


.PHONY: broker
broker:
	$(DC) -f $(BROCKER_FILE) up --build -d


.PHONY: app
app:
	$(DC) -f $(APP_FILE) up --build -d


.PHONY: all
all:
	broker app


.PHONY: broker-down
broker-down:
	$(DC) -f $(BROCKER_FILE) down


.PHONY: app-down
app-down:
	$(DC) -f $(APP_FILE) down


.PHONY: down
down:
	broker-down app-down

.PHONY: restart
restart: down all

