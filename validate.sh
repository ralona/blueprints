#!/bin/bash

# Script rápido para validar archivos YAML
source venv/bin/activate 2>/dev/null || {
    echo "⚠️  Entorno virtual no encontrado. Ejecuta primero: ./setup.sh"
    exit 1
}

python validate_yaml.py "$@"