import requests
from bs4 import BeautifulSoup
import logging
from project_config.settings import HEADERS

def make_request(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error en la solicitud a {url}: {e}")
        return None
