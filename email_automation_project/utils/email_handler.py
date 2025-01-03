import sys
import os
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email
from datetime import datetime
#ruta absoluta del directorio raíz del proyecto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#ruta raíz al inicio del sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)
#imprtamos los settings
from project_config import settings


#Testeamos la conexión
def connect_imap():
    try:
        coneccion = imaplib.IMAP4_SSL(settings.IMAP_SERVER)
        coneccion.login(settings.USERNAME, settings.PASSWORD)
        print("Conexión exitosa")
        return coneccion
    except Exception as e:
        print("Error al conectar:", e)
        return None


#creamos una funciona para leer los emails
def search_unread_emails(coneccion):
    try:#seleccionamos la carpeta INBOX
        coneccion.select("INBOX")
        #buscamos los emails sin leer
        status, email_ids = coneccion.search(None, "UNSEEN")
        #devolvemos los id de los emails
        email_ids = email_ids[0].split()
        print(f"Correos no leídos encontrados: {len(email_ids)}")
        return email_ids
    except Exception as e:
        print("Error al buscar emails:", e)
        return []


#funcion para enviar respuesta automatica
def send_auto_reply(to_email, subject, body):
    try:
        server = smtplib.SMTP(settings.SMTP_SERVER, settings.PORT_SMTP)
        server.starttls()
        server.login(settings.USERNAME, settings.PASSWORD)


        message = MIMEMultipart()
        message["From"] = settings.USERNAME
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server.sendmail(settings.USERNAME, to_email, message.as_string())
        server.quit()
        print(f"Notificación enviada a {to_email}")

    except Exception as e:
        print(f"Error al enviar notificación a {to_email}: {e}")




#Recuperar el Contenido de un Correo
def fetch_email_content(coneccion, email_ids):
    try:
        #recupera el correo por su id
        status, email_data = coneccion.fetch(email_ids, "(RFC822)")
        #devuelve el contenido del correo
        raw_email = email_data[0][1]
        # Convierte el contenido en un objeto manejable
        message = email.message_from_bytes(raw_email)
        return message
    except Exception as e:
        print("Error al recuperar el contenido del correo:", e)
        return None


#funcion para emviar notificaciones a otro correo
def send_notification(to_email, subject, body):
    try:
        server = smtplib.SMTP(settings.SMTP_SERVER, settings.PORT_SMTP)
        server.starttls()
        server.login(settings.USERNAME, settings.PASSWORD)

        message = MIMEMultipart()
        message["From"] = settings.USERNAME
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server.sendmail(settings.USERNAME, to_email, message.as_string())
        server.quit()
        print(f"Notificación enviada a {to_email}")
    except Exception as e:
        print(f"Error al enviar notificación: {e}")



    # funcion para salvar attachments de los correos
def save_attachment(part, save_dir):
    try:
        filename = part.get_filename()
        if filename:
            filepath = os.path.join(save_dir, filename)
            with open(filepath, "wb") as f:
                f.write(part.get_payload(decode=True))
            print(f"Archivo adjunto guardado: {filepath}")
    except Exception as e:
        print(f"Error al guardar el archivo adjunto: {e}")



    #Procesar el Contenido del Correo
def process_email(message):
    try:#extraer el asunto y el remitente
        subject = message["Subject"]
        sender = message['From']

        #notificaciones por correo
        if 'Importante' in subject:
            send_notification(
                to_email='example@gmail.com',        #poner correo destino
                subject=f"Correo importante recibido: {subject}",
                body=f"Remitente: {sender}\nAsunto: {subject}"
            )
    except Exception as e:
        print(f"Error al procesar el correo: {e}")

    try:
        subject = message['Subject']
        sender = message['From']

        # Respuestas automáticas basadas en palabras clave
        if "Soporte" in subject:
            send_auto_reply(
                to_email=sender,
                subject="Consulta recibida",
                body="Hemos recibido su consulta y estamos procesándola. Nos pondremos en contacto pronto."
            )
        # Puedes añadir más condiciones si lo necesitas
    except Exception as e:
        print(f"Error al procesar el correo: {e}")

    try:
        subject = message['Subject']
        sender = message['From']

        # Descargar archivos adjuntos si el asunto contiene "Facturas"
        if "Facturas" in subject:
            save_dir = f"attachments/{datetime.now().strftime('%Y-%m-%d')}"
            os.makedirs(save_dir, exist_ok=True)

            if message.is_multipart():
                for part in message.walk():
                    if part.get_content_disposition() == "attachment":
                        save_attachment(part, save_dir)
    except Exception as e:
        print(f"Error al procesar el correo: {e}")



# Integrar Todo: Leer y Procesar Correos
def read_emails(coneccion):
    try:#buscar correos no leidos
        email_ids = search_unread_emails(coneccion)

        #recuperar el contenido de los correos
        for email_id in email_ids:
            message = fetch_email_content(coneccion, email_id)
            if message:
                process_email(message)
    except Exception as e:
        print(f"Error al leer los correos: {e}")





































