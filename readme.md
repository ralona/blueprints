# Home Assistant Custom Blueprints

Repositorio de blueprints personalizados para Home Assistant con validación automática de sintaxis YAML.

## Blueprints disponibles

### 1. Luz Adaptativa Inteligente Pro (Script)
**Archivo:** `adaptive_light_script.yml`  
**Con Preview:** `adaptive_light_script_with_preview.yml`

Script avanzado que controla luces con brillo y temperatura adaptados automáticamente según la hora del día.

#### Características principales:
- **4 períodos adaptativos**: Mañana, Día, Tarde y Noche
- **Modo Visitas**: Enciende luces sin ajustes automáticos
- **Modo Preview**: Simula el comportamiento a cualquier hora del día
- **Notificaciones**: Muestra información del estado actual (opcional)
- **Transiciones suaves**: Configurables de 0 a 30 segundos
- **Panel de control**: Tarjeta de dashboard incluida para testing

#### Configuración por períodos:
- **Mañana (6:00-8:59)**: Luz moderada fría-neutra para activación
- **Día (9:00-17:59)**: Máxima iluminación blanca para productividad
- **Tarde (18:00-21:59)**: Luz cálida relajante
- **Noche (22:00-5:59)**: Iluminación mínima muy cálida

#### Modo Preview (Vista Previa)

La versión con preview permite simular cómo se comportará la luz a diferentes horas:

1. **Habilitar Modo Preview**: Activa la simulación
2. **Seleccionar Hora**: Elige cualquier hora del día (0-23)
3. **Ver Notificaciones**: Muestra información detallada del estado
4. **Panel de Dashboard**: Usa `preview_dashboard_card.yaml` para control visual

**Archivos de soporte:**
- `preview_dashboard_card.yaml` - Tarjeta para el dashboard
- `preview_helpers.yaml` - Helpers para configuración avanzada

### 2. Brightness Only in ON Devices
**Archivo:** `brightness_only_in_on_devices.yml`

Blueprint para controlar el brillo solo en dispositivos encendidos.

## Instalación

1. Copia la URL del blueprint deseado
2. En Home Assistant, ve a Configuración > Automatizaciones y escenas > Blueprints
3. Haz clic en "Importar Blueprint"
4. Pega la URL del archivo `.yml`
5. Configura según tus necesidades

## Validación de Blueprints

Este repositorio incluye validación automática de sintaxis YAML para blueprints de Home Assistant.

### Opción 1: Usando Docker (Recomendado - No requiere Python)

```bash
# Validar todos los archivos YAML
./validate-docker.sh

# Validar archivos específicos
./validate-docker.sh adaptive_light_script.yml

# Usando docker-compose
docker-compose up
```

### Opción 2: Usando Python local

```bash
# Configurar entorno (solo la primera vez)
./setup.sh

# Validar archivos
./validate.sh
```

### Pre-commit Hook

El repositorio incluye hooks de pre-commit para validar automáticamente antes de cada commit:

```bash
# Con Python local
pre-commit install

# Con Docker (usa .pre-commit-config-docker.yaml)
pre-commit install -c .pre-commit-config-docker.yaml
```

## Requisitos

- **Opción Docker**: Solo Docker instalado
- **Opción Python**: Python 3.7+ con pip

## Estructura del Proyecto

```
blueprints/
├── *.yml                     # Blueprints de Home Assistant
├── validate_yaml.py          # Script de validación
├── validate-docker.sh        # Validador con Docker
├── validate.sh               # Validador con Python local
├── Dockerfile                # Imagen Docker del validador
├── docker-compose.yml        # Configuración Docker Compose
├── requirements.txt          # Dependencias Python
└── .pre-commit-config*.yaml  # Configuraciones pre-commit
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Valida tus blueprints antes de hacer commit
2. Abre un issue o pull request
3. Asegúrate de que todos los tests pasen
