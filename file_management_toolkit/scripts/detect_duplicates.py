import os
import hashlib
import logging

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_hash(file_path):
    """Calcula el hash de un archivo para detectar duplicados."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def detect_duplicates(source_dir):
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"El directorio fuente no existe: {source_dir}")

        hash_dict = {}
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    file_hash = calculate_hash(file_path)
                    if file_hash in hash_dict:
                        logging.info(f"Archivo duplicado detectado: {file_path}")
                        print(f"Duplicado: {file_path}")
                    else:
                        hash_dict[file_hash] = file_path

        print("Detección de duplicados completada.")
        logging.info("Proceso completado: Detección de duplicados.")

    except Exception as e:
        logging.error(f"Error al detectar duplicados: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Error: Se requiere el directorio fuente.")
        sys.exit(1)

    source_directory = sys.argv[1]
    detect_duplicates(source_directory)
