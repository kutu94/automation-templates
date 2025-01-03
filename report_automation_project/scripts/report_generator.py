import matplotlib.pyplot as plt
from fpdf import FPDF
import os
from project_config.settings import OUTPUT_FOLDER, CHART_FOLDER , INPUT_FOLDER


"""generar una grafica de barras y lo guarda como imagen"""
def generate_chart(data, chart_name):
    try:
        os.makedirs(CHART_FOLDER, exist_ok=True)
        chart_path = os.path.join(CHART_FOLDER, chart_name)
        data.plot(kind='bar', color = 'skyblue')
        plt.title("Resumen de Datos")
        plt.xlabel("Categorías")
        plt.ylabel("Valores")
        plt.savefig(chart_path)
        plt.close()
        return chart_path
    except Exception as e:
        print(f"Error al generar la grafica: {e}")
        return None



"""generar el reporte en pdf"""
def generate_pdf_report(chart_path, output_file):
    try:
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Reporte automatico", ln=True, align="C")
        pdf.image(chart_path, x=10, y=20, w=180)
        pdf.output(os.path.join(OUTPUT_FOLDER, output_file))
        print(f"Reporte generado en: {os.path.join(OUTPUT_FOLDER, output_file)}")
    except Exception as e:
        print(f"Error al generar el reporte PDF: {e}")


