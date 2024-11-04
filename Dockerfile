# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire app directory (including data and analysis script) into the container
COPY app/ .

# Create an output directory to store results
RUN mkdir -p output

# Run the analysis script
CMD ["python", "analysis.py"]
