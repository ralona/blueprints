#!/bin/bash

echo "🔧 Configurando el validador de YAML para blueprints de Home Assistant..."

# Verificar si Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado. Por favor instálalo primero."
    exit 1
fi

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual e instalar dependencias
echo "📚 Instalando dependencias..."
source venv/bin/activate
pip install --quiet --upgrade pip
pip install --quiet pyyaml pre-commit

# Instalar pre-commit hooks
if [ -f ".pre-commit-config.yaml" ]; then
    echo "🪝 Instalando pre-commit hooks..."
    pre-commit install
    echo "✅ Pre-commit hooks instalados correctamente"
fi

echo ""
echo "✨ ¡Configuración completa!"
echo ""
echo "Para validar manualmente los archivos YAML, ejecuta:"
echo "  source venv/bin/activate && python validate_yaml.py"
echo ""
echo "O simplemente:"
echo "  ./validate.sh"