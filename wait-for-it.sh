#!/bin/bash
until nc -z db 5432; do
    echo "Esperando a PostgreSQL..."
    sleep 2
done
python app.py