
# pull the official docker image
FROM python:3.10

# set work directory
WORKDIR /src

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update

# copy project
COPY . /src/
