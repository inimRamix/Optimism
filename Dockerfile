FROM python:3.9-alpine3.16
WORKDIR /service
EXPOSE 8000
RUN apk add postgresql-client build-base postgresql-dev
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt
COPY service /service
RUN adduser --disabled-password service-user
USER service-user