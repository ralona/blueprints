# 🔍 Guía de Uso - Preview en Configuración

## Cómo usar el modo Preview/Test

El blueprint `adaptive_light_with_config_preview.yml` incluye un sistema de preview integrado directamente en la configuración que te permite probar cómo se comportará la luz a diferentes horas **sin salir de la pantalla de configuración**.

### 📋 Pasos para usar el Preview:

1. **Importa el blueprint** en Home Assistant
2. **Crea un nuevo script** basado en este blueprint
3. En la configuración verás la sección **"🔍 PREVIEW / TEST"**

### 🧪 Para probar una hora específica:

1. **Activa** el switch "🧪 Activar Modo Test"
2. **Selecciona** la hora que quieres simular en el dropdown "🕐 Hora de Test"
   - Cada opción muestra el período al que pertenece (🌅🌙☀️🌆)
3. **Guarda** el script
4. **Ejecuta** el script para ver el resultado
5. La luz se configurará como si fuera esa hora

### 💡 Características visuales en la configuración:

- **Separadores visuales**: Cada sección está claramente separada con líneas
- **Emojis indicativos**: Cada período tiene su emoji característico
- **Descripciones detalladas**: Tips y recomendaciones en cada campo
- **Dropdown con preview**: El selector de hora muestra qué período corresponde a cada hora
- **Notificaciones opcionales**: Activa para ver exactamente qué se está aplicando

### 📊 Tabla de referencia rápida:

| Hora | Período | Emoji | Config Recomendada |
|------|---------|-------|-------------------|
| 6:00-8:59 | Mañana | 🌅 | 75% brillo, 4500K |
| 9:00-17:59 | Día | ☀️ | 100% brillo, 5500K |
| 18:00-21:59 | Tarde | 🌆 | 60% brillo, 3000K |
| 22:00-5:59 | Noche | 🌙 | 20% brillo, 2200K |

### ⚠️ Importante:

- **Desactiva el Modo Test** después de probar para que el script funcione normalmente
- El Modo Test **sobrescribe** la hora actual mientras esté activo
- Las notificaciones te ayudan a confirmar que los valores se están aplicando correctamente

### 🎯 Workflow recomendado:

1. Configura los valores de brillo y temperatura para cada período
2. Usa el Modo Test para probar cada período (mañana, día, tarde, noche)
3. Ajusta los valores según lo que veas
4. Desactiva el Modo Test
5. ¡Listo! Tu luz se adaptará automáticamente durante el día

### 🔧 Troubleshooting:

- **La luz no responde**: Verifica que la entidad de luz sea correcta
- **No cambia la temperatura**: Algunas luces no soportan temperatura de color
- **Test no funciona**: Asegúrate de que el Modo Test esté activado
- **Valores no se aplican**: Revisa las notificaciones para ver qué está pasando