import os
import subprocess

# Directorio raíz del proyecto
project_root = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(project_root, "data")
organized_dir = os.path.join(project_root, "organized_files")

# Crea los directorios base si no existen
for directory in [data_dir, organized_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    while True:
        print("\n=== Gestión de Archivos ===")
        print("Selecciona una funcionalidad:")
        print("1. Detectar Archivos Duplicados")
        print("2. Eliminar Archivos Vacíos")
        print("3. Organizar Archivos por Fecha")
        print("4. Organizar Archivos por Tipo")
        print("5. Renombrado Masivo")
        print("6. Mover Archivos")
        print("7. Salir\n")

        option = input("Elige una opción (1-7): ")

        if option == "1":  # Detectar duplicados
            subprocess.run(["python", "scripts/detect_duplicates.py", data_dir])
        elif option == "2":
            subprocess.run(["python", "scripts/delete_empty_files.py", data_dir])
        elif option == "3":
            subprocess.run(["python", "scripts/organize_by_date.py", data_dir, organized_dir])
        elif option == "4":
            subprocess.run(["python", "scripts/organize_by_type.py", data_dir, organized_dir])
        elif option == "5":
            subprocess.run(["python", "scripts/rename_files.py", data_dir])
        elif option == "6":
            subprocess.run(["python", "scripts/move_files.py", data_dir, organized_dir])
        elif option == "7":
            print("\nSaliendo... ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
