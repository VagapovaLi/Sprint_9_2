FROM python:3.11-slim

# Установка дополнительных инструментов (по необходимости)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую папку внутри контейнера
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Запускаем тесты по умолчанию (можно изменить)
CMD ["pytest"]
