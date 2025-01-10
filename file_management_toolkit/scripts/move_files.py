import os
import shutil
import logging
import sys

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def move_files(source_dir, target_dir, pattern=None):
    """
    Mueve archivos de un directorio fuente a un directorio destino.

    Args:
        source_dir (str): Directorio fuente.
        target_dir (str): Directorio destino.
        pattern (str, opcional): Patrón para filtrar archivos (e.g., "factura").
    """
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"El directorio fuente no existe: {source_dir}")

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        moved_files = 0

        for file_name in os.listdir(source_dir):
            file_path = os.path.join(source_dir, file_name)

            if os.path.isfile(file_path):
                # Filtrar archivos según el patrón, si se proporciona
                if pattern and pattern not in file_name:
                    continue

                # Mover archivo
                shutil.move(file_path, os.path.join(target_dir, file_name))
                logging.info(f"Movido: {file_name} → {target_dir}")
                print(f"Movido: {file_name} → {target_dir}")
                moved_files += 1

        if moved_files == 0:
            print("No se encontraron archivos para mover.")
        else:
            print(f"{moved_files} archivos movidos.")
        logging.info(f"Proceso completado: {moved_files} archivos movidos.")

    except Exception as e:
        logging.error(f"Error al mover archivos: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Se requieren los directorios fuente y destino.")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2]
    move_files(source_directory, target_directory)
