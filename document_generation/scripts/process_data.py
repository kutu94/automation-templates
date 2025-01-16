import os
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def process_data(input_file, output_file=None):
    """
    Lee datos desde un archivo (CSV o JSON), aplica transformaciones básicas
    y opcionalmente guarda los datos procesados en un archivo de salida.

    Args:
        input_file (str): Ruta del archivo de entrada (CSV o JSON).
        output_file (str, opcional): Ruta del archivo donde se guardarán los datos procesados.
                                     Si no se proporciona, simplemente se devuelve el DataFrame.

    Returns:
        pd.DataFrame: DataFrame con los datos procesados.
    """
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"El archivo de entrada no existe: {input_file}")

        # Determinar extensión del archivo
        ext = os.path.splitext(input_file)[1].lower()
        if ext == ".csv":
            df = pd.read_csv(input_file)
        elif ext == ".json":
            df = pd.read_json(input_file)
        else:
            raise ValueError("Formato de archivo no soportado. Use .csv o .json")

        # Ejemplo de limpieza básica:
        # 1. Eliminar filas con datos vacíos.
        df.dropna(inplace=True)

        # 2. Quitar espacios en columnas de texto (strip).
        for col in df.select_dtypes(include=["object"]):
            df[col] = df[col].str.strip()

        # 3. Logs de información
        logging.info(f"Se han procesado {len(df)} filas de datos desde {input_file}.")

        # Guardar si se especifica un archivo de salida
        if output_file:
            ext_out = os.path.splitext(output_file)[1].lower()
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            if ext_out == ".csv":
                df.to_csv(output_file, index=False)
            elif ext_out == ".json":
                df.to_json(output_file, orient="records", indent=4, force_ascii=False)
            else:
                raise ValueError("Formato de archivo de salida no soportado. Use .csv o .json")

            logging.info(f"Datos procesados guardados en: {output_file}")

        return df

    except Exception as e:
        logging.error(f"Error al procesar datos: {e}")
        raise


if __name__ == "__main__":
    # Ejemplo de uso
    input_path = "data/raw_data.csv"  # Cambia la ruta si deseas otro archivo
    output_path = "output/processed_data.csv"

    df_processed = process_data(input_path, output_path)
    print("Datos procesados:\n", df_processed.head())
