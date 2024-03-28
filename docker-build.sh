#!/bin/bash

# Проверяем, передан ли аргумент TAG
if [ -z "$1" ]; then
    echo "Usage: $0 TAG (e.g. 1.2.3)"
    exit 1
fi

# Проверяем формат TAG
if [[ ! $1 =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Invalid TAG format. Please use X.X.X format (e.g. 1.2.3)"
    exit 1
fi

# Сохраняем TAG в переменную
TAG=$1

# Собираем backend образ
docker build -f dockerfiles/backend/Dockerfile --tag task-tracker-kanban:$TAG --platform linux/amd64 .

# Собираем frontend образ
docker build -f dockerfiles/frontend/Dockerfile --tag task-tracker-kanban:$TAG --platform linux/amd64 .
