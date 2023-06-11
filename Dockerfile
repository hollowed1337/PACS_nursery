<<<<<<< HEAD

FROM python:3.9

=======
# Указываем базовый образ
FROM python:3.10
# Указываем автора данного образа
>>>>>>> f6b5e4a9b83935218a8edc1c24179bdb761793e8
LABEL maintainer="saha011p@gmail.com"

WORKDIR /code

COPY ./req.txt /code/req.txt
COPY ./src /code/src
COPY ./alembic.ini /code/alembic.ini
COPY ./migrations /code/migrations
<<<<<<< HEAD

RUN pip install --no-cache-dir --upgrade -r /code/req.txt
=======
# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade -r /code/req.txt
>>>>>>> f6b5e4a9b83935218a8edc1c24179bdb761793e8
