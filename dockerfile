# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (excluding via .dockerignore)
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Set Streamlit to run the correct file
CMD ["streamlit", "run", "streamlit.py", "--server.enableCORS=false", "--server.enableXsrfProtection=false", "--server.port=8501"]
