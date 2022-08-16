FROM python:3.10.2

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

RUN mkdir /app && chmod 777 /app
COPY cookiecutter.yml /app/cookiecutter.yml
ENV COOKIECUTTER_CONFIG=/app/cookiecutter.yml
WORKDIR /app
