APP_HOST=0.0.0.0
APP_PORT=8000
APP_PROJECT_NAME="Read-only API для онлайн-кинотеатра"
APP_DESCRIPTION="Информация о фильмах, жанрах и людях, участвовавших в создании произведения"
APP_LOG_LEVEL=debug
APP_ENTRYPOINT=main:app

REDIS__HOST=redis
REDIS__PORT=6379
REDIS__PASSWORD=redispass

ELASTIC__HOST=elastic
ELASTIC__PORT=9200