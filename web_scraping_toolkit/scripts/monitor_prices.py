import requests
from bs4 import BeautifulSoup
import logging
import csv
import sys
import os
import time
import shutil
from datetime import datetime

# Agrega el directorio raíz del proyecto al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from project_config.settings import HEADERS, TARGET_URLS
from scripts.clean_and_validate import process_scraped_data
from project_config.settings import PROCESSING_SETTINGS


# Crear el directorio de logs si no existe
log_dir = os.path.join(project_root, "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configuración de logs
logging.basicConfig(
    filename=os.path.join(log_dir, "scraping_log.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def scrape_prices():
    url = TARGET_URLS.get("monitor")
    if not url:
        logging.error("La URL para precios no está configurada en settings.")
        print("Error: La URL para precios no está configurada.")
        return []

    start_time = time.time()
    try:
        logging.info(f"Iniciando scraping de precios en {url}")
        print(f"Conectando a {url}...")
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("div", class_="a-section octopus-pc-asin-title")
        prices = soup.find_all("span", class_="a-price")

        data = []
        for product, price in zip(products, prices):
            product_name = product.get_text(strip=True)
            product_price = price.get_text(strip=True)
            data.append({"name": product_name, "price": product_price})

        elapsed_time = time.time() - start_time
        logging.info(f"Scraping completado en {elapsed_time:.2f} segundos. {len(data)} productos encontrados.")
        print(f"Scraping completado. {len(data)} productos encontrados.")
        return data

    except Exception as e:
        logging.error(f"Error al realizar el scraping: {e}")
        print(f"Error al realizar el scraping: {e}")
        return []

def export_prices(data):
    """Limpia, valida y exporta los datos extraídos."""
    try:
        # Configuración para limpieza y validación
        settings = PROCESSING_SETTINGS["prices"]

        # Limpieza y validación
        cleaned_data = process_scraped_data(data, settings["cleaning_steps"], settings["validation_steps"])

        # Rutas absolutas para exportación
        csv_path = os.path.join(project_root, "data", "prices.csv")

        # Exportar los datos limpios
        from scripts.export_utils import export_to_csv
        export_to_csv(cleaned_data.to_dict(orient="records"), csv_path)

        logging.info("Precios procesados y exportados correctamente.")
        print("Precios procesados y exportados correctamente.")
    except Exception as e:
        logging.error(f"Error al procesar los precios: {e}", exc_info=True)
        print(f"Error al procesar los precios: {e}")


if __name__ == "__main__":
    scraped_data = scrape_prices()
    if scraped_data:
        export_prices(scraped_data)
    else:
        print("No se encontraron datos para procesar.")