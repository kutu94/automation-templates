import csv
from fpdf import FPDF


def exportar_a_csv(cursor, file_path):
    """Exporta los resultados de una consulta a un archivo CSV."""
    try:
        results = cursor.fetchall()  # Trae todas las filas de una sola vez
        if not results:
            print("No hay datos para exportar.")
            return

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribir los nombres de las columnas
            column_names = [desc[0] for desc in cursor.description]
            writer.writerow(column_names)

            # Escribir los datos
            writer.writerows(results)

        print(f"Datos exportados correctamente a {file_path}.")
    except Exception as e:
        print(f"Error al exportar a CSV: {e}")


def exportar_a_pdf(cursor, file_path):
    """Exporta los resultados de una consulta a un archivo PDF."""
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Títulos de las columnas
        column_names = [desc[0] for desc in cursor.description]
        pdf.cell(200, 10, txt="Reporte de Datos", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt=" | ".join(column_names), ln=True, align='L')

        # Datos
        for row in cursor.fetchall():
            pdf.cell(200, 10, txt=" | ".join(str(item) for item in row), ln=True, align='L')

        # Guardar PDF
        pdf.output(file_path)
        print(f"Datos exportados correctamente a {file_path}.")
    except Exception as e:
        print(f"Error al exportar a PDF: {e}")