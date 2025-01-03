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
