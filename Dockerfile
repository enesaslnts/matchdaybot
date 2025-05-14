FROM python:3.10-slim

WORKDIR /app

COPY ./app /app

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "main.py"]
