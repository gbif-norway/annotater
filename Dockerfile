FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /srv/annotater
WORKDIR /srv
COPY . /srv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
