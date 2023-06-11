
FROM python:3.9

LABEL maintainer="saha011p@gmail.com"

WORKDIR /code

COPY ./req.txt /code/req.txt
COPY ./src /code/src
COPY ./alembic.ini /code/alembic.ini
COPY ./migrations /code/migrations

RUN pip install --no-cache-dir --upgrade -r /code/req.txt