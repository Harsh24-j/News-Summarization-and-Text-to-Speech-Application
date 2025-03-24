# Use Python 3.9 base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run FastAPI backend and Gradio frontend
CMD uvicorn api:app --host 0.0.0.0 --port 8000 & \
    sleep 5 && \
    python app.py