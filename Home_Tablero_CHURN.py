

# 📦 Cargando librerías necesarias
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards

# 🧭 Configurar la página
st.set_page_config(page_title="Dashboard CHURN Donantes - UNICEF", page_icon="📈", layout="wide")

# ===============================
# 📋 Menú lateral con navegación
with st.sidebar:
    selected = option_menu(
        menu_title="Menú Principal",
        options=["Inicio", "Análisis", "Datos"],
        icons=["house", "bar-chart", "table"],
        default_index=0
    )

# ======================================
# Nuevo comentario1
# Nuevo comentario2 

# 🏠 Página de inicio / presentación
if selected == "Inicio":
    st.markdown("<h2 style='text-align: center; color: #4B8BBE;'> Donnators Churn Analysis Dashboard with Location wise Risk Status</h1>", unsafe_allow_html=True)

    st.markdown("""
        <h3 style='text-align: center; color: #333333;'>Análisis exploratorio, y modelamiento del riesgo de abandono de donadores (2024 - 2025)</h3>
        <hr style="height:2px;border-width:0;color:gray;background-color:gray">
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: justify; font-size: 14px; color: #444444;">
        Esta herramienta de análisis de churn visualiza la distribución y las causas de abandono de los donantes 
        recurrentes a nivel nacional entre 2024 y 2025. El tablero facilita la comparación de métricas de lealtad 
        por departamento y canal de captación, permitiendo una toma de decisiones informada para reducir la pérdida 
        de recursos y optimizar el ciclo de vida del donante.
        </div>
    """, unsafe_allow_html=True)




    # ===============================
    
    st.markdown("##")
    #st.image("MENTAL2.png", width=200, caption="Observatorio de Salud Mental")
    #st.markdown("<h2 style='text-align: center;'>Observatorio de Salud Mental</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])  # crea 3 columnas (izq, centro, der) 
    with col2:     # usamos solo la columna del medio 
        st.image("Logo2_UNICEF.png", width=350) 
    #st.markdown("<h2 style='text-align: center;'>Observatorio de Salud Mental</h2>", unsafe_allow_html=True)
    
    
    st.markdown("##")
    
    
    
    
    
    
    
    # ===============================
    # 🔹 Recuadro elegante informativo
    st.markdown("""
    <div style="border: 2px solid #4B8BBE; padding: 20px; border-radius: 15px; background-color: #F5F5F5;">
        <h4 style="color: #4B8BBE;">🔎 ¿Qué encontrarás en este tablero?</h4>
        <ul style="color: #333333; font-size: 16px;">
            <li>Estadísticas por grupos</li>
            <li>Tendencias por ciudad o región</li>
            <li>Comparaciones por tasa ajustada</li>
            <li>Visualizaciones interactivas</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Otras páginas (dejar en blanco por ahora)
elif selected == "Análisis":
    st.markdown("🚧 Página en construcción: Aquí irán los gráficos analíticos...")

elif selected == "Datos":
    st.markdown("📄 Aquí podrás explorar los datos fuente...")





#st.sidebar.image("data/Logo_UNILLANOS.png",caption="")      # LOGO
st.sidebar.image("Logo1_UNICEF.png",caption="")            # LOGO













# PARA EJECUTAR EL DASHBOARD, CORRER LAS SIGUIENTES LÍNEAS EN C:
# Invoca la carpeta donde está ubicado el archivo:  --->

# cd C:\Users\cesar\Downloads\TABLERO_STREAMLIT_DASHBOARD\DASHBOARD_STREAMLIT_COMPLETO




# Invocando el archivo: ---->
# python streamlit_app.py (este comando no corrió... entonces ejecutar el siguiente: ----> )

# streamlit run Home_Tablero.py












# =================================================
# EJECUTARLO EN BASH:
# =================================================
# OJO, EL PYTHON 3.11.11 INSTALADO EN ESTE SPYDER, ESTÁ UBICADO AQUÍ:
# "C:\Users\cesar\AppData\Local\spyder-6\envs\spyder-runtime\python.exe"
    
# ENTONCES LA EJECUCIÓN DE ESTE STREAMLIT, SE DEBE HACER DE LA SIGUIENTE MANERA:
    
# cd C:\Users\cesar\OneDrive\Escritorio\UNICEF\Dashboard_CHURN
# "C:\Users\cesar\AppData\Local\spyder-6\envs\spyder-runtime\python.exe" -m streamlit run Home_Tablero_CHURN.py






















