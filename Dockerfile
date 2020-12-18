FROM alpine:3.12.3

WORKDIR /app
ADD . /app

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk update
RUN apk upgrade
RUN apk add --no-cache gcc g++ libffi-dev python3-dev musl-dev
RUN apk add --no-cache py3-pip

RUN pip3 install --upgrade pip
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip3 config set install.trusted-host mirrors.aliyun.com
RUN pip3 install pyzmq==19.0.2
RUN pip3 install jupyter
