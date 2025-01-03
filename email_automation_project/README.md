# Script de Automatización de Correos Electrónicos

## Descripción
Este proyecto automatiza la gestión de correos electrónicos, proporcionando funcionalidades como:
- Lectura de correos no leídos desde la bandeja de entrada.
- Respuestas automáticas basadas en palabras clave.
- Descarga y organización de archivos adjuntos.
- Notificaciones de correos importantes.

## Funcionalidades
1. **Lectura de correos no leídos:**
   - Busca y procesa correos sin leer en la bandeja de entrada.
2. **Respuestas automáticas:**
   - Responde automáticamente a correos específicos.
3. **Descarga de archivos adjuntos:**
   - Guarda adjuntos en carpetas organizadas por remitente o fecha.
4. **Notificaciones por correo:**
   - Envía resúmenes de correos importantes al administrador.

## Cómo Usar
1. **Configura las credenciales:**
   - Crea un archivo `.env` con el siguiente formato:
     ```plaintext
     EMAIL_USERNAME=tu_correo@gmail.com
     EMAIL_PASSWORD=tu_contraseña_de_aplicación
     IMAP_SERVER=imap.gmail.com
     PORT=587
     SMTP_SERVER=smtp.gmail.com
     ```
2. **Instala dependencias:**
   ```bash
   pip install -r requirements.txt


# Email Automation Script

## Description
This project automates email management by providing functionalities such as:
- Reading unread emails from the inbox.
- Sending automatic replies based on keywords.
- Downloading and organizing email attachments.
- Sending notifications for important emails.

## Features
1. **Read Unread Emails:**
   - Searches and processes unread emails in the inbox.
2. **Automatic Replies:**
   - Automatically replies to specific emails.
3. **Attachment Download:**
   - Saves attachments in folders organized by sender or date.
4. **Email Notifications:**
   - Sends summaries of important emails to the administrator.

## How to Use
1. **Set up credentials:**
   - Create a `.env` file with the following format:
     ```plaintext
     EMAIL_USERNAME=your_email@gmail.com
     EMAIL_PASSWORD=your_application_password
     IMAP_SERVER=imap.gmail.com
     SMTP_SERVER=smtp.gmail.com
     SMTP_PORT=587
     ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
