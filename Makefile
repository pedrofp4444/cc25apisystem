# Project name/Docker image
IMAGE_NAME=cc25apisystem
PORT=47326

# Environment (default: no authentication)
AUTH_ON?=false

# Install dependencies
install:
	pip install -r requirements.txt

# Run locally with hot-reload
run:
	AUTH_ON=$(AUTH_ON) uvicorn main:app --reload --port $(PORT) --host 0.0.0.0

# Docker: Build image
build:
	docker build -t $(IMAGE_NAME) .

# Docker: Run container
docker-run:
	docker run -e AUTH_ON=$(AUTH_ON) -p $(PORT):$(PORT) $(IMAGE_NAME)

# Create new handler via scaffolding
scaffold:
	python3 scaffold.py

# Clean __pycache__
clean:
	find . | grep -E "__pycache__|\.pyc|\.pyo" | xargs rm -rf
