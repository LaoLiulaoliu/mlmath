FROM alpine:3.12.1

WORKDIR /app
ADD . /app

RUN apk update
RUN apk upgrade
RUN apk add --no-cache py3-pip
RUN apk add --no-cache gcc g++ libffi-dev python3-dev musl-dev

RUN pip3 install --upgrade pip
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip3 config set install.trusted-host mirrors.aliyun.com
RUN pip3 install jupyter
