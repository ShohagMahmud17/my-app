# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Set the default command to run the app
CMD ["python", "run.py"]
