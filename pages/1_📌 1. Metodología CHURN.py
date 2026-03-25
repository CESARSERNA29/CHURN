



# Cargando las Librerías: 
# ======================

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




# Descomenta esta línea si usas MySQL:
# from query import *

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
#st.header("MORBILIDAD:  Tratamiento Estadístico, KPI y Tendencias")



# Título general
st.markdown("""
<h1 style='text-align: center; color: #3A3A3A;'> CHURN Analysis: Tratamiento Analítico, KPIs y Tendencias</h1>
""", unsafe_allow_html=True)

st.markdown("##")

st.markdown("""
        <h3 style='text-align: center; color: #333333;'>CHURN Methodology: Tratamiento Analítico, KPI y Tendencias </h3>
        <hr style="height:2px;border-width:0;color:gray;background-color:gray">
    """, unsafe_allow_html=True)

st.markdown("""
        <div style="text-align: justify; font-size: 16px; color: #444444;">La lealtad del donante es el motor fundamental que sostiene la misión de UNICEF, especialmente en contextos donde la infancia enfrenta crisis por desigualdad, violencia o exclusión. Más allá de una transacción económica, el compromiso de un socio es un vínculo dinámico que permite a la organización desarrollar programas de largo plazo, enfrentar emergencias y transformar la realidad de miles de niños.
        
    \nEn el sector humanitario, el interés por estudiar el Churn (deserción) desde enfoques cuantitativos es una necesidad crítica. Factores globales como la inestabilidad económica, las crisis migratorias y los cambios en las prioridades de consumo han incrementado la volatilidad de los aportes. Entender por qué un donante decide interrumpir su ayuda no es solo una métrica de marketing, sino un imperativo para garantizar la continuidad de la asistencia en el territorio. 
    
    
    \nEn regiones de operación compleja como la Orinoquía colombiana, donde la dispersión geográfica y las barreras estructurales dificultan la presencia institucional, el análisis estadístico riguroso del comportamiento del donante se vuelve una herramienta estratégica. Los KPIs de retención y el análisis de tendencias nos permiten orientar esfuerzos de fidelización, optimizar recursos de captación y diseñar campañas de comunicación focalizadas que resuenen con la realidad local y el sentimiento del donante.
        
    
    """, unsafe_allow_html=True)






# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================

st.markdown("---")  # Otra línea si quieres enfatizarlo aún más
st.markdown(
    "<h3 style='text-align: center; color: #DC143C;'>En construcción (...)</h3>", 
    unsafe_allow_html=True
)

# LOGO
with st.container():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("CONSTRUCCION4.png", width=250)

st.markdown("---")

# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================




#  ------------------------------------------------------------







