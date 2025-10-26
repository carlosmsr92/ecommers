"""
Dashboard Avanzado de Analytics Ecommerce Global
Autor: cmsr92
Plataforma profesional de Business Intelligence con ML, IA y Análisis Predictivo
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from streamlit_folium import st_folium
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Analytics Ecommerce Global | cmsr92",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

PALETA_CORPORATIVA = {
    'primario': '#0F172A',
    'secundario': '#1E40AF',
    'acento': '#10B981',
    'acento2': '#F59E0B',
    'error': '#EF4444',
    'exito': '#10B981',
    'neutro': '#64748B',
    'fondo': '#F8FAFC',
    'gradiente1': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'gradiente2': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
    'gradiente3': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
    'gradiente4': 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
    'gradiente5': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
}

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {{
        font-family: 'Inter', sans-serif;
    }}
    
    .main {{
        background-color: {PALETA_CORPORATIVA['fondo']};
    }}
    
    .header-principal {{
        background: {PALETA_CORPORATIVA['gradiente1']};
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        text-align: center;
    }}
    
    .header-principal h1 {{
        color: white;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }}
    
    .header-principal p {{
        color: rgba(255,255,255,0.95);
        font-size: 1.1rem;
        margin-top: 0.5rem;
        font-weight: 300;
    }}
    
    .tarjeta-kpi {{
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-left: 4px solid {PALETA_CORPORATIVA['acento']};
        transition: transform 0.2s, box-shadow 0.2s;
        height: 100%;
    }}
    
    .tarjeta-kpi:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }}
    
    .kpi-icono {{
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }}
    
    .kpi-valor {{
        font-size: 2.2rem;
        font-weight: 700;
        color: {PALETA_CORPORATIVA['primario']};
        margin: 0.5rem 0;
    }}
    
    .kpi-etiqueta {{
        font-size: 0.9rem;
        color: {PALETA_CORPORATIVA['neutro']};
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    
    .kpi-cambio {{
        font-size: 0.85rem;
        margin-top: 0.5rem;
        padding: 0.25rem 0.5rem;
        border-radius: 6px;
        display: inline-block;
    }}
    
    .kpi-cambio.positivo {{
        background-color: rgba(16, 185, 129, 0.1);
        color: {PALETA_CORPORATIVA['exito']};
    }}
    
    .kpi-cambio.negativo {{
        background-color: rgba(239, 68, 68, 0.1);
        color: {PALETA_CORPORATIVA['error']};
    }}
    
    .seccion-titulo {{
        font-size: 1.8rem;
        font-weight: 700;
        color: {PALETA_CORPORATIVA['primario']};
        margin: 2.5rem 0 1.5rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 3px solid {PALETA_CORPORATIVA['acento']};
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }}
    
    .filtro-grupo {{
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }}
    
    .filtro-titulo {{
        font-size: 1.1rem;
        font-weight: 600;
        color: {PALETA_CORPORATIVA['primario']};
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        background-color: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }}
    
    .stTabs [data-baseweb="tab"] {{
        padding: 12px 24px;
        background-color: {PALETA_CORPORATIVA['fondo']};
        border-radius: 8px;
        font-weight: 600;
        color: {PALETA_CORPORATIVA['neutro']};
        border: 2px solid transparent;
        transition: all 0.3s;
    }}
    
    .stTabs [data-baseweb="tab"]:hover {{
        background-color: rgba(102, 126, 234, 0.1);
        border-color: {PALETA_CORPORATIVA['secundario']};
    }}
    
    .stTabs [aria-selected="true"] {{
        background: {PALETA_CORPORATIVA['gradiente1']} !important;
        color: white !important;
        border-color: transparent !important;
    }}
    
    .pie-pagina {{
        text-align: center;
        padding: 2rem;
        margin-top: 4rem;
        border-top: 2px solid #E5E7EB;
        color: {PALETA_CORPORATIVA['neutro']};
        font-size: 0.9rem;
    }}
    
    .firma-autor {{
        font-weight: 700;
        color: {PALETA_CORPORATIVA['secundario']};
        font-size: 1.1rem;
    }}
    
    .expander-filtros {{
        background: white;
        border-radius: 12px;
        border: 2px solid #E5E7EB;
    }}
    
    div[data-testid="stExpander"] {{
        background: white;
        border-radius: 12px;
        border: 2px solid #E5E7EB;
        margin-bottom: 1rem;
    }}
    
    div[data-testid="stExpander"] summary {{
        font-weight: 600;
        color: {PALETA_CORPORATIVA['primario']};
        font-size: 1.05rem;
    }}
    
    .stSelectbox label, .stMultiSelect label, .stDateInput label {{
        font-weight: 600;
        color: {PALETA_CORPORATIVA['primario']};
        font-size: 0.95rem;
    }}
</style>
""", unsafe_allow_html=True)

from utils.data_loader_pg import load_or_generate_data, filter_data, get_date_range_preset

@st.cache_resource
def cargar_datos():
    return load_or_generate_data()

print("Dashboard completo creado")
