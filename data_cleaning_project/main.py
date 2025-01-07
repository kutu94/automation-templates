from scripts.data_cleaning import fill_missing_values, remove_duplicates, normalize_text
from scripts.data_validation import validate_email, validate_date_format
from scripts.report_generator import setup_logger, log_start, log_stats, log_errors, log_end
from project_config.settings import RAW_DATA_PATH, CLEANED_DATA_PATH, LOG_FILE_PATH
import pandas as pd

def main():
    # Configura el logger
    log_file = setup_logger()
    log_start()

    # Carga de datos
    print("Cargando datos...")
    original_df = pd.read_csv(RAW_DATA_PATH)
    cleaned_df = original_df.copy()

    # Limpieza de datos
    print("Realizando limpieza de datos...")
    cleaned_df = fill_missing_values(cleaned_df, "Edad", 30)
    cleaned_df = remove_duplicates(cleaned_df)
    cleaned_df = normalize_text(cleaned_df, "Nombre")

    # Validación de datos
    print("Validando datos...")
    cleaned_df.loc[:, "Correo Válido"] = cleaned_df["Correo"].apply(validate_email)
    cleaned_df.loc[:, "Registro Válido"] = cleaned_df["Registro"].apply(validate_date_format)

    # Estadísticas
    log_stats(original_df, cleaned_df)

    # Exporta datos limpios
    print("Exportando datos limpios...")
    cleaned_df.to_csv(CLEANED_DATA_PATH, index=False)

    # Finaliza el proceso
    log_end()

    # Informa al usuario dónde encontrar el log
    print(f"Proceso completado. Revisa el log en: {log_file}")

if __name__ == "__main__":
    main()
