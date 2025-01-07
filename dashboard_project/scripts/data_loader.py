import pandas as pd

def cargar_datos_ventas(file_path):
    """Carga el dataset de ventas."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo {file_path}: {e}")
        return None

def cargar_datos_inventario(file_path):
    """Carga el dataset de inventario."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo {file_path}: {e}")
        return None

