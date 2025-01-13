import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import os
from dotenv import load_dotenv

# Cargar configuraciones desde .env
load_dotenv()

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def send_email(subject, body, recipient):
    """
    Envía un correo electrónico usando SMTP.

    Args:
        subject (str): Asunto del correo.
        body (str): Cuerpo del correo.
        recipient (str): Dirección del destinatario.
    """
    try:
        # Credenciales desde .env
        sender_email = os.getenv("EMAIL_USERNAME")
        sender_password = os.getenv("EMAIL_PASSWORD")

        if not sender_email or not sender_password:
            raise ValueError("Credenciales de correo no configuradas en .env")

        # Configuración del mensaje
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Configuración del servidor SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)

        logging.info(f"Correo enviado a {recipient} con el asunto: {subject}")
        print(f"Correo enviado a {recipient} con el asunto: {subject}")

    except Exception as e:
        logging.error(f"Error al enviar el correo: {e}")
        print(f"Error al enviar el correo: {e}")


if __name__ == "__main__":
    # Prueba del envío de correo
    send_email(
        subject="Notificación de Prueba",
        body="Este es un correo de prueba enviado desde la herramienta de notificaciones.",
        recipient="destinatario@gmail.com"
    )
