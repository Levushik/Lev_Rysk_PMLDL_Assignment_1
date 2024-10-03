# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI app directory into the container
COPY . /app

# Copy the models folder into the container
COPY models /app/models

# Install the required Python packages, including scikit-learn
RUN pip install fastapi uvicorn joblib catboost numpy pydantic scikit-learn

# Expose port 8000 for the FastAPI service
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
