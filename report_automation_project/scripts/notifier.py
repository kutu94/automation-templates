import smtplib
from email.mime.text import MIMEText
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from project_config.settings import USERNAME, PASSWORD, SMTP_SERVER, PORT_SMTP, NOTIFY_EMAIL

def send_email_notification(subject, message):
    """Envía una notificación por correo"""
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = USERNAME
        msg["To"] = NOTIFY_EMAIL

        with smtplib.SMTP(SMTP_SERVER, PORT_SMTP) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)
            server.sendmail(USERNAME, [NOTIFY_EMAIL], msg.as_string())
        print(f"Notificación enviada a {NOTIFY_EMAIL}")
    except Exception as e:
        print(f"Error al enviar notificación: {e}")