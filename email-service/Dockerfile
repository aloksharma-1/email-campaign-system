FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

ENV SMTP_SERVER=smtp.gmail.com
ENV SMTP_PORT=587
ENV SENDER_EMAIL=your-email@gmail.com
ENV SENDER_PASSWORD=your-app-password

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
