import logging
from datetime import datetime

def setup_logger():
    """Configura el logger para crear un archivo con la fecha actual."""
    fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/cleaning_report_{fecha_actual}.log"
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )
    return log_file  # Devuelve el nombre del archivo para referencia

def log_start():
    """Registra el inicio del proceso."""
    logging.info("=== Inicio del proceso de limpieza de datos ===")

def log_stats(original_df, cleaned_df):
    """Registra estadísticas del dataset."""
    logging.info(f"Número de registros iniciales: {len(original_df)}")
    logging.info(f"Número de registros después de limpieza: {len(cleaned_df)}")
    logging.info(f"Registros eliminados: {len(original_df) - len(cleaned_df)}")
    logging.info(f"Columnas procesadas: {list(original_df.columns)}")

def log_errors(errors):
    """Registra errores encontrados durante la limpieza."""
    if errors:
        logging.error("Errores encontrados durante la validación:")
        for error in errors:
            logging.error(f"- {error}")
    else:
        logging.info("No se encontraron errores durante la validación.")

def log_end():
    """Registra el fin del proceso."""
    logging.info("=== Proceso completado ===")
