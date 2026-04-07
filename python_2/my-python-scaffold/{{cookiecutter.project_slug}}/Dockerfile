# Use a slim version of Python to keep the image small
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY app.py .

# Inform the platform which port the app listens on
EXPOSE 8080

CMD ["python", "app.py"]
