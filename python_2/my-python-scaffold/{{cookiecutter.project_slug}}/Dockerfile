FROM python:3.11-slim

# Metadata injection for the Platform Engineering catalog
LABEL maintainer="{{ cookiecutter.author_name }}"
LABEL service="{{ cookiecutter.project_slug }}"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Match the port defined in the scaffold configuration
EXPOSE {{ cookiecutter.app_port }}

CMD ["python", "app.py"]
