# Notification Toolkit

## Descripción
El **Notification Toolkit** es una plantilla modular diseñada para automatizar el envío de notificaciones a través de múltiples canales. Esta herramienta es adaptable y puede configurarse según las necesidades de cada cliente, ofreciendo soporte para:
- Notificaciones por correo electrónico.
- Mensajes en Slack.
- Mensajes SMS o WhatsApp (usando servicios como Twilio).

## Funcionalidades
1. **Notificaciones por Correo:**
   - Envío de correos electrónicos utilizando credenciales SMTP.
   - Configurable con cualquier proveedor (Gmail, Outlook, etc.).

2. **Notificaciones en Slack:**
   - Enviar mensajes a un canal o usuario específico utilizando Webhooks.

3. **Notificaciones SMS o WhatsApp:**
   - Envío de mensajes usando APIs como Twilio.
   - Ideal para alertas urgentes o comunicaciones rápidas.

4. **Uso de Variables de Entorno:**
   - Configuración segura mediante un archivo `.env` para manejar credenciales.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/kutu94/notification-toolkit.git
   cd notification-toolkit
