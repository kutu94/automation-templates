# Automatización de Flujos de Trabajo

## Descripción
Este proyecto automatiza flujos de trabajo comunes en empresas, conectando diferentes herramientas y plataformas como formularios, hojas de cálculo y CRMs. Con funcionalidades flexibles y adaptables, esta plantilla es ideal para empresas que necesitan procesar datos, generar informes y enviar alertas automáticamente.

## Características Principales
- **Extracción de datos:** Obtención de datos desde una fuente externa (API, base de datos, archivo).
- **Procesamiento de datos:** Limpieza y transformación de los datos obtenidos.
- **Envío a Google Sheets:** Almacena los datos procesados en una hoja de cálculo de Google.
- **Envío al CRM:** Transfiere los datos a un sistema CRM para gestión empresarial.
- **Notificaciones:** Envío de alertas al equipo sobre eventos clave.



## Instalación
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/kutu94/automation_workflows.git
   cd automation_workflows

   ```

2. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## Configurar el archivo .env
1. **Crea un archivo `.env` en la raíz del proyecto.**
2. **Escribe las variables de entorno necesarias:**
   ```bash
    GOOGLE_SHEETS_API_KEY=tu_api_key
    CRM_API_URL=https://tu_crm.com/api
    CRM_API_KEY=tu_crm_api_key

3. **Ejecutar el script:**
   ```bash
   python main.py
   ```    
         
## Licencia
Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

