import csv


#carga datos desde un archivo CSV a la base de datos.
def cargar_datos_desde_csv(conn, csv_file, table_name):
    try:
        cursor = conn.cursor()
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Lee el encabezado del archivo CSV

            placeholders = ', '.join(['%s'] * len(headers))
            insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({placeholders})"

            for row in reader:
                cursor.execute(insert_query, row)

        conn.commit()
        print(f"Datos cargados desde {csv_file} a la tabla {table_name}.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
    finally:
        cursor.close()
















