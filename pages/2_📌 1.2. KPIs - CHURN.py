
# ========================
# Cargando las Librerías: 
# ========================
import streamlit as st
import pandas as pd
# from pandas_profiling import ProfileReport
import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
# from numerize.numerize import numerize
from numerize import numerize
import time
from streamlit_extras.metric_cards import style_metric_cards
# st.set_option('deprecation.showPyplotGlobalUse', False)
import plotly.graph_objs as go
import plotly.graph_objects as go
# ----------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
#from streamlit-aggrid import AgGrid, GridOptionsBuilder







# Descomenta esta línea si usas MySQL:
# from query import *

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
#st.header("MORBILIDAD:  Tratamiento Estadístico, KPI y Tendencias")




# Título general
st.markdown("""
<h1 style='text-align: center; color: #3A3A3A;'> Dashboard CHURN Donantes - UNICEF</h1>
""", unsafe_allow_html=True)



#  ------------------------------------------------------------





#-------------------------------------------------------------------------------
# Cargar y preparación de las fuentes de datos
#-------------------------------------------------------------------------------
# -------------------------------
# Tabla de Datos De Churn :
# -------------------------------



# =========================
# CARGAR DATA
# =========================
@st.cache_data
def load_data():
        return pd.read_excel("data/rfm_data.xlsx")
#       return pd.read_excel("C:/Users/cesar/OneDrive/Escritorio/UNICEF/Dashboard_CHURN/data/rfm_data.xlsx")
df = load_data()

df_sm0 = df
# -------------------------------------------------------------------------












#------------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA:



# Dataset sin filtros
df_filtrado = df_sm0.copy()



# SECCIÓN 1.1. : 
# INTRODUCCION A CHURN:
# --------------------------
#st.markdown("##")


#st.header("CHURN")
#st.write("La morbilidad es la frecuencia o proporción de personas que presentan una enfermedad o condición específica dentro de una población determinada. Desde un enfoque estadístico, el análisis de la morbilidad permite identificar patrones, tendencias y distribuciones geográficas o demográficas de las enfermedades, lo cual es clave para la planificación en salud pública.  \n Mediante indicadores como el número de casos absolutos, la tasa de morbilidad (por cada 10.000 habitantes) o la prevalencia y la incidencia, se pueden evaluar los grupos más afectados, detectar zonas de mayor vulnerabilidad y priorizar recursos. Estas métricas también permiten comparar el comportamiento de enfermedades a lo largo del tiempo o entre regiones, facilitando la toma de decisiones basadas en evidencia.  El análisis estadístico de la morbilidad es, por tanto, una herramienta fundamental para monitorear el estado de salud de una población, y diseñar intervenciones efectivas.") 











# ---------------------------------------------------------------------------
# Sección de Filtrado:
# -------------------

st.subheader("Indicadores Clave de CHURN")

# ---------------------------------------------------------------------------
# Sección de Filtros – Ocultos pero definidos por defecto
# ---------------------------------------------------------------------------

# 🧩 Valores por defecto para los filtros (sin mostrarlos)
Ciudades = df_sm0['City'].dropna().unique().tolist()
Canal = df_sm0['Channel'].dropna().unique().tolist()


# ✅ DataFrame filtrado (en este caso sin aplicar restricciones)
df_selection = df_sm0[
    (df_sm0['City'].isin(Ciudades)) &
    (df_sm0['Channel'].isin(Canal))
]

# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Filtros visibles para el usuario, pero aún no se aplican
#Departamento = st.multiselect("Selecciona Departamento", df_sm0['departamento'].dropna().unique())
#Municipio = st.multiselect("Selecciona Municipio", df_sm0['municipio'].dropna().unique())
#Grupo = st.multiselect("Selecciona Grupo", df_sm0['grupo'].dropna().unique())

df_selection = df_sm0.copy()  # No se filtra todavía


# ----------------------------------------------------------------------------
# Asignación directa sin filtros interactivos
df_selection = df_sm0.copy()



# Secciones del dashboard
#if selected == "📊 KPI":

st.subheader("KPIs")
# calcular los Indicadores Clave de Morbilidad:
total_donantes = float(pd.Series(df_selection['Churn']).count())
total_Churn = float(pd.Series(df_selection['Churn']).sum())
Churn_Rate = float(pd.Series(df_selection['Churn']).mean())
CLV_Medio = float(pd.Series(df_selection['CLV_model']).mean())
investment_mode1 = float(pd.Series(df_selection['City']).nunique())
investment_mode2 = float(pd.Series(df_selection['Channel']).nunique())





