# Dockerfile
FROM python:3.10.9

COPY collector1.py /app/collector1.py

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "collector1.py"]