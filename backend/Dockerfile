# Dockerfile

# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for Python and Django
ENV PYTHONUNBUFFERED=1
ENV DJANGO_ENV=production

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY . .


# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
