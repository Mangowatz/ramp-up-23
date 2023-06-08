# Use the official Python base image
FROM python:3.10-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the code file and requirements file into the container
COPY publisher.py /app
COPY requirements.txt /app

# Install the dependencies
RUN pip install -r requirements.txt


# Specify the command to run when the container starts
CMD ["uvicorn", "publisher:app", "--host", "0.0.0.0", "--port", "80"]