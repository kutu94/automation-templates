import os
import shutil
import logging
from datetime import datetime

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

import os
import sys


def organize_by_date(source_dir, target_dir, use_creation_date=True):
    """
    Organiza archivos por fecha de creación o modificación.

    Args:
        source_dir (str): Directorio fuente donde están los archivos.
        target_dir (str): Directorio destino donde se organizarán los archivos.
        use_creation_date (bool): Usar la fecha de creación en lugar de modificación.
    """
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"El directorio fuente no existe: {source_dir}")

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        for file_name in os.listdir(source_dir):
            file_path = os.path.join(source_dir, file_name)

            if os.path.isfile(file_path):
                # Obtener fecha de creación o modificación
                if use_creation_date:
                    file_time = os.path.getctime(file_path)
                else:
                    file_time = os.path.getmtime(file_path)

                # Convertir la fecha en formato Año/Mes
                date_folder = datetime.fromtimestamp(file_time).strftime("%Y/%m")
                dest_folder = os.path.join(target_dir, date_folder)
                os.makedirs(dest_folder, exist_ok=True)

                # Mover archivo
                shutil.move(file_path, os.path.join(dest_folder, file_name))
                logging.info(f"Movido: {file_name} → {dest_folder}")

        print("Archivos organizados por fecha.")
        logging.info("Proceso completado: Organización por fecha.")

    except Exception as e:
        logging.error(f"Error al organizar archivos por fecha: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Se requieren los directorios fuente y destino.")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2]
    organize_by_date(source_directory, target_directory)
