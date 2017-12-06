FROM ubuntu:16.04

RUN \
  apt-get update && \
  apt-get install -y build-essential lsb-release git \
                     python python-pip \
                     uwsgi uwsgi-plugin-python


RUN pip install --upgrade pip


RUN pip install mkdocs
RUN pip install markdown-include
RUN pip install bibtexparser
RUN pip install Jinja2


WORKDIR /workdir
