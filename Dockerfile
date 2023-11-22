FROM python:slim-bookworm

WORKDIR /app

COPY . /app/

RUN pip install poetry && poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /app

