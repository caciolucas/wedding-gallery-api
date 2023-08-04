#!/bin/sh

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
gunicorn --bind 0.0.0.0:8000 --workers 3 --log-level INFO wedding_gallery.wsgi:application