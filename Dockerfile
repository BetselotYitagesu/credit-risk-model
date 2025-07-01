# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire project (src/, notebooks/, etc.)
COPY . .

# Set environment variable for MLflow (optional)
ENV MLFLOW_TRACKING_URI=http://mlflow:5000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
