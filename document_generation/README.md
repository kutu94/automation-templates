# Generación de Documentos Automatizada

## Descripción
Este proyecto se centra en la **creación automática de documentos** (Word y PDF) y en el **procesamiento de datos** previo. Permite generar informes o facturas usando plantillas, crear PDFs personalizados y producir reportes en formato tabular, todo a partir de datos sin procesar.

## Estructura del Proyecto
document_generation/
- ├── templates/                  # Carpeta para plantillas de documentos
- │   ├── invoice_template.docx   # Plantilla para facturas
- │   ├── contract_template.docx  # Plantilla para contratos
- │
- ├── data/                       # Carpeta para almacenar datos
- │   ├── sales_data.csv          # Datos de ventas (opcional)
- │   ├── client_data.json        # Información de clientes
- │
- ├── output/                     # Carpeta para almacenar los documentos generados
- │   ├── invoices/               # Facturas generadas
- │   ├── contracts/              # Contratos generados
- │
- ├── project_config/             # Configuración del proyecto
- │   ├── settings.py             # Configuración general (e.g., rutas, plantillas)
- │
- ├── scripts/                    # Scripts para cada funcionalidad
- │   ├── generate_word.py        # Genera documentos Word
- │   ├── generate_pdf.py         # Genera documentos PDF
- │   ├── process_data.py         # Procesa datos de entrada
- │
- ├── main.py                     # Punto de entrada principal del proyecto
- ├── README.md                   # Documentación del proyecto
- ├── requirements.txt            # Dependencias del proyecto
- └── .env                        # Variables de entorno


## Funcionalidades Principales

1. **Process Data (`process_data.py`):**
   - Lee datos desde un archivo CSV o JSON.
   - Aplica limpieza (eliminar filas vacías, quitar espacios) y validaciones básicas.
   - Opcionalmente, guarda el resultado en un nuevo archivo.

2. **Generate Word (`generate_word.py`):**
   - Toma una plantilla `.docx` con marcadores (`{{campo}}`).
   - Reemplaza esos marcadores con datos reales (por ejemplo, cliente, monto de factura).
   - Guarda el documento generado en la carpeta `output/`.

3. **Generate PDF (`generate_pdf.py`):**
   - Genera un archivo PDF (por ejemplo, una factura) usando la librería `fpdf`.
   - Permite personalizar encabezados, textos y datos de detalle.

4. **Generate Report (`generate_report.py`):**
   - Crea un reporte tabular en PDF tomando datos de un archivo CSV/JSON.
   - Muestra columnas y filas con un formato básico de tabla.
   - Guarda el reporte en `output/reports/`.

5. **Menú Interactivo (`main.py`):**
   - Permite ejecutar cada script de forma independiente.
   - Pide al usuario elegir una opción y llama a los scripts mediante `subprocess.run`.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/kutu94/document_generation.git
   cd document_generation

2. **Instalar dependencias**:
    ```bash
   pip install -r requirements.txt

## Dependencias
**Consulta requirements.txt para ver las librerías clave:**
    
    pandas==1.5.3
    python-docx==0.8.11
    fpdf==1.7.2


## Posibles Extensiones
- Integración con notificaciones: Enviar correos o mensajes cuando se generen documentos.
- Integración con Google Drive: Subir los PDFs o documentos Word automáticamente.
- Plantillas avanzadas: Usar Jinja2 o librerías similares para plantillas con mayor lógica.

## Notas
- Verifica la carpeta templates/ si necesitas agregar tus plantillas .docx personalizadas.
- Ajusta rutas y nombres de archivos según tus preferencias en cada script o en el menú de main.py.

## Licencia

- Este proyecto está licenciado bajo la MIT License.