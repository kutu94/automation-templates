import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os

# Ruta al archivo de credenciales
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
credentials_file = os.path.join(project_root, "project_config", "credentials.json")

# Conexión a Google Sheets
def connect_to_google_sheets(sheet_name):
    """
    Conecta a Google Sheets usando credenciales y retorna el objeto de hoja.
    """
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(credentials)
    return client.open(sheet_name).sheet1

def send_to_google_sheets(data, sheet_name="AutomatizacionDatos"):
    """
    Envía datos procesados a Google Sheets.
    """
    try:
        # Conectar a la hoja
        sheet = connect_to_google_sheets(sheet_name)

        # Convertir los datos a una lista de listas
        if isinstance(data, pd.DataFrame):
            data = data.values.tolist()

        # Enviar datos a la hoja (sobrescribe contenido existente)
        sheet.clear()
        sheet.append_row(["name", "email", "phone", "email_is_valid", "phone_is_valid"])  # Encabezados
        sheet.append_rows(data)

        print("Datos enviados correctamente a Google Sheets.")
    except Exception as e:
        print(f"Error al enviar datos a Google Sheets: {e}")

if __name__ == "__main__":
    # Ejemplo de datos procesados
    processed_data = pd.DataFrame([
        {"name": "John Doe", "email": "john@example.com", "phone": "1234567890", "email_is_valid": True, "phone_is_valid": True},
        {"name": "Jane Smith", "email": "jane@example.com", "phone": "0987654321", "email_is_valid": True, "phone_is_valid": True},
    ])

    send_to_google_sheets(processed_data)
