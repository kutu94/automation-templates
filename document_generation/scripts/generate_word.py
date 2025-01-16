import os
from docx import Document


def generate_word(template_path, output_path, data):
    """
    Genera un documento Word basado en una plantilla y datos proporcionados.

    Args:
        template_path (str): Ruta al archivo de plantilla (.docx).
        output_path (str): Ruta donde se guardará el documento generado.
        data (dict): Diccionario con los datos para completar la plantilla.
    """
    try:
        # Cargar la plantilla
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"La plantilla no existe: {template_path}")

        document = Document(template_path)

        # Reemplazar marcadores en el texto
        for paragraph in document.paragraphs:
            for key, value in data.items():
                if f"{{{{{key}}}}}" in paragraph.text:
                    paragraph.text = paragraph.text.replace(f"{{{{{key}}}}}", value)

        # Guardar el documento generado
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        document.save(output_path)
        print(f"Documento generado correctamente: {output_path}")

    except Exception as e:
        print(f"Error al generar el documento Word: {e}")


if __name__ == "__main__":
    # Ruta de la plantilla y salida
    template = "templates/invoice_template.docx"
    output = "output/invoices/invoice_001.docx"

    # Datos para completar la plantilla
    data = {
        "client_name": "Juan Pérez",
        "invoice_number": "001",
        "date": "2025-01-10",
        "total": "$150.00",
    }

    # Generar el documento
    generate_word(template, output, data)