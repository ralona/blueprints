#!/bin/bash

# Script para validar blueprints usando Docker
# No requiere Python instalado localmente

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🐳 Validador de Blueprints con Docker"
echo "======================================"
echo ""

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker no está instalado${NC}"
    echo "Por favor, instala Docker desde: https://docs.docker.com/get-docker/"
    exit 1
fi

# Verificar si Docker está ejecutándose
if ! docker info &> /dev/null; then
    echo -e "${RED}❌ Docker no está ejecutándose${NC}"
    echo "Por favor, inicia Docker Desktop o el servicio Docker"
    exit 1
fi

# Construir la imagen si no existe o si el Dockerfile ha cambiado
echo "📦 Preparando contenedor de validación..."
docker build -t ha-blueprint-validator:latest . --quiet

# Ejecutar el validador
echo "🔍 Validando archivos YAML..."
echo ""

# Si se pasan argumentos, úsalos; si no, valida todos los archivos
if [ $# -eq 0 ]; then
    docker run --rm -v "$(pwd)":/blueprints:ro ha-blueprint-validator:latest
else
    docker run --rm -v "$(pwd)":/blueprints:ro ha-blueprint-validator:latest "$@"
fi

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo -e "\n${GREEN}✅ Validación completada exitosamente${NC}"
else
    echo -e "\n${RED}❌ Se encontraron errores en la validación${NC}"
fi

exit $exit_code