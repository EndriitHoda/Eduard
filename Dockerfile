# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Run the app with gunicorn (production-ready)
CMD exec gunicorn -b 0.0.0.0:${PORT:-5000} app:app