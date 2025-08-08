FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

RUN apt update 

RUN apt -y install postgresql-client python3 python3-pip

RUN pip3 install tavern

# Install Python development tools
RUN pip install --upgrade pip setuptools wheel