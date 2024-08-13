# Variables
VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
DOCKER_IMAGE := telegram-bot-image

# Targets
.PHONY: all install venv run test clean docker-build docker-run

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