# cybercare_project

Project for Cybercare recruitment process.
Task description can be found in Task.md file. Link -> [task description](./Task.md#task-description)

## Requirements:
to run this project you need to have installed:
- python 3.9 or higher
- poetry (dependency manager) https://python-poetry.org/docs/#installation 
- make (optional) https://www.gnu.org/software/make/
- docker (optional) https://docs.docker.com/get-docker/
- docker-compose (optional) https://docs.docker.com/compose/install/

## Installation:
- clone (or download and unpack) this repository
- install dependencies with poetry (see below)
- run make install or directly run `poetry install` in the root directory of the project

## How to run:
First make sure the consumer server is running (see 1st below) and then pass the data 
from the propagator service by running Event propagator (see 2nd below).

### Event consumer:
- make consumer_service or directly run `poetry run python -m consumer_service` in the root 
  directory of the project

This will start the server on the configured host. This command exposes the web 
application on port 8000, mounts current directory and enables autoreload. You can find swagger documentation at `/api/docs`.

### Event propagator:
- make propagator_service or directly run `poetry run python -m propagator_service` in the root directory of the project


## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Project structure
To generate: 
- project structure run: `tree "service_consumer"`
- project structure run: `tree "service_propagator"`

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

example env file:
```
CYBERCARE_PROJECT_RELOAD=True
OUTPUT_FILE_NAME=output.json
OUTPUT_FILE_DIR=file_storage
INPUT_FILE_NAME=input.json
INPUT_FILE_DIR=file_storage
EVENT_ENDPOINT=EVENT
PERIOD_SECONDS=3
```

to propagate env variables execute:
```bash
set -a
. ./.env
set +a
```

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possibe bugs);


You can read more about pre-commit here: https://pre-commit.com/


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . run --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml --project-directory . down
```

For running tests on your local machine.


2. Run the pytest.
```bash
pytest -vv .
```
