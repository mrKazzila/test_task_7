# ===== Base variables =====
PROJECT_NAME = kazakov-test_task
DC = docker-compose

APP_DC_FILE = docker-compose.yaml
APP_ENV_FILE = env/.env

# ===== App services  =====
docker_up:
	@echo "Run the project..."
	${DC} --env-file ${APP_ENV_FILE} -p ${PROJECT_NAME} -f ${APP_DC_FILE} up -d --build

docker_down:
	@echo "Stopping project containers..."
	${DC} --env-file ${APP_ENV_FILE} -p ${PROJECT_NAME} -f ${APP_DC_FILE} down
