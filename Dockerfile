FROM python:3.11-alpine

# Metadatos
LABEL maintainer="Home Assistant Blueprints Validator"
LABEL description="Validador de YAML para blueprints de Home Assistant"

# Instalar dependencias del sistema
RUN apk add --no-cache \
    git \
    bash

# Crear directorio de trabajo
WORKDIR /app

# Copiar solo el validador y requirements
COPY validate_yaml.py /app/
COPY requirements.txt /app/

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Crear directorio para los blueprints
WORKDIR /blueprints

# Punto de entrada por defecto
ENTRYPOINT ["python", "/app/validate_yaml.py"]