FROM python:3.9-slim AS app

RUN mkdir /app
WORKDIR /app

COPY ./app/requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./app /app
