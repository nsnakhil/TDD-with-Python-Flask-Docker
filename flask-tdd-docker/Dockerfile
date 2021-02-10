# pull official base image
FROM ubuntu::18.04

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add and install requirements
COPY flask-tdd-docker/requirements.txt requirements.txt 
RUN pip install -r requirements.txt

# add app
COPY . .

# run server
CMD ["gunicorn3", "-b", "0.0.0.0:8000", "app:app", "--workers=5"]
