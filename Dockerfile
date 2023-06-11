FROM python:3.9

# Указываем базовый образ
FROM python:3.10
# Указываем автора данного образа
LABEL maintainer="saha011p@gmail.com"

WORKDIR /code

COPY ./req.txt /code/req.txt
COPY ./src /code/src
COPY ./alembic.ini /code/alembic.ini
COPY ./migrations /code/migrations

RUN pip install --no-cache-dir --upgrade -r /code/req.txt