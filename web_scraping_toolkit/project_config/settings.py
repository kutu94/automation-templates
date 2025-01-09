from scripts.clean_and_validate import remove_duplicates, fill_missing_values, normalize_text, validate_date_format


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
}


TARGET_URLS = {
    "prices": "https://www.amazon.es/s?k=laptops",
    "articles": "https://www.bbc.com/mundo",
    "inventory_url": "https://www.example.com/inventory",
    "monitor":  "https://www.amazon.es/gp/browse.html?node=937992031&ref_=nav_em__lap_0_2_13_5"
}

# Configuración para la extracción de artículos
SCRAPING_SETTINGS = {
    "article_url": "https://www.bbc.com/mundo",
    "article_tag": "h3",
    "article_class": "bbc-pam0zn e47bds20"
}

# Configuración opcional para proxies
#PROXIES = {
#    "http": "http://123.45.67.89:8080",
#    "https": "http://123.45.67.89:8080",
#}

PROCESSING_SETTINGS = {
    "prices": {
        "cleaning_steps": [
            remove_duplicates,
            lambda df: fill_missing_values(df, "price", "0.00"),
            lambda df: normalize_text(df, ["name"]),
        ],
        "validation_steps": [
            ("price", lambda x: x.replace(".", "", 1).isdigit()),
        ],
    },
    "inventory": {
        "cleaning_steps": [
            remove_duplicates,
            lambda df: fill_missing_values(df, "price", "0.00"),
            lambda df: fill_missing_values(df, "availability", "Desconocido"),
            lambda df: normalize_text(df, ["name", "availability"]),
        ],
        "validation_steps": [
            ("price", lambda x: x.replace(".", "", 1).isdigit()),
        ],
    },
    "articles": {
        "cleaning_steps": [
            remove_duplicates,
            lambda df: fill_missing_values(df, "title", "Sin Título"),
            lambda df: normalize_text(df, ["title"]),
        ],
        "validation_steps": [
            ("date", validate_date_format),
        ],
    },
}