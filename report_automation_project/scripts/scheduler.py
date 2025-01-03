import schedule
import time
from main import main


# generador de reportes automatico
def job():
    main(
        input_file="data/example_data.csv",
        output_file="output/weekly_report.pdf",
        group_column="region",
        aggregate_column="sales",
    )

    #configurar tarea
    schedule.every().monday.at("08:00").do(job)

if __name__ == "__main__":
    print("Programador de tareas iniciado. Esperando próxima ejecución...")
    while True:
        schedule.run_pending()
        time.sleep(1)