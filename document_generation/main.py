import os
import subprocess

def main():
    while True:
        print("\n=== Menú de Generación de Documentos ===")
        print("1. Process Data (limpiar y validar datos)")
        print("2. Generate Word (crear documento .docx)")
        print("3. Generate PDF (crear documento .pdf)")
        print("4. Generate Report (generar reporte tabular en .pdf)")
        print("5. Salir\n")

        option = input("Elige una opción (1-5): ")

        if option == "1":
            print("\nProcesando datos: 'raw_data.csv' → 'processed_data.csv' (opcional)")
            # Por ejemplo: data/raw_data.csv -> data/processed_data.csv
            input_file = "data/raw_data.csv"        # Ajusta según tu estructura
            output_file = "data/processed_data.csv" # Ajusta según tu estructura
            subprocess.run(["python", "scripts/process_data.py", input_file, output_file])

        elif option == "2":
            print("\nGenerando documento Word desde la plantilla ...")
            # Llamamos al script generate_word.py sin argumentos
            # Ajusta dentro de generate_word.py si quieres pasarle algo adicional.
            subprocess.run(["python", "scripts/generate_word.py"])

        elif option == "3":
            print("\nGenerando documento PDF ...")
            # Llamamos a generate_pdf.py sin argumentos
            # Si en generate_pdf.py esperas datos, ajústalo para recibirlos o simularlos.
            subprocess.run(["python", "scripts/generate_pdf.py"])

        elif option == "4":
            print("\nGenerando reporte en PDF con 'generate_report.py' ...")
            # Ejemplo: data/report_data.csv -> output/reports/report_summary.pdf
            input_file = "data/report_data.csv"
            output_file = "output/reports/reporte_resumen.pdf"
            subprocess.run(["python", "scripts/generate_report.py", input_file, output_file])

        elif option == "5":
            print("\nSaliendo... ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intenta nuevamente.\n")


if __name__ == "__main__":
    main()
