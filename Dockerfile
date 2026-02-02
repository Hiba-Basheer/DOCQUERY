# Dockerfile for DOCQUERY
FROM python:3.11-slim

WORKDIR /app

# copying requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copying application
COPY app/ ./app/

EXPOSE 8000

# running server on '0.0.0.0' so container is accessible outside
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]