#!/bin/sh
set -e

uv run python manage.py migrate

uv run python manage.py collectstatic --noinput

exec uv run gunicorn SoftwareProject.wsgi:application --bind 0.0.0.0:8000