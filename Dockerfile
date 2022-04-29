# syntax=docker/dockerfile:1
FROM python:3.9.1
WORKDIR /usr/src/app
RUN ["apt-get", "update"]
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
