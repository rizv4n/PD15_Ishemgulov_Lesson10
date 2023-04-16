FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY migrations migrations
ENV FLASK_APP=run.py


CMD flask run -h 0.0.0.0 -p 80