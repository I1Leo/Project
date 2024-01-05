FROM python:3.10

ARG BRANCH_NAME

WORKDIR /usr/src/app

RUN git clone https://github.com/I1Leo/Project /usr/src/app
RUN git checkout ?BRANCH_NAME

WORKDIR /usr/src/app/src

RUN cp example.env .env

RUN pip install -r requirements.txt --no-cache-dir             

WORKDIR /usr/src/app/src/backend

EXPOSE 8000