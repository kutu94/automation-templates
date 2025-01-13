from twilio.rest import Client
import os
from dotenv import load_dotenv

# Cargar configuraciones desde .env
load_dotenv()

def send_sms(to, message):
    """
    Envía un mensaje SMS usando Twilio.

    Args:
        to (str): Número de teléfono del destinatario (incluyendo código de país).
        message (str): Mensaje a enviar.
    """
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_phone = os.getenv("TWILIO_PHONE_NUMBER")

        if not account_sid or not auth_token or not from_phone:
            raise ValueError("Credenciales de Twilio no configuradas en .env")

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=from_phone,
            to=to
        )
        print(f"Mensaje enviado a {to}. SID: {message.sid}")

    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")
