import logging

def validate_data(data, required_columns):
    """Valida que las columnas necesarias estén presentes en el DataFrame"""
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        logging.error(f"Faltan las columnas requeridas: {missing_columns}")
        raise ValueError(f"Faltan las columnas requeridas: {missing_columns}")
    logging.info("Validación de datos completada exitosamente")

    