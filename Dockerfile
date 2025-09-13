FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем всё внутрь контейнера
COPY . .

CMD ["python", "server/server.py"]