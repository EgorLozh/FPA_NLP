FROM python:3.10-slim

RUN apt-get update && apt-get install -y tree

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python start.py

ENV PYTHONUNBUFFERED=1
