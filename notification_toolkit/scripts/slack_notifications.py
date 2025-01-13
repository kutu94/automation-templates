import requests
import logging
import os
from dotenv import load_dotenv

# Cargar configuraciones desde .env
load_dotenv()

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def send_slack_message(message):
    """
    Envía un mensaje a un canal de Slack usando un webhook.

    Args:
        message (str): Mensaje a enviar.
    """
    try:
        webhook_url = os.getenv("SLACK_WEBHOOK_URL")
        if not webhook_url:
            raise ValueError("Webhook de Slack no configurado en .env")

        payload = {"text": message}
        response = requests.post(webhook_url, json=payload)

        if response.status_code == 200:
            logging.info("Mensaje enviado a Slack.")
            print("Mensaje enviado a Slack.")
        else:
            logging.error(f"Error al enviar mensaje a Slack: {response.status_code} {response.text}")

    except Exception as e:
        logging.error(f"Error al enviar mensaje a Slack: {e}")
        print(f"Error al enviar mensaje a Slack: {e}")


if __name__ == "__main__":
    # Prueba de envío a Slack
    send_slack_message("Este es un mensaje de prueba enviado desde Python.")
