import os
import sys
# Agrega el directorio raíz del proyecto al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import logging
import requests
from bs4 import BeautifulSoup
from scripts.clean_and_validate import process_scraped_data
from scripts.export_utils import export_to_json, export_to_csv
from project_config.settings import HEADERS, TARGET_URLS, PROCESSING_SETTINGS

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def scrape_inventory(url):
    """
    Extrae el inventario desde la URL especificada.
    """
    try:
        logging.info(f"Iniciando scraping de inventario en {url}")
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("div", class_="product-title")
        prices = soup.find_all("div", class_="price")
        availabilities = soup.find_all("div", class_="availability")

        data = []
        for product, price, availability in zip(products, prices, availabilities):
            data.append({
                "name": product.get_text(strip=True),
                "price": price.get_text(strip=True),
                "availability": availability.get_text(strip=True),
            })

        logging.info(f"Inventario encontrado: {len(data)} productos.")
        return data

    except Exception as e:
        logging.error(f"Error al realizar el scraping: {e}")
        return []


def process_inventory(scraped_data):
    """
    Limpia, valida y exporta los datos de inventario.
    """
    settings = PROCESSING_SETTINGS["inventory"]
    cleaned_data = process_scraped_data(scraped_data, settings["cleaning_steps"], settings["validation_steps"])
    return cleaned_data


def export_inventory(data):
    """
    Exporta los datos de inventario en formatos JSON y CSV.
    """
    json_path = os.path.join(project_root, "data", "inventory.json")
    csv_path = os.path.join(project_root, "data", "inventory.csv")

    export_to_json(data.to_dict(orient="records"), json_path)
    export_to_csv(data.to_dict(orient="records"), csv_path)

    logging.info("Inventario procesado y exportado correctamente.")
    print("Inventario procesado y exportado correctamente.")


if __name__ == "__main__":
    url = TARGET_URLS.get("inventory_url", "https://example.com/inventory")
    scraped_data = scrape_inventory(url)

    if scraped_data:
        cleaned_data = process_inventory(scraped_data)
        export_inventory(cleaned_data)
    else:
        print("No se encontraron datos de inventario.")
