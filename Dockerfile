FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /insta
WORKDIR /insta
COPY . /insta

ADD ./requirements.txt /insta

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input
