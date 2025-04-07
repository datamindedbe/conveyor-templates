# Ref: https://github.com/jmarch/sqlmesh/blob/add-docker-support/Dockerfile
# https://github.com/TobikoData/sqlmesh/issues/1218
FROM python:3.11-slim
# Set working directory
WORKDIR /app

# Install system dependencie
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt requirements.txt

# Install Python dependencies
# RUN pip install -r requirements.txt --no-cache-dir

# Copy project files
COPY . .

# Set envirionment variable
ENV SQLMESH_PROJECT_DIR="/app"