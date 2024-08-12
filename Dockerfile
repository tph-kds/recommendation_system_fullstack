# Use an official Python runtime as a parent image
FROM python:3.9-slim

# (exec shell)
RUN echo "Welcome everyone 👋" 
# (exec form)
RUN ["echo", "Welcome everyone👋 "] 

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pip and update it
RUN apt update && \
    apt install -y --no-install-recommends \
    python3-pip && \
    pip install --upgrade pip && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
    
    
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
    
# Add metadata to the image
LABEL maintainer="tranphihung8383@example.com"
LABEL version="1.0"
LABEL description="This Docker image contains a Flask application."
# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Command to run the Flask app
ENTRYPOINT ["python", "app/app.py"]

# Add default arguments
CMD ["--host=0.0.0.0", "--port=5000"]