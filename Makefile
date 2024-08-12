# Variables
APP_NAME = app.py  # Name of your main Flask application file
VENV = env_rs  # Name of your virtual environment directory

# Targets

# Initialize a virtual environment and install dependencies
.PHONY: setup
setup:
	@echo Creating virtual environment ...
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate && pip install -r requirements.txt

# Build the application
.PHONY: build-application
# Build the Docker image
build-application:
	@echo Building Docker image...
	docker build -t flask-app .

# Run the application
.PHONY: run-application
# Run the Docker container
run-application: build-application
	@echo Starting Application...
	docker run --rm -p 5000:5000 flask-app

# Clean up Docker images and containers
.PHONY: clean
clean:
	@echo Cleaning up...
	docker system prune -f