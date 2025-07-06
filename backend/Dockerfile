# Dockerfile for the Backend Application (Python Flask)

# Use a Python base image. Python 3.9-slim-buster is a good balance
# between size and features for a Flask application.
FROM python:3.9-slim-buster

# Set the working directory inside the container
# All subsequent commands will be executed in this directory
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker's build cache.
# If requirements.txt doesn't change, this layer won't be rebuilt.
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
# --no-cache-dir prevents pip from storing cached wheels, reducing image size
# -r specifies to install from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
# This includes app.py and any other necessary Python files
COPY . .

# Expose port 5000, which is the default port our Flask application listens on
EXPOSE 5000

# Define the command to run the application when the container starts.
# 'flask run --host=0.0.0.0' makes the Flask app accessible from outside the container.
# We also specify the app module 'app.py' using FLASK_APP environment variable.
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
