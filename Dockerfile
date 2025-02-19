# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script and other files into the container
COPY main.py .
COPY web_urls.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set up Git inside the container
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Configure Git (Make sure you set up authentication before running)
RUN git config --global user.name "Mubassim-Khan" && \
    git config --global user.email "mubassimkhan@gmail.com"

# Run the script in the background
CMD ["python", "main.py"]
