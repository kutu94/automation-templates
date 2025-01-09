import csv
import json
import logging


def export_to_csv(data, file_path):
    try:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"Datos exportados a {file_path}")
    except Exception as e:
        logging.error(f"Error al exportar a CSV: {e}")

def export_to_json(data, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        logging.info(f"Datos exportados a {file_path}")
    except Exception as e:
        logging.error(f"Error al exportar a JSON: {e}")
