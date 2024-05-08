# Use an official CUDA base image
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Install Python and system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Python dependencies from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]