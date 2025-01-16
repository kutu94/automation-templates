import os

# Directorio raíz del proyecto (puedes usarlo para rutas globales)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Directorios por defecto
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Configuraciones genéricas (placeholders)
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_ENCODING = "utf-8"

# Ejemplo de variable para tokens o claves (aunque lo recomendado es usar .env para credenciales)
API_TOKEN = "placeholder_token"

"""
Nota: 
- No incluyas credenciales sensibles aquí; usa .env para eso.
- Puedes importar estos valores en tus scripts cuando necesites rutas o configuraciones.
  Ejemplo: 
    from project_config.settings import DATA_DIR, OUTPUT_DIR
"""
