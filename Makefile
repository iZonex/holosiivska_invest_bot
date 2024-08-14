# Variables
VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
DOCKER_IMAGE := telegram-bot-image
SERVICE_NAME := telegram-bot
SERVICE_SCRIPT := setup_telegram_bot_service.sh

# Targets
.PHONY: all install venv run test clean docker-build docker-run setup-service

# Default target: Set up the virtual environment and install dependencies
all: install

# Create a virtual environment
venv:
	python3 -m venv $(VENV)

# Install dependencies
install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run the bot
run:
	$(PYTHON) lambda_function.py

# Run tests
test:
	$(PYTHON) -m pytest -v

# Clean up the environment
clean:
	rm -rf $(VENV)
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf .pytest_cache

# Build the Docker image
docker-build:
	docker build -t $(DOCKER_IMAGE) .

# Run the Docker container
docker-run:
	docker run -d --name telegram-bot-container $(DOCKER_IMAGE)

# Setup the bot as a systemd service
setup-service:
	@if [ -z "$(TELEGRAM_TOKEN)" ]; then \
		echo "Error: TELEGRAM_TOKEN is not set. Please provide it as an argument:"; \
		echo "make setup-service TELEGRAM_TOKEN=your_telegram_token"; \
		exit 1; \
	fi
	./$(SERVICE_SCRIPT) $(TELEGRAM_TOKEN)