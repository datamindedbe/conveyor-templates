FROM python:3.11.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
COPY setup.py setup.py
# Put dependencies in it's own layer as a cache, if you change code only the code layer needs to be rebuild
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY src ./src
RUN python3 -m pip install . --no-cache-dir
ENTRYPOINT ["python3", "-m", "alerting.app"]
