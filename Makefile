.PHONY: install format lint fix clean

# Default target
all: install format lint

# Install dependencies
install:
	pip install -r requirements.txt
	pip install black flake8 autopep8

# Format code with Black
format:
	black .

# Lint code with Flake8
lint:
	flake8 .

# Fix code with Autopep8
fix:
	autopep8 --in-place --aggressive --aggressive --recursive .

# Clean up Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +

# Run all code quality tools
quality: format lint

# Help command
help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make format   - Format code with Black"
	@echo "  make lint     - Lint code with Flake8"
	@echo "  make fix      - Fix code with Autopep8"
	@echo "  make clean    - Clean up Python cache files"
	@echo "  make quality  - Run all code quality tools"
	@echo "  make help     - Show this help message" 