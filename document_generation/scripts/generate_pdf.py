import os
from fpdf import FPDF


class PDFGenerator(FPDF):
    """
    Clase para generar PDFs con datos dinámicos.
    Puedes personalizar fuentes, tamaños, márgenes, etc.
    """

    def header(self):
        # Cabecera del documento
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Factura de Compra", 0, 1, "C")
        self.ln(5)

    def footer(self):
        # Pie de página
        self.set_y(-15)
        self.set_font("Arial", "I", 9)
        self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", 0, 0, "C")


def generate_pdf(data, output_path):
    """
    Genera un PDF con datos de factura (o los que necesites) usando FPDF.

    Args:
        data (dict): Datos necesarios para completar la factura.
        output_path (str): Ruta para guardar el archivo PDF generado.
    """
    pdf = PDFGenerator()
    pdf.alias_nb_pages()  # Para el conteo de páginas
    pdf.add_page()

    # Configurar fuente por defecto
    pdf.set_font("Arial", size=12)

    # Imprimir datos principales
    pdf.cell(0, 10, f"Cliente: {data.get('client_name', 'N/A')}", 0, 1)
    pdf.cell(0, 10, f"Factura Nro: {data.get('invoice_number', '---')}", 0, 1)
    pdf.cell(0, 10, f"Fecha: {data.get('date', '---')}", 0, 1)
    pdf.cell(0, 10, f"Total a pagar: {data.get('total', '---')}", 0, 1)

    # Espacio
    pdf.ln(10)

    # Agregar algún texto de ejemplo
    pdf.cell(0, 10, "Detalle de compra:", 0, 1)

    # Ejemplo: Detalle en forma de lista
    items = data.get("items", [])
    for item in items:
        pdf.cell(10)  # Indentar
        pdf.cell(0, 10, f"- {item}", 0, 1)

    # Crear carpeta de salida si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Guardar el PDF
    pdf.output(output_path)
    print(f"PDF generado: {output_path}")


if __name__ == "__main__":
    # Datos de ejemplo
    sample_data = {
        "client_name": "Juan Pérez",
        "invoice_number": "1001",
        "date": "2025-01-10",
        "total": "$200.00",
        "items": [
            "Producto A (x2)",
            "Producto B (x1)",
            "Producto C (x3)"
        ]
    }

    output_pdf = "output/invoices/factura_1001.pdf"
    generate_pdf(sample_data, output_pdf)