#!/bin/bash

set -e

echo "Container starting up..."

# Health check - ensure database is reachable
echo "Checking database connection..."
python manage.py check --database default

# Collect static files (safe to run multiple times)
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Django server..."
# TODO change to run on supervisord when have celery service
exec gunicorn config.wsgi:application --workers 3 --bind 0.0.0.0:8000
