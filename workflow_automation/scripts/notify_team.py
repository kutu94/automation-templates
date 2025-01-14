import os
from datetime import datetime

def notify_team(message, log_file="logs/notifications.log"):
    """
    Simula el envío de una notificación al equipo escribiendo en un archivo de log.

    Args:
        message (str): El mensaje que se desea enviar.
        log_file (str): La ruta del archivo donde se registrarán las notificaciones.
    """
    try:
        # Crea el directorio de logs si no existe
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Escribe la notificación en el archivo de log
        with open(log_file, "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {message}\n")

        print(f"Notificación enviada: {message}")
    except Exception as e:
        print(f"Error al enviar notificación: {e}")


if __name__ == "__main__":
    # Prueba de la función
    notify_team("El procesamiento de datos se completó con éxito.")
    notify_team("Se detectó un error en la conexión con Google Sheets.")
