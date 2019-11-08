.PHONY: build
build:
	docker-compose build

.PHONY: start
start:
	docker-compose up -d --build

.PHONY: stop
stop:
	docker-compose down

.PHONY: logs
logs:
	docker-compose logs