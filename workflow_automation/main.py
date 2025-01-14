import os
import subprocess

# Directorio raíz del proyecto
project_root = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(project_root, "data")

# Crea el directorio de datos si no existe
if not os.path.exists(data_dir):
    os.makedirs(data_dir)


def main():
    while True:
        print("\n=== Automatización de Flujos de Trabajo ===")
        print("Selecciona una funcionalidad:")
        print("1. Fetch Data (Obtener datos de un origen)")
        print("2. Process Data (Procesar datos obtenidos)")
        print("3. Send to Google Sheets (Enviar datos a Google Sheets)")
        print("4. Send to CRM (Enviar datos al CRM)")
        print("5. Notificar al equipo (Simular envío de notificaciones)")
        print("6. Salir\n")

        option = input("Elige una opción (1-6): ")

        if option == "1":
            print("\nEjecutando: Fetch Data...")
            subprocess.run(["python", "scripts/fetch_data.py"])
        elif option == "2":
            print("\nEjecutando: Process Data...")
            subprocess.run(["python", "scripts/process_data.py"])
        elif option == "3":
            print("\nEjecutando: Send to Google Sheets...")
            subprocess.run(["python", "scripts/send_to_sheets.py"])
        elif option == "4":
            print("\nEjecutando: Send to CRM...")
            subprocess.run(["python", "scripts/send_to_crm.py"])
        elif option == "5":
            print("\nEjecutando: Notificar al equipo...")
            subprocess.run(["python", "scripts/notify_team.py"])
        elif option == "6":
            print("\nSaliendo... ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Intenta nuevamente.\n")


if __name__ == "__main__":
    main()
