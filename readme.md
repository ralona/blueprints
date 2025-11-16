# Home Assistant Custom Blueprints

Repositorio de blueprints personalizados para Home Assistant.

## Blueprints disponibles

### 1. Luz Adaptativa Inteligente Pro (Script)
**Archivo:** `adaptive_light_script.yml`

Script avanzado que controla luces con brillo y temperatura adaptados automáticamente según la hora del día.

#### Características principales:
- **4 períodos adaptativos**: Mañana, Día, Tarde y Noche
- **Modo Visitas**: Enciende luces sin ajustes automáticos
- **Detección de capacidades**: Se adapta a luces RGB o temperatura de color
- **Control manual inteligente**: Respeta cambios manuales recientes
- **Transiciones suaves**: Configurables de 0 a 30 segundos
- **Registro de eventos**: Para depuración opcional
- **Ajuste adaptativo**: Transiciones más naturales basadas en el estado actual

#### Configuración por períodos:
- **Mañana (6:00-8:59)**: Luz moderada fría-neutra para activación
- **Día (9:00-17:59)**: Máxima iluminación blanca para productividad
- **Tarde (18:00-21:59)**: Luz cálida relajante
- **Noche (22:00-5:59)**: Iluminación mínima muy cálida

### 2. Brightness Only in ON Devices
**Archivo:** `brightness_only_in_on_devices.yml`

Blueprint para controlar el brillo solo en dispositivos encendidos.

## Instalación

1. Copia la URL del blueprint deseado
2. En Home Assistant, ve a Configuración > Automatizaciones y escenas > Blueprints
3. Haz clic en "Importar Blueprint"
4. Pega la URL del archivo `.yml`
5. Configura según tus necesidades

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request.
