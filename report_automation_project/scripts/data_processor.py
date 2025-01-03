import pandas as pd


#Carga los datos desde un archivo CSV o Excel
def load_data(file_path):
    try:
        if file_path.endswith('.csv'):
            return  pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
           return  pd.read_excel(file_path)
        else:
            raise ValueError(f"Formato de archivo no admitido: {file_path}, use CSV or XLSX")
    except Exception as e:
        raise ValueError(f"Error al cargar el archivo: {e}")
        return None

#Procesa los datos para generar métricas clave
def process_data(data, group_by_column, aggegate_column):
    try:
        summary = data.groupby(group_by_column)[aggegate_column].sum()
        return summary
    except Exception as e:
        print(f"Error al procesar los datos: {e}")
        return None

