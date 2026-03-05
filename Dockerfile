# Use Python 3.13 as base image
FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files first (better Docker cache)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy project
COPY . .

# Collect static files (for production)
RUN uv run python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start server
CMD sh -c "uv run python manage.py migrate && uv run gunicorn SoftwareProject.wsgi:application --bind 0.0.0.0:8000"