import os
import sys
# Agrega el directorio raíz del proyecto al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import logging
from scripts.scraping_basics import make_request
from project_config.settings import SCRAPING_SETTINGS, PROCESSING_SETTINGS
from scripts.clean_and_validate import process_scraped_data
from scripts.export_utils import export_to_json, export_to_csv

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def scrape_articles(url):
    """
    Extrae artículos de la página web especificada en la URL.
    """
    try:
        logging.info(f"Iniciando scraping en {url}")
        print(f"Conectando a {url}...")

        # Haz la solicitud
        soup = make_request(url)
        if not soup:
            logging.warning(f"No se pudo obtener contenido HTML de {url}")
            print("No se pudo obtener contenido de la página.")
            return []

        # Extrae los artículos
        articles = soup.find_all(
            SCRAPING_SETTINGS["article_tag"],
            class_=SCRAPING_SETTINGS["article_class"]
        )

        # Verifica si se encontraron artículos
        if not articles:
            logging.warning("No se encontraron artículos en la página.")
            print("No se encontraron artículos en la página.")
            return []

        # Procesa los datos extraídos
        data = [{"title": article.get_text(strip=True)} for article in articles if article.get_text()]
        logging.info(f"Artículos encontrados: {len(data)}")
        print(f"{len(data)} artículos encontrados. Proceso completado.")
        return data

    except Exception as e:
        logging.error(f"Error al realizar el scraping: {e}", exc_info=True)
        print(f"Error durante la extracción: {e}")
        return []


def process_articles(scraped_data):
    """
    Limpia, valida y exporta los datos extraídos.
    """
    try:
        # Configuración para limpieza y validación
        settings = PROCESSING_SETTINGS["articles"]

        # Limpieza y validación
        cleaned_data = process_scraped_data(scraped_data, settings["cleaning_steps"], settings["validation_steps"])

        # Rutas absolutas para exportación
        json_path = os.path.join(project_root, "data", "articles.json")
        csv_path = os.path.join(project_root, "data", "articles.csv")

        # Exportar los datos en múltiples formatos
        export_to_json(cleaned_data.to_dict(orient="records"), json_path)
        export_to_csv(cleaned_data.to_dict(orient="records"), csv_path)

        logging.info("Artículos procesados y exportados correctamente.")
        print("Artículos procesados y exportados correctamente.")

    except Exception as e:
        logging.error(f"Error al procesar los artículos: {e}", exc_info=True)
        print(f"Error al procesar los artículos: {e}")


if __name__ == "__main__":
    # URL para artículos
    url = SCRAPING_SETTINGS["article_url"]
    # Scraping de artículos
    scraped_data = scrape_articles(url)
    # Limpieza, validación y exportación
    if scraped_data:
        process_articles(scraped_data)
    else:
        print("No se encontraron datos para procesar.")
