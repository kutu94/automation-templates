import os
import json

def send_to_crm(data, crm_file="data/crm_data.json"):
    """
    Simula el envío de datos procesados a un CRM escribiéndolos en un archivo JSON.

    Args:
        data (list): Lista de datos procesados a enviar.
        crm_file (str): Ruta del archivo donde se almacenarán los datos simulando el CRM.
    """
    try:
        # Crea el directorio de datos si no existe
        data_dir = os.path.dirname(crm_file)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Verifica si ya existe un archivo CRM y carga datos previos
        if os.path.exists(crm_file):
            with open(crm_file, "r", encoding="utf-8") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Agregar los nuevos datos al archivo existente
        updated_data = existing_data + data

        # Guardar los datos actualizados en el archivo CRM
        with open(crm_file, "w", encoding="utf-8") as file:
            json.dump(updated_data, file, indent=4, ensure_ascii=False)

        print(f"Datos enviados al CRM y almacenados en {crm_file}.")
    except Exception as e:
        print(f"Error al enviar datos al CRM: {e}")


if __name__ == "__main__":
    # Datos de prueba
    processed_data = [
        {"id": 1, "name": "Cliente A", "email": "clientea@example.com", "status": "activo"},
        {"id": 2, "name": "Cliente B", "email": "clienteb@example.com", "status": "inactivo"},
    ]

    send_to_crm(processed_data)
