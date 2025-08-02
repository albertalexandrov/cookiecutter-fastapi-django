FROM python:3.12

ARG PROJECT_SLUG={{cookiecutter.project_slug}}

WORKDIR /${PROJECT_SLUG}

ENV PYTHONUNBUFFERED=1

COPY poetry.lock pyproject.toml ./
COPY src ./

RUN apt-get install -y --no-install-recommends gcc libc6-dev wget libpq-dev unzip \
&& apt-get clean \
&& pip install poetry==1.8.3

RUN poetry config virtualenvs.create false && poetry install \
&& useradd app \
&& chown -R app:app /${PROJECT_SLUG}

user app
