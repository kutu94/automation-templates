import os
import logging
from fpdf import FPDF
import pandas as pd

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class ReportPDF(FPDF):
    """
    Clase para generar un reporte PDF con encabezado y pie de página personalizados.
    """

    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Reporte Resumen", 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 9)
        self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", 0, 0, "C")


def generate_report(data_file, output_path):
    """
    Genera un reporte PDF tomando datos desde un archivo CSV o JSON.
    El reporte presenta un resumen tabular de la información.

    Args:
        data_file (str): Ruta del archivo con datos (CSV o JSON).
        output_path (str): Ruta donde se guardará el archivo PDF generado.
    """
    try:
        # Cargar datos desde CSV o JSON
        ext = os.path.splitext(data_file)[1].lower()
        if ext == ".csv":
            df = pd.read_csv(data_file)
        elif ext == ".json":
            df = pd.read_json(data_file)
        else:
            raise ValueError("Formato no soportado. Usa .csv o .json")

        # Crear instancia de PDF
        pdf = ReportPDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Escribir título del reporte
        pdf.cell(0, 10, f"Datos del Archivo: {os.path.basename(data_file)}", 0, 1)
        pdf.ln(5)

        # Si el DataFrame tiene muchas columnas, puedes ajustarlo dinámicamente.
        # Para este ejemplo, asumimos un número manejable de columnas.
        columns = df.columns.tolist()

        # Encabezados
        pdf.set_font("Arial", "B", 12)
        col_width = pdf.w / (len(columns) + 1)  # +1 para márgenes sencillos
        for col in columns:
            pdf.cell(col_width, 10, col, 1, 0, "C")
        pdf.ln()

        # Filas de datos
        pdf.set_font("Arial", size=12)
        for _, row in df.iterrows():
            for col in columns:
                # Convierte todo a string para imprimir
                cell_value = str(row[col])
                pdf.cell(col_width, 10, cell_value, 1, 0, "C")
            pdf.ln()

        # Crear carpeta de salida si no existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pdf.output(output_path)
        print(f"Reporte generado correctamente en: {output_path}")
        logging.info(f"Reporte generado en {output_path}")

    except Exception as e:
        logging.error(f"Error al generar reporte: {e}")
        print(f"Error al generar reporte: {e}")


if __name__ == "__main__":
    # Ejemplo de uso: archivo CSV o JSON
    # data/report_data.csv (o data/report_data.json)
    demo_data_file = "data/report_data.csv"
    output_report = "output/reports/reporte_resumen.pdf"
    generate_report(demo_data_file, output_report)
