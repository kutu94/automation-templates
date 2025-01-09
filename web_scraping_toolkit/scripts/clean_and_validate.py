import pandas as pd
import re
import logging

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def fill_missing_values(df, column, value):
    """Rellena valores faltantes en una columna específica."""
    if column in df.columns:
        logging.info(f"Rellenando valores faltantes en la columna: {column}")
        df[column] = df[column].fillna(value)
    return df


def remove_duplicates(df):
    """Elimina filas duplicadas del DataFrame."""
    logging.info("Eliminando filas duplicadas")
    return df.drop_duplicates()


def normalize_text(df, columns):
    """Convierte texto en columnas específicas a formato título."""
    for column in columns:
        if column in df.columns:
            logging.info(f"Normalizando texto en la columna: {column}")
            df[column] = df[column].str.title()
    return df


def validate_column(df, column, validation_function):
    """Valida una columna usando una función personalizada."""
    if column in df.columns:
        logging.info(f"Validando columna: {column}")
        df[f"{column}_is_valid"] = df[column].apply(validation_function)
    return df


def validate_email(email):
    """Valida el formato de un correo electrónico."""
    if not isinstance(email, str):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def validate_date_format(date):
    """Valida si una fecha tiene un formato correcto."""
    try:
        pd.to_datetime(date, format="%Y-%m-%d")
        return True
    except ValueError:
        return False


def process_scraped_data(data, cleaning_steps, validation_steps):
    """
    Procesa los datos scrapeados aplicando pasos de limpieza y validación.

    cleaning_steps: Lista de funciones para limpieza (e.g., [remove_duplicates, normalize_text])
    validation_steps: Lista de funciones para validación (e.g., [(column, validation_function)])
    """
    logging.info("Iniciando el proceso de limpieza y validación.")
    df = pd.DataFrame(data)

    # Aplicar pasos de limpieza
    for step in cleaning_steps:
        logging.info(f"Aplicando paso de limpieza: {step.__name__}")
        df = step(df)

    # Aplicar pasos de validación
    for column, validation_function in validation_steps:
        logging.info(f"Aplicando validación en la columna: {column}")
        df = validate_column(df, column, validation_function)

    logging.info("Proceso de limpieza y validación completado.")
    return df


# Bloque para pruebas directas
if __name__ == "__main__":
    # Prueba con precios
    scraped_prices = [
        {"name": "Monitor Dell", "price": "150.99"},
        {"name": "Teclado mecánico", "price": ""},
        {"name": "Monitor Dell", "price": "150.99"},
    ]

    cleaning_steps = [
        remove_duplicates,
        lambda df: fill_missing_values(df, "price", "0.00"),
        lambda df: normalize_text(df, ["name"]),
    ]

    validation_steps = [
        ("price", lambda x: x.replace(".", "", 1).isdigit()),  # Validar precios como números
    ]

    cleaned_prices = process_scraped_data(scraped_prices, cleaning_steps, validation_steps)
    print(cleaned_prices)

    # Prueba con artículos
    scraped_articles = [
        {"title": "noticia 1", "date": "2025-01-01"},
        {"title": "NOTICIA 2", "date": "2025/01/01"},
        {"title": "", "date": ""},
    ]

    cleaning_steps = [
        remove_duplicates,
        lambda df: fill_missing_values(df, "title", "Sin Título"),
        lambda df: normalize_text(df, ["title"]),
    ]

    validation_steps = [
        ("date", validate_date_format),  # Validar fechas
    ]

    cleaned_articles = process_scraped_data(scraped_articles, cleaning_steps, validation_steps)
    print(cleaned_articles)
