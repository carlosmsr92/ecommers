"""
Componentes UI Reutilizables para Dashboard
Autor: cmsr92
"""

import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

PALETA_CORPORATIVA = {
    'primario': '#0F172A',
    'secundario': '#1E40AF',
    'acento': '#10B981',
    'acento2': '#F59E0B',
    'error': '#EF4444',
    'exito': '#10B981',
    'neutro': '#64748B',
    'fondo': '#F8FAFC',
}

def crear_tarjeta_kpi(icono, etiqueta, valor, cambio=None, formato='numero', col=None):
    """
    Crea una tarjeta KPI profesional
    
    Args:
        icono: Emoji del icono
        etiqueta: Texto descriptivo del KPI
        valor: Valor numérico del KPI
        cambio: Cambio porcentual vs periodo anterior (opcional)
        formato: 'numero', 'moneda', 'porcentaje'
        col: Columna de streamlit donde renderizar (opcional)
    """
    if formato == 'moneda':
        valor_formateado = f"${valor:,.0f}"
    elif formato == 'porcentaje':
        valor_formateado = f"{valor:.1f}%"
    else:
        valor_formateado = f"{valor:,}" if isinstance(valor, (int, float)) else str(valor)
    
    html_cambio = ""
    if cambio is not None:
        icono_tendencia = "📈" if cambio >= 0 else "📉"
        clase_cambio = "positivo" if cambio >= 0 else "negativo"
        html_cambio = f'''
        <div class="kpi-cambio {clase_cambio}">
            {icono_tendencia} {abs(cambio):.1f}% vs periodo anterior
        </div>
        '''
    
    html_kpi = f'''
    <div class="tarjeta-kpi">
        <div class="kpi-icono">{icono}</div>
        <div class="kpi-etiqueta">{etiqueta}</div>
        <div class="kpi-valor">{valor_formateado}</div>
        {html_cambio}
    </div>
    '''
    
    if col:
        col.markdown(html_kpi, unsafe_allow_html=True)
    else:
        st.markdown(html_kpi, unsafe_allow_html=True)

def crear_seccion_titulo(titulo, icono="📊"):
    """Crea un título de sección profesional"""
    st.markdown(f'<div class="seccion-titulo">{icono} {titulo}</div>', unsafe_allow_html=True)

def crear_header_principal(titulo, subtitulo):
    """Crea el header principal del dashboard"""
    st.markdown(f"""
    <div class="header-principal">
        <h1>{titulo}</h1>
        <p>{subtitulo}</p>
    </div>
    """, unsafe_allow_html=True)

def crear_pie_pagina():
    """Crea el pie de página con firma cmsr92"""
    st.markdown("""
    <div class="pie-pagina">
        <p>Dashboard Avanzado de Analytics Ecommerce Global</p>
        <p class="firma-autor">Desarrollado por cmsr92</p>
        <p style="font-size: 0.85rem; margin-top: 1rem;">
            © 2025 - Plataforma de Business Intelligence con Machine Learning e Inteligencia Artificial
        </p>
    </div>
    """, unsafe_allow_html=True)

def crear_metrica_comparativa(titulo, valor_actual, valor_anterior, formato='numero'):
    """Crea una métrica con comparación visual"""
    if formato == 'moneda':
        actual_str = f"${valor_actual:,.0f}"
        anterior_str = f"${valor_anterior:,.0f}"
    elif formato == 'porcentaje':
        actual_str = f"{valor_actual:.1f}%"
        anterior_str = f"{valor_anterior:.1f}%"
    else:
        actual_str = f"{valor_actual:,}"
        anterior_str = f"{valor_anterior:,}"
    
    if valor_anterior > 0:
        cambio = ((valor_actual - valor_anterior) / valor_anterior) * 100
        delta_str = f"{cambio:+.1f}%"
    else:
        delta_str = "N/A"
    
    st.metric(
        label=titulo,
        value=actual_str,
        delta=delta_str,
        delta_color="normal"
    )

def aplicar_estilos_globales():
    """Aplica los estilos CSS globales del dashboard"""
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
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
        
        .stSelectbox label, .stMultiSelect label, .stDateInput label, .stSlider label {{
            font-weight: 600;
            color: {PALETA_CORPORATIVA['primario']};
            font-size: 0.95rem;
        }}
        
        .tooltip-info {{
            font-size: 0.85rem;
            color: {PALETA_CORPORATIVA['neutro']};
            font-style: italic;
            margin-top: 0.25rem;
        }}
    </style>
    """, unsafe_allow_html=True)

def mostrar_info_dataset(num_transacciones, num_clientes, num_productos, fecha_min, fecha_max):
    """Muestra información resumida del dataset"""
    años = fecha_max.year - fecha_min.year + 1
    st.info(f"""
    📊 **Dataset Actual:** {num_transacciones:,} transacciones | {num_clientes:,} clientes | {num_productos:,} productos  
    📅 **Periodo:** {fecha_min.strftime('%d/%m/%Y')} - {fecha_max.strftime('%d/%m/%Y')} ({años} años)
    """)
