FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y build-essential libssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y build-essential libssl-dev && apt-get clean

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
