import streamlit as st
import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from scripts.data_loader import cargar_datos_ventas, cargar_datos_inventario
from scripts.data_visualization import grafico_ventas_diarias, grafico_stock_productos

# Configuración del Dashboard
st.set_page_config(
    page_title="Dashboard Empresarial",
    layout="wide"
)

# Cargar Datos
ventas = cargar_datos_ventas('../data/ventas.csv')
inventario = cargar_datos_inventario('../data/inventario.csv')

# Título y descripción
st.title("Dashboard Empresarial")
st.write("Monitoree métricas clave de su negocio en tiempo real.")

# Sección de Ventas
st.header("📊 Ventas")
if ventas is not None:
    st.plotly_chart(grafico_ventas_diarias(ventas), use_container_width=True)
else:
    st.error("No se pudieron cargar los datos de ventas.")

# Sección de Inventario
st.header("📦 Inventario")
if inventario is not None:
    st.plotly_chart(grafico_stock_productos(inventario), use_container_width=True)
else:
    st.error("No se pudieron cargar los datos de inventario.")
