import logging
import os

# Crear carpeta de logs
log_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configuración de logs
logging.basicConfig(
    filename=os.path.join(log_dir, "file_management.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
