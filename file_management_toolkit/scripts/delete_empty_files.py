import os
import logging

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def delete_empty_files(source_dir):
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"El directorio fuente no existe: {source_dir}")

        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                    logging.info(f"Archivo vacío eliminado: {file_path}")

        print("Archivos vacíos eliminados.")
        logging.info("Proceso completado: Eliminación de archivos vacíos.")

    except Exception as e:
        logging.error(f"Error al eliminar archivos vacíos: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Error: Se requiere el directorio fuente.")
        sys.exit(1)

    source_directory = sys.argv[1]
    delete_empty_files(source_directory)
