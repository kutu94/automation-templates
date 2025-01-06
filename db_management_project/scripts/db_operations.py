import logging

#Validaciones y Manejo de Errores
def manejar_errores(func):
    def envoltura(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error en {func.__name__}: {e}")
    return envoltura

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
@manejar_errores
def listar_tabla(conn, table_name):
    """Lista todos los registros de una tabla."""
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        for row in cursor.fetchall():
            logging.info(row)
    except Exception as e:
        logging.error(f"Error al listar la tabla '{table_name}': {e}")
    finally:
        cursor.close()

@manejar_errores
def actualizar_precio(conn, producto_id, nuevo_precio):
    """Actualiza el precio de un producto en la tabla 'productos'."""
    try:
        cursor = conn.cursor()
        update_query = 'UPDATE productos SET precio = %s WHERE id = %s'
        cursor.execute(update_query, (nuevo_precio, producto_id))
        conn.commit()
        logging.info(f"Precio actualizado para el producto ID {producto_id}.")
    except Exception as e:
        logging.error(f"Error al actualizar el precio: {e}")
    finally:
        cursor.close()

@manejar_errores
def verificar_existencia(conn, table_name, column_name, value):
    """Verifica si un valor existe en una tabla."""
    try:
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = %s"
        cursor.execute(query, (value,))
        exists = cursor.fetchone()[0] > 0
        return exists
    except Exception as e:
        logging.error(f"Error al verificar existencia: {e}")
        return False
    finally:
        cursor.close()

@manejar_errores
def eliminar_registro(conn, table_name, column_name, value):
    """Elimina un registro de una tabla."""
    try:
        cursor = conn.cursor()
        delete_query = f"DELETE FROM {table_name} WHERE {column_name} = %s"
        cursor.execute(delete_query, (value,))
        conn.commit()
        logging.info(f"Registro eliminado de la tabla '{table_name}'.")
    except Exception as e:
        logging.error(f"Error al eliminar el registro: {e}")
    finally:
        cursor.close()
