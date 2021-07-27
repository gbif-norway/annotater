FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
