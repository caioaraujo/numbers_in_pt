# Numbers in portuguese 
Given a number, describes it in portuguese.

## Requirements

- Python 3.6 (https://www.python.org/downloads/release/python-368/)
- PIP (https://pypi.org/project/pip/)

Optional:

- Docker (https://docs.docker.com/install/)
- Pipenv (https://github.com/pypa/pipenv)
- Make (https://www.gnu.org/software/make/)

## Installation

### Locally

You can install all dependencies and creating a virtualenv with pipenv by running:

`pipenv install`<br>
or<br>
`make pipenv-setup`

### Using Docker

You can build the image by running on project root:

`docker build --tag=numbers_in_pt .`<br>
or<br>
`make docker-build`

## Running 

### Local

`python manage.py runserver`<br>
or<br>
`make start`
