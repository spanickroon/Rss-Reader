FROM python:3.8

RUN mkdir /code

WORKDIR /code
ADD . /code
ENV PYTHONPATH "${PATHONPATH}:/rssreader"
