FROM python:3.10-slim

WORKDIR /app

COPY ./app /app

# Trivy installieren
RUN apt-get update && apt-get install -y wget curl unzip \
    && wget -O trivy.deb https://github.com/aquasecurity/trivy/releases/download/v0.50.0/trivy_0.50.0_Linux-64bit.deb \
    && apt-get install -y ./trivy.deb \
    && rm trivy.deb




ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "main.py"]
