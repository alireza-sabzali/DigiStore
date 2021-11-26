FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY . /app

ADD ./requirements.txt /app

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input
