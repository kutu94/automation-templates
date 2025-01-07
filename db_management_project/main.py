from scripts.db_operations import listar_tabla, verificar_existencia, actualizar_precio, eliminar_registro
from scripts.data_loader import cargar_datos_desde_csv
from scripts.export_utils import exportar_a_pdf, exportar_a_csv
from scripts.db_connector import connect_to_database

def exportar_productos(connection):
    """Exporta los productos a PDF y CSV."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM productos")

    # Exportar a PDF
    print("\nExportando productos a 'productos_report.pdf'...")
    exportar_a_pdf(cursor, "output/productos_report.pdf")

    # Exportar a CSV
    print("\nExportando productos a 'productos_export.csv'...")
    exportar_a_csv(cursor, "output/productos_export.csv")

    cursor.close()


def main():
    # Conexión a la base de datos
    connection = connect_to_database()
    if not connection:
        print("No se pudo conectar a la base de datos.")
        return

    try:
        # 1. Listar registros de la tabla "productos"
        print("\nListando productos en la base de datos:")
        listar_tabla(connection, "productos")

        # 2. Actualizar precio de un producto
        print("\nActualizando precio del producto ID 1...")
        actualizar_precio(connection, producto_id=1, nuevo_precio=1500.00)

        # 3. Verificar existencia de un cliente
        print("\nVerificando si el cliente 'juan.perez@gmail.com' existe:")
        cliente_existe = verificar_existencia(connection, "clientes", "correo", "juan.perez@gmail.com")
        print(f"¿El cliente existe? {'Sí' if cliente_existe else 'No'}")

        # 4. Cargar datos desde un archivo CSV
        print("\nCargando datos desde archivo CSV a la tabla 'clientes'...")
        cargar_datos_desde_csv(connection, "data/example_data.csv", "clientes")

        # 5. Eliminar un producto
        print("\nEliminando producto con ID 2...")
        eliminar_registro(connection, "productos", "id", 2)

        # 6. Listar productos después de los cambios
        print("\nListando productos después de los cambios:")
        listar_tabla(connection, "productos")

        # Exportar productos a archivos
        exportar_productos(connection)

    finally:
        # Asegurarse de cerrar la conexión
        connection.close()
        print("\nConexión cerrada.")


if __name__ == "__main__":
    main()