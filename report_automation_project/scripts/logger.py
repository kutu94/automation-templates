import logging
import os
import sys

# Agregar el directorio raíz del proyecto al PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from project_config.settings import OUTPUT_FOLDER

def setup_logger():
    os.makedirs(f"{OUTPUT_FOLDER}/logs", exist_ok=True)
    logging.basicConfig(
        filename=f"{OUTPUT_FOLDER}/logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Sistema de logs configurado")



