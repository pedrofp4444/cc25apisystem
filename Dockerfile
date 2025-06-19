# Python base image
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 47326

CMD ["sh", "-c", "AUTH_ON=$AUTH_ON uvicorn main:app --host 0.0.0.0 --port ${PORT:-47326} --reload"]
