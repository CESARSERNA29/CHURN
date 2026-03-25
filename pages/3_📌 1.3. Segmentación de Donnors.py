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
# ----------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np





# Descomenta esta línea si usas MySQL:
# from query import *

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
#st.header("MORTALIDAD:  Tratamiento Estadístico, KPI y Tendencias")



# Título general
st.markdown("""
<h1 style='text-align: center; color: #3A3A3A;'> Segmentación de Donnors: Clusters, KPIs y Tendencias</h1>
""", unsafe_allow_html=True)

st.write("")



st.markdown("""
        <div style="text-align: justify; font-size: 18px; color: #444444;">A continuación se presenta un análisis gráfico de segmentación de Donnors discriminados a partir del CLV (TLV) y la propensión al Churn.  Con ello se plantea una segmentación cartesiana del siguiente estilo.
          
    """, unsafe_allow_html=True)



st.markdown("##")
    
    
    
#  ------------------------------------------------------------

st.markdown("---")  # Otra línea si quieres enfatizarlo aún más
# Matriz
st.markdown(
    "<h3 style='text-align: center; color: #3A3A3A;'>Matriz de Segmentación Estratégica</h3>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,2.5,1])

with col2:
    st.image("Figure_3Matriz.png", use_container_width=True)

st.markdown("---")



st.markdown("##")





#-------------------------------------------------------------------------------
# Cargar y preparación de las fuentes de datos
#-------------------------------------------------------------------------------
# -------------------------------
# Tabla de Datos para Segmentar:
# -------------------------------

# =========================
# CARGAR DATA
# =========================
# --------------------------------
# Tabla de Datos para Mortalidad:
# --------------------------------

@st.cache_data
def load_data():
#        return pd.read_excel("data/rfm_data.xlsx")
        return pd.read_excel("C:/Users/cesar/OneDrive/Escritorio/UNICEF/Dashboard_CHURN/data/rfm_data.xlsx")
df = load_data()


# -------------------------------------------------------------------------


# BASE DE DATOS:
# ----------------
# Aplicar filtros:
# ----------------
df_filtrado = df.copy()

# -----------------------------




    




# ===========================
# 1. FILTROS (ANTES DE TODO)
# ===========================
# FILTROS
# ==========================
city = st.sidebar.multiselect("Ciudad", df['City'].unique())
channel = st.sidebar.multiselect("Canal", df['Channel'].unique())

df_filtrado = df.copy()

if city:
    df_filtrado = df_filtrado[df_filtrado['City'].isin(city)]

if channel:
    df_filtrado = df_filtrado[df_filtrado['Channel'].isin(channel)]
    



# =======================
# 2. CORTES Y CUADRANTES
# =======================
# Transformado las escalas por el sesgo excesivo:
df_filtrado["CLV_pct"] = df_filtrado["CLV_model"].rank(pct=True)
df_filtrado["churn_pct"] = df_filtrado["churn_probability"].rank(pct=True)

# Version 2:
# Transformaciones
df_filtrado["CLV_plot"] = np.log1p(df_filtrado["CLV_model"])
df_filtrado["churn_plot"] = df_filtrado["churn_probability"] ** 0.5



# CORTES: 
# --------
#clv_cut = df_filtrado['CLV_model'].median()
#clv_cut = 300000000

#churn_cut = df_filtrado['churn_probability'].median()
#churn_cut = 0.10

# Cortes según la transformación de la escala... por el sesgo:
clv_cut = df_filtrado["CLV_plot"].median()
churn_cut = df_filtrado["churn_plot"].median()




# Cuadrantes:
# -----------
q1 = df_filtrado[(df_filtrado["CLV_plot"] < clv_cut) & (df_filtrado["churn_plot"] >= churn_cut)]
q2 = df_filtrado[(df_filtrado["CLV_plot"] >= clv_cut) & (df_filtrado["churn_plot"] >= churn_cut)]
q3 = df_filtrado[(df_filtrado["CLV_plot"] < clv_cut) & (df_filtrado["churn_plot"] < churn_cut)]
q4 = df_filtrado[(df_filtrado["CLV_plot"] >= clv_cut) & (df_filtrado["churn_plot"] < churn_cut)]



st.markdown("##")




# ============================
# 3. KPIs (AHORA SÍ DINÁMICOS)
# ============================
col1, col2, col3, col4 = st.columns(4)

with col2:
    st.metric("🟡 Interv. Ligera", len(q1))

with col3:
    st.metric("🔴 Máx. Prioridad", len(q2))

with col1:
    st.metric("⚪ Monit. Pasivo", len(q3))

with col4:
    st.metric("🟢 Fidelización", len(q4))
    
    
    
st.markdown("##")




    

# ======================
# 4. GRÁFICO (CORREGIDO)
# ======================


import plotly.express as px

fig = go.Figure()

colors = px.colors.qualitative.Set2
channels = df_filtrado["Channel"].unique()

for i, ch in enumerate(channels):
    df_ch = df_filtrado[df_filtrado["Channel"] == ch]

    fig.add_trace(go.Scatter(
#       x=df_ch["CLV_model"],
#       y=df_ch["churn_probability"],
        x=df_ch["CLV_plot"], y=df_ch["churn_plot"],
        mode='markers',
        name=ch,  #  leyenda por canal
        marker=dict(
            size=np.sqrt(df_ch["Monetary"]) / 2,
            color=colors[i % len(colors)],
            opacity=0.7
        ),
        text=df_ch["donor_id"],
        hovertemplate="<b>%{text}</b><br>CLV: %{x}<br>Churn: %{y}<extra></extra>"
    ))



# Líneas de cuadrantes
fig.add_vline(x=clv_cut, line_dash="dash", line_color="gray")
fig.add_hline(y=churn_cut, line_dash="dash", line_color="gray")

# Fondos
#fig.add_shape(...)




# Escala log en X
#fig.update_xaxes(type="log")



# Recorte para evitar compresión
fig.update_yaxes(range=[0, df_filtrado["churn_probability"].quantile(0.95)])



# LABELS FINALES:
fig.update_layout(
    title="Matriz de priorización de intervención",
    xaxis_title="CLV (escala log)",
    yaxis_title="Probabilidad de churn",
    legend_title="Canal",
    plot_bgcolor="white"
)


# ======================
# GRÁFICO (ARRIBA)
# ======================
st.plotly_chart(fig, use_container_width=True)

st.markdown("##")




# ===============================
# 5. TABLAS (AHORA SÍ CORRECTAS)
# ===============================

def tabla_top(df, titulo):
    
    with st.expander(f"{titulo} (Total: {len(df)})"):
        
        df_show = df.sort_values("CLV_model", ascending=False)[
            ["donor_id", "CLV_model", "churn_probability"]
        ]

        # Formato
        df_show["CLV_model"] = df_show["CLV_model"].apply(lambda x: f"${x:,.0f}")
        df_show["churn_probability"] = df_show["churn_probability"].apply(lambda x: f"{x:.1%}")

        st.dataframe(
            df_show,
            height=300,  # 👈 scroll interno
            use_container_width=True
        )




# Mostrar tablas:
tabla_top(q3, "⚪ Monit. Pasivo")
tabla_top(q1, "🟡 Interv. Ligera")
tabla_top(q2, "🔴 Máx. Prioridad")
tabla_top(q4, "🟢 Fidelización")















































