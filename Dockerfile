FROM python:3.8

RUN mkdir /code

WORKDIR /code
ADD . /code
ADD requirements.txt code/requirements.txt

RUN pip install .
ENV PYTHONPATH "${PATHONPATH}:/."
