FROM python:3
RUN mkdir /to-do
WORKDIR /to-do
RUN pip install -r requirements.txt
COPY requirements.txt /to-do/
RUN pip install -r requirements.txt
COPY . /to-do/
