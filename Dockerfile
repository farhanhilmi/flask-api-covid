FROM python:3.9.7
ADD . /flask-api-covid
WORKDIR /flask-api-covid
RUN pip install -r requirements.txt