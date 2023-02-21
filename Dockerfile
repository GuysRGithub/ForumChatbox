FROM python:3.7.8-stretch AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
    build-essential \
    curl \
    git \
    jq \
    libgomp1 \
    vim

WORKDIR /app

RUN python -m pip install --no-cache-dir --upgrade pip

RUN python -m pip install rasa==2.8.25 SQLAlchemy==1.3.22

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml
