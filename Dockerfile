FROM python:3.11-alpine3.19

# Create a working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY code .

# Expose Flask app port (default is 5000)
EXPOSE 8080

# Execute the app directly
CMD ["python", "app.py"]
