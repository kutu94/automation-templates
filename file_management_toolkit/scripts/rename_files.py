import os
import logging

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def rename_files(source_dir, prefix="file", start_number=1):
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"El directorio fuente no existe: {source_dir}")

        count = start_number
        for file_name in os.listdir(source_dir):
            file_path = os.path.join(source_dir, file_name)

            if os.path.isfile(file_path):
                new_name = f"{prefix}_{count}{os.path.splitext(file_name)[1]}"
                new_path = os.path.join(source_dir, new_name)
                os.rename(file_path, new_path)
                logging.info(f"Renombrado: {file_name} → {new_name}")
                count += 1

        print("Renombrado masivo completado.")
        logging.info("Proceso completado: Renombrado masivo.")

    except Exception as e:
        logging.error(f"Error al renombrar archivos: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Error: Se requiere el directorio fuente.")
        sys.exit(1)

    source_directory = sys.argv[1]
    rename_files(source_directory)
