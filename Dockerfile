# Указываем базовый образ
FROM python:3.9
# Указываем автора данного образа
LABEL maintainer="saha011p@gmail.com"
# Указываем директорию /code в качестве рабочей.
# Если такой директории нет, то она будет создана
WORKDIR /code
# Копируем основные файлы проекта в директорию /code
COPY ./req.txt /code/req.txt
COPY ./src /code/src
COPY ./alembic.ini /code/alembic.ini
COPY ./migrations /code/migrations
# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade -r /code/req.txt