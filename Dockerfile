# Use the official Python image as a parent image
FROM python:3.9.6

# Set environment variables to prevent buffering of output and ensure Python operates in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
