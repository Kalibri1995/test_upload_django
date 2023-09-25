FROM python:3.10-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./file_upload_project /app/file_upload_project
ADD ./docker /app/docker

RUN chmod +x /app/docker/file_upload_project/server-entrypoint.sh
RUN chmod +x /app/docker/file_upload_project/worker-entrypoint.sh
