FROM python:3.7-slim

WORKDIR /app
RUN apt update && apt install -y git && rm -rf /var/lib/apt/lists/*

COPY src/requirements.txt src/requirements.txt
RUN pip install -r src/requirements.txt --no-cache-dir
COPY . .