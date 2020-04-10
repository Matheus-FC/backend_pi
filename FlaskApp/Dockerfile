FROM ubuntu:18.04

RUN apt-get update -y && \
		apt-get install -y python-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]