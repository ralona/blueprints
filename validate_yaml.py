#!/usr/bin/env python3
"""
Validador de archivos YAML para blueprints de Home Assistant
Verifica la sintaxis y estructura antes de hacer commit
"""

import sys
import yaml
import os
from pathlib import Path
from typing import List, Tuple

# Definir constructor para tags de Home Assistant
class HomeAssistantYAML(yaml.SafeLoader):
    pass

def input_constructor(loader, node):
    """Constructor para el tag !input de Home Assistant"""
    return loader.construct_scalar(node)

def secret_constructor(loader, node):
    """Constructor para el tag !secret de Home Assistant"""
    return loader.construct_scalar(node)

def include_constructor(loader, node):
    """Constructor para el tag !include de Home Assistant"""
    return loader.construct_scalar(node)

# Registrar los constructores para tags de Home Assistant
HomeAssistantYAML.add_constructor('!input', input_constructor)
HomeAssistantYAML.add_constructor('!secret', secret_constructor)
HomeAssistantYAML.add_constructor('!include', include_constructor)
HomeAssistantYAML.add_constructor('!include_dir_list', include_constructor)
HomeAssistantYAML.add_constructor('!include_dir_merge_list', include_constructor)
HomeAssistantYAML.add_constructor('!include_dir_merge_named', include_constructor)

def validate_yaml_file(file_path: Path) -> Tuple[bool, str]:
    """
    Valida un archivo YAML y retorna si es válido junto con mensajes de error
    
    Args:
        file_path: Ruta al archivo YAML
        
    Returns:
        Tupla (is_valid, error_message)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Intenta cargar el YAML con soporte para tags de Home Assistant
        yaml.load(content, Loader=HomeAssistantYAML)
        
        # Validación específica para blueprints de Home Assistant
        if file_path.suffix == '.yml' or file_path.suffix == '.yaml':
            data = yaml.load(content, Loader=HomeAssistantYAML)
            
            # Verificar estructura básica de blueprint
            if 'blueprint' in data:
                blueprint = data['blueprint']
                
                # Verificar campos requeridos
                required_fields = ['name', 'domain']
                for field in required_fields:
                    if field not in blueprint:
                        return False, f"Campo requerido '{field}' faltante en blueprint"
                
                # Verificar dominio válido
                valid_domains = ['automation', 'script']
                if blueprint['domain'] not in valid_domains:
                    return False, f"Dominio inválido: {blueprint['domain']}. Debe ser uno de: {valid_domains}"
                
                # Verificar estructura de sequence si existe
                if 'sequence' in data:
                    if not isinstance(data['sequence'], list):
                        return False, "El campo 'sequence' debe ser una lista"
                    
                    # Verificar estructura de choose
                    for item in data['sequence']:
                        if isinstance(item, dict) and 'choose' in item:
                            if not isinstance(item['choose'], list):
                                return False, "'choose' debe ser una lista"
                            
                            # Verificar que cada opción tenga conditions y sequence
                            for idx, choice in enumerate(item['choose']):
                                if not isinstance(choice, dict):
                                    return False, f"Opción {idx} en 'choose' debe ser un diccionario"
                                if 'conditions' not in choice:
                                    return False, f"Opción {idx} en 'choose' debe tener 'conditions'"
                                if 'sequence' not in choice:
                                    return False, f"Opción {idx} en 'choose' debe tener 'sequence'"
        
        return True, "✓ Archivo YAML válido"
        
    except yaml.YAMLError as e:
        # Extraer información útil del error
        if hasattr(e, 'problem_mark'):
            mark = e.problem_mark
            return False, f"Error de sintaxis YAML en línea {mark.line + 1}, columna {mark.column + 1}: {e.problem}"
        else:
            return False, f"Error de sintaxis YAML: {str(e)}"
    except FileNotFoundError:
        return False, f"Archivo no encontrado: {file_path}"
    except Exception as e:
        return False, f"Error inesperado: {str(e)}"

def find_yaml_files(directory: Path = None) -> List[Path]:
    """
    Encuentra todos los archivos YAML en el directorio
    
    Args:
        directory: Directorio a buscar (por defecto, directorio actual)
        
    Returns:
        Lista de rutas a archivos YAML
    """
    if directory is None:
        directory = Path.cwd()
    
    yaml_files = []
    for ext in ['*.yml', '*.yaml']:
        yaml_files.extend(directory.glob(ext))
    
    return yaml_files

def main():
    """Función principal"""
    print("🔍 Validando archivos YAML para blueprints de Home Assistant...\n")
    
    # Si se proporcionan archivos específicos como argumentos
    if len(sys.argv) > 1:
        files_to_check = [Path(f) for f in sys.argv[1:] if f.endswith(('.yml', '.yaml'))]
    else:
        # Buscar todos los archivos YAML en el directorio actual
        files_to_check = find_yaml_files()
    
    if not files_to_check:
        print("⚠️  No se encontraron archivos YAML para validar")
        return 0
    
    all_valid = True
    results = []
    
    for file_path in files_to_check:
        is_valid, message = validate_yaml_file(file_path)
        results.append((file_path, is_valid, message))
        
        if not is_valid:
            all_valid = False
    
    # Mostrar resultados
    print("=" * 60)
    for file_path, is_valid, message in results:
        status = "✅" if is_valid else "❌"
        print(f"{status} {file_path.name}")
        print(f"   {message}")
        print()
    
    print("=" * 60)
    
    if all_valid:
        print("✅ Todos los archivos YAML son válidos")
        return 0
    else:
        print("❌ Se encontraron errores en algunos archivos")
        print("\n💡 Sugerencias para corregir errores comunes:")
        print("   - Verifica la indentación (usa espacios, no tabs)")
        print("   - Asegúrate de que las listas empiecen con '-'")
        print("   - Revisa que todos los 'choose' tengan 'conditions' y 'sequence'")
        print("   - Los valores 'default' en 'choose' van al mismo nivel que las opciones")
        return 1

if __name__ == "__main__":
    sys.exit(main())