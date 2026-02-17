# FraudNet.AI Development Makefile

.PHONY: help install test lint format clean docker-build docker-up docker-down docker-logs reset-db migrate seed-data

# Default target
help:
	@echo "FraudNet.AI Development Commands"
	@echo "================================"
	@echo "install          Install dependencies"
	@echo "test             Run all tests"
	@echo "test-cov         Run tests with coverage"
	@echo "test-unit        Run unit tests only"
	@echo "test-integration Run integration tests only"
	@echo "lint             Run code linting"
	@echo "format           Format code with black"
	@echo "type-check       Run mypy type checking"
	@echo "clean            Clean up cache files"
	@echo ""
	@echo "Docker Commands:"
	@echo "docker-build     Build Docker images"
	@echo "docker-up        Start development environment"
	@echo "docker-down      Stop development environment"
	@echo "docker-logs      Show container logs"
	@echo "docker-shell     Open shell in app container"
	@echo ""
	@echo "Database Commands:"
	@echo "reset-db         Reset database (destructive)"
	@echo "migrate          Run database migrations"
	@echo "seed-data        Seed database with sample data"
	@echo ""
	@echo "Production Commands:"
	@echo "prod-build       Build production image"
	@echo "prod-up          Start production environment"
	@echo "prod-down        Stop production environment"

# Development setup
install:
	pip install -r requirements.txt
	pip install -e .

# Testing
test:
	python -m pytest tests/ -v

test-cov:
	python -m pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing

test-unit:
	python -m pytest tests/unit/ -v

test-integration:
	python -m pytest tests/integration/ -v

# Code quality
lint:
	flake8 app/ tests/
	black --check app/ tests/
	isort --check-only app/ tests/

format:
	black app/ tests/
	isort app/ tests/

type-check:
	mypy app/

# Cleanup
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/

# Docker development
docker-build:
	docker-compose -f docker-compose.dev.yml build

docker-up:
	docker-compose -f docker-compose.dev.yml up -d
	@echo "Waiting for services to be ready..."
	@sleep 10
	@echo "Services started. API available at http://localhost:5000"

docker-down:
	docker-compose -f docker-compose.dev.yml down

docker-logs:
	docker-compose -f docker-compose.dev.yml logs -f

docker-shell:
	docker-compose -f docker-compose.dev.yml exec app /bin/bash

# Database management
reset-db:
	docker-compose -f docker-compose.dev.yml exec mysql mysql -u root -prootpassword123 -e "DROP DATABASE IF EXISTS fraudnet; CREATE DATABASE fraudnet;"
	docker-compose -f docker-compose.dev.yml restart app

migrate:
	docker-compose -f docker-compose.dev.yml exec app python -c "from app.models.database import create_tables; create_tables()"

seed-data:
	docker-compose -f docker-compose.dev.yml exec app python scripts/seed_data.py

# Production
prod-build:
	docker-compose build

prod-up:
	docker-compose up -d

prod-down:
	docker-compose down

# Development server (without Docker)
run-dev:
	export FLASK_ENV=development && export FLASK_DEBUG=1 && flask run --host=0.0.0.0 --port=5000

# Training
train-model:
	docker-compose -f docker-compose.dev.yml exec app python -c "from app.training.model_trainer import ModelTrainer; trainer = ModelTrainer(); trainer.train_model()"

# Security scan
security-scan:
	docker run --rm -v "$(PWD):/src" aquasec/trivy fs /src

# Code analysis
analyze:
	radon cc app/ -a
	radon mi app/
	bandit -r app/

# Documentation
docs:
	@echo "Generating API documentation..."
	# Add documentation generation command here