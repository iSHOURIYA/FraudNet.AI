# Multi-stage Docker build for FraudNet.AI

# Build stage
FROM python:3.11-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        pkg-config \
        default-libmysqlclient-dev \
        gcc \
        g++ \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Development stage
FROM builder as development

# Install development dependencies
RUN pip install flask[dotenv] ipdb

# Set development environment
ENV FLASK_ENV=development \
    FLASK_DEBUG=1

# Create non-root user for development
RUN groupadd -r fraudnet && useradd -r -g fraudnet fraudnet

# Create app directory
WORKDIR /app

# Create directories for artifacts and logs
RUN mkdir -p /app/artifacts/models /app/artifacts/metrics /app/artifacts/preprocessing /app/logs \
    && chown -R fraudnet:fraudnet /app

# Switch to non-root user
USER fraudnet

# Expose port
EXPOSE 5000

# Development command (Flask development server with hot reload)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]

# Production stage
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production \
    PATH="/opt/venv/bin:$PATH"

# Install runtime dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r fraudnet && useradd -r -g fraudnet fraudnet

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Create app directory
WORKDIR /app

# Copy application code
COPY --chown=fraudnet:fraudnet . .

# Create directories for artifacts and logs
RUN mkdir -p /app/artifacts/models /app/artifacts/metrics /app/artifacts/preprocessing /app/logs \
    && chown -R fraudnet:fraudnet /app

# Switch to non-root user
USER fraudnet

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:5000/api/v1/health/live || exit 1

# Default command
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "--preload", "run:app"]