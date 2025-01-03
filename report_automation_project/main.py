
from project_config.settings import OUTPUT_FOLDER, INPUT_FOLDER, DEFAULT_GROUP_COLUMN, DEFAULT_AGGREGATE_COLUMN
from scripts.data_processor import load_data, process_data
from scripts.report_generator import generate_chart, generate_pdf_report
from scripts.logger import setup_logger
from scripts.notifier import send_email_notification



def main():
    # Configuración predeterminada
    input_file = f"{INPUT_FOLDER}/example_data.csv"
    output_file = "example_report.pdf"
    group_column = DEFAULT_GROUP_COLUMN
    aggregate_column = DEFAULT_AGGREGATE_COLUMN

    # Cargar y procesar datos
    data = load_data(input_file)
    if data is not None:
        summary = process_data(data, group_column, aggregate_column)

        # Generar gráfico y reporte
        if summary is not None:
            chart_path = generate_chart(summary, chart_name="sales_chart.png")
            if chart_path:
                generate_pdf_report(chart_path, output_file)

setup_logger()

if __name__ == "__main__":
    main()


send_email_notification(
    "Reporte Generado",
    "El reporte ha sido generado exitosamente y está disponible en la carpeta de salida."
)