import os
import json

# Ruta al archivo JSON con las respuestas
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_file = os.path.join(project_root, "data", "responses.json")

def fetch_data():
    """
    Carga datos desde un archivo JSON simulando una captura desde un formulario.
    """
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"El archivo {data_file} no existe.")

    with open(data_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    data = fetch_data()
    print("Datos capturados:")
    print(data)
