import mysql.connector
import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from project_config.settings import DB_CONFIG


#conectamos la base de datos
def connect_to_database():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)

        return conn
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

if __name__ == "__main__":
    connection = connect_to_database()
    if connection:
        print("La conexión fue establecida correctamente.")
        connection.close()
    else:
        print("No se pudo establecer la conexión.")