# CSS personalizado
st.markdown("""
    <style>
    /* Reducir tamaño del metric */
    div[data-testid="stMetric"] {
        text-align: center;
        font-size: 14px;
    }

    /* Reducir tamaño del valor principal */
    div[data-testid="stMetricValue"] {
        font-size: 18px;
    }

    /* Centrar texto de st.info */
    div[data-testid="stAlert"] {
        text-align: center;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Layout
# -------------------------
# =========================
# FILA 1 (3 tarjetas)
# =========================
col1, col2, col3 = st.columns(3)

with col1: 
    st.info('Periods', icon="📆") 
    st.metric(label="Cohorte", value="2024-1 - 2024-12")

with col2:
    st.info('Tot. Cities.', icon="📍")
    st.metric(label="Tot. Ciudades.", value=f"{investment_mode1:,.0f}")

with col3:
    st.info('Channels.', icon="📡")  #🌐
    st.metric(label="Tot. Canal", value=f"{investment_mode2:,.0f}")



st.markdown("##")   # SALTO


# =========================
# FILA 2 (4 tarjetas)
# =========================
col4, col5, col6, col7 = st.columns(4)

with col4:
    st.info('Donors', icon="🧑‍🤝‍🧑")
    st.metric(label="Tot. Donantes", value=f"{total_donantes:,.0f}".replace(",", "."))

with col5:
    st.info('Tot. Churn', icon="⚠️")
    st.metric(label="Tot. Abandono", value=f"{total_Churn:,.0f}".replace(",", "."))

with col6:
    st.info('Churn Rate', icon="📉")
    st.metric(label="Tasa de Abandono", value=f"{Churn_Rate:.2%}")


# ---------------------------
def formatear_moneda_cop(valor):
    if valor >= 1_000_000:
        return f"${valor/1_000_000:,.2f} Mill"
    elif valor >= 1_000:
        return f"${valor/1_000:,.2f} K"
    else:
        return f"${valor:,.0f}"
# -----------------------------


with col7:
    st.info('Avg. CLV Medio', icon="🎯")
    st.metric(label="CLV Medio", value=formatear_moneda_cop(CLV_Medio))

#------------------------------------------------------------------------------







# ----------------------------------------------------------------------

# 4. Crear la tabla cruzada sumando la columna 'cant' 

# ---------------------------------------------------------------------





st.markdown("##")   # SALTO






# ---------------------------------------------------------------------


    
# ------------------------------------------------------------------------
# GRÁFICO CIRCULAR DE SUBSECTORES:
# ---------------------------------

st.markdown("<h4 style='color:#547FD4; font-weight:bold;'>Tasa de Cancelación por Ciudad y Canal </h4>", unsafe_allow_html=True) 
st.write("Da click en uno de las Ciudades (en el centro del gráfico) para desplegar estadísticas") 




# =====================================
# TITULO Y ESTILO DEL ENCABEZADO:
st.set_page_config(page_title="Dashboard ", page_icon="📈", layout="wide")  
#st.header("Resumen Gráfico Exploratorio Multidimensional")
 
# Cargar CSS si existe el archivo
try:
    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Archivo style.css no encontrado. Continuando sin estilos personalizados.")

# LLAMANDO EL DATAFRAME:
try:
    # Importando la tabla agregada con los resúmenes de las variables:
    df_subsectores = pd.read_excel('data/TablaCHURN_Subsectores.xlsx', sheet_name='Hoja1')
    df_subsectores["poblacion"] = round(df_subsectores["poblacion"], 0)
    df_subsectores["conteos"] = round(df_subsectores["conteos"], 0)
    df_subsectores["tasas"] = round(df_subsectores["tasas"], 1) 

    
    # Estructura jerárquica: City > Ciudades > Totales
    labels = df_subsectores['labels'].tolist()
    parents = df_subsectores['parents'].tolist()
    poblacion = df_subsectores['poblacion'].tolist()
    conteos = df_subsectores['conteos'].tolist()
    tasas = df_subsectores['tasas'].tolist()
    
    # Etiquetas personalizadas con conteo y tasa
    custom_labels = [f"{l}<br>Donors: {d:,.0f}<br>Churn: {v:,.0f}<br>Tasa: {t*100:.1f}%".replace(',', '.') if v != 0 else l 
                 for l, d, v, t in zip(labels, poblacion, conteos, tasas)]
    
    # Sunburst plot
    #colors = ['#2A3180', '#39A8E0', '#F28F1C', '#E5352B', '#662681', '#009640', '#9D9D9C']
    fig = go.Figure(go.Sunburst(
        labels=custom_labels,
        parents=parents,
        values=conteos,
        branchvalues="remainder" #,  # ahora los padres no necesitan tener suma directa
        #marker=dict(colors=colors * (len(labels) // len(colors) + 1))  # Repetir colores si son necesarios
    ))
    
    # Agregando el Titulo (Elegante)
    fig.update_layout(
        title={
            "text": "Tasa de Churn por Ciudad y Departamento",
            "y": 0.95, 
            "x": 0.5, 
            "xanchor": "center", 
            "yanchor": "top", 
            "font": dict(size=24, color="black")
        }, 
        margin=dict(t=80, l=10, r=10, b=10)
    )
    
    
    
    # ¡AQUÍ ESTÁ LA LÍNEA QUE FALTABA!
    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
except FileNotFoundError:
    st.error("Archivo 'TablaMorbilidad_Subsectores.xlsx' no encontrado. Verifica que el archivo esté en el directorio correcto.")
except Exception as e:
    st.error(f"Error al cargar los datos: {str(e)}")
    
 

# ---------------------------------------------------------------------




    
# ------------------------------------------------------------------------







# ===========================
# Mapa Leaflet de CHURN
# ---------------------------



















