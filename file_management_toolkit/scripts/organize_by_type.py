import sys
import os
import shutil
import logging

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def organize_by_type(source_dir, target_dir):
    """
    Clasifica archivos por tipo (extensión) y los mueve a subcarpetas en el directorio de destino.
    """
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"El directorio fuente no existe: {source_dir}")

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        file_types = {
            "images": [".jpg", ".jpeg", ".png", ".gif"],
            "documents": [".pdf", ".docx", ".txt", ".xlsx"],
            "others": []
        }

        for file_name in os.listdir(source_dir):
            file_path = os.path.join(source_dir, file_name)

            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file_name)
                ext = ext.lower()

                folder = "others"
                for category, extensions in file_types.items():
                    if ext in extensions:
                        folder = category
                        break

                dest_folder = os.path.join(target_dir, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file_name))
                logging.info(f"Movido: {file_name} → {dest_folder}")

        print("Archivos organizados por tipo.")
        logging.info("Proceso completado: Organización por tipo.")

    except Exception as e:
        logging.error(f"Error al organizar archivos por tipo: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Se requieren los directorios fuente y destino.")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2]
    organize_by_type(source_directory, target_directory)
