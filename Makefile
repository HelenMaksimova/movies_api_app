.PHONY: clean create_network up_app up_tests run_app_local run_tests_local help

NETWORK_NAME ?= movies_net
CLEAN ?= false
CLEAN_TARGET ?= app

SHELL := /bin/bash

clean:
	@echo "✅ Выполняем очистку (цель: $(CLEAN_TARGET))..."
	@if [ "$(CLEAN_TARGET)" = "tests" ]; then \
		docker compose -f .docker/docker-compose.tests.yml down; \
	else \
		docker compose -f .docker/docker-compose.yml down; \
	fi
	@echo "✅ Готово!"

create_network:
	@docker network inspect $(NETWORK_NAME) >/dev/null 2>&1 || docker network create $(NETWORK_NAME)

up_app:
	@if [ "$(CLEAN)" = "true" ]; then \
		$(MAKE) clean CLEAN_TARGET=app; \
	fi
	@$(MAKE) create_network
	@docker compose -f .docker/docker-compose.yml up -d

up_tests:
	@if [ "$(CLEAN)" = "true" ]; then \
		$(MAKE) clean CLEAN_TARGET=tests; \
	fi
	@$(MAKE) create_network
	@docker compose -f .docker/docker-compose.tests.yml up -d

run_app_local:
	@cd app && python main.py

run_tests_local:
	@docker compose -f .docker/docker-compose.test_app.yml up -d
	@cd tests/functional && pytest -sv

help:
	@echo "*********************************************************************"
	@echo "  Управление окружением"
	@echo "*********************************************************************"
	@echo ""
	@echo "  make create_network"
	@echo "      Создаёт внешнюю Docker-сеть $(NETWORK_NAME), если её ещё нет."
	@echo ""
	@echo "  make up_app [CLEAN=true]"
	@echo "      Поднимает приложение в Docker (.docker/docker-compose.yml)."
	@echo "      CLEAN=true  — перед запуском выполняет make clean CLEAN_TARGET=app."
	@echo ""
	@echo "  make up_tests [CLEAN=true]"
	@echo "      Поднимает тестовое окружение в Docker (.docker/docker-compose.tests.yml)."
	@echo "      CLEAN=true  — перед запуском выполняет make clean CLEAN_TARGET=tests."
	@echo ""
	@echo "  make run_app_local"
	@echo "      Запускает приложение локально (cd app && python main.py), без Docker."
	@echo ""
	@echo "  make run_tests_local"
	@echo "      Поднимает test_app в Docker и запускает pytest в tests/functional."
	@echo ""
	@echo "  make clean [CLEAN_TARGET=app|tests]"
	@echo "      Останавливает и удаляет контейнеры выбранной цели."
	@echo "      CLEAN_TARGET=app    (по умолчанию) — .docker/docker-compose.yml"
	@echo "      CLEAN_TARGET=tests  — .docker/docker-compose.tests.yml"
	@echo ""
	@echo "  make help"
	@echo "      Показывает эту справку."
	@echo ""
	@echo "*********************************************************************"