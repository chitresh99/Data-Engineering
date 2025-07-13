# FROM: Use Python 3.11 slim as base image (smaller than full Python)
FROM python:3.11-slim

# WORKDIR: Set working directory inside container
WORKDIR /app

# COPY: Copy requirements first (Docker layer caching optimization)
COPY requirements.txt .

# RUN: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# COPY: Copy application code
COPY . .

# EXPOSE: Document that container listens on port 5000
EXPOSE 5000

# ENV: Set environment variable
ENV ENVIRONMENT=production

# CMD: Default command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]