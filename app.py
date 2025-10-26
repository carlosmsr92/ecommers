"""
Dashboard Avanzado de Analytics Ecommerce Global
Autor: cmsr92
Versión: 2.0
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

from utils.ui_components import (
    aplicar_estilos_globales, crear_header_principal, crear_tarjeta_kpi,
    crear_seccion_titulo, crear_pie_pagina, mostrar_info_dataset
)
from utils.filtros import crear_filtros_sidebar, aplicar_filtros
from utils.data_loader_pg import load_or_generate_data

aplicar_estilos_globales()

@st.cache_resource
def cargar_datos():
    return load_or_generate_data()

transacciones_df, clientes_df, productos_df = cargar_datos()

if transacciones_df is None or clientes_df is None or productos_df is None:
    st.error("❌ Error al cargar los datos. Por favor recarga la página.")
    st.stop()

crear_header_principal(
    "📊 Analytics Ecommerce Global",
    "Plataforma Avanzada de Business Intelligence, Machine Learning y Análisis Predictivo"
)

filtros = crear_filtros_sidebar(transacciones_df)
datos_filtrados = aplicar_filtros(transacciones_df, filtros)

if len(datos_filtrados) == 0:
    st.warning("⚠️ No hay datos que coincidan con los filtros seleccionados. Ajusta los criterios de búsqueda.")
    st.stop()

tab_overview, tab_geografia, tab_forecasting, tab_productos, tab_clientes, tab_canal, tab_ml, tab_finanzas, tab_operacional = st.tabs([
    "🏠 Resumen General",
    "🌍 Análisis Geográfico",
    "📈 Forecasting & Tendencias",
    "📦 Análisis de Productos",
    "👥 Segmentación de Clientes",
    "📱 Análisis de Canal",
    "🤖 ML & IA Insights",
    "💰 Análisis Financiero",
    "⚙️ Métricas Operacionales"
])

with tab_overview:
    crear_seccion_titulo("Indicadores Clave de Rendimiento (KPIs)")
    
    ingresos_totales = datos_filtrados['total_amount_usd'].sum()
    pedidos_totales = len(datos_filtrados)
    ticket_promedio = datos_filtrados['total_amount_usd'].mean()
    beneficio_total = datos_filtrados['profit'].sum()
    clientes_unicos = datos_filtrados['customer_id'].nunique()
    margen_promedio = (beneficio_total / ingresos_totales * 100) if ingresos_totales > 0 else 0
    
    fecha_inicio_comparacion = filtros['fecha_inicio'] - (filtros['fecha_fin'] - filtros['fecha_inicio'])
    datos_periodo_anterior = transacciones_df[
        (transacciones_df['date'] >= pd.Timestamp(fecha_inicio_comparacion)) & 
        (transacciones_df['date'] < pd.Timestamp(filtros['fecha_inicio']))
    ]
    
    ingresos_anteriores = datos_periodo_anterior['total_amount_usd'].sum()
    cambio_ingresos = ((ingresos_totales - ingresos_anteriores) / ingresos_anteriores * 100) if ingresos_anteriores > 0 else 0
    
    pedidos_anteriores = len(datos_periodo_anterior)
    cambio_pedidos = ((pedidos_totales - pedidos_anteriores) / pedidos_anteriores * 100) if pedidos_anteriores > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)
    
    crear_tarjeta_kpi("💰", "Ingresos Totales", ingresos_totales, cambio_ingresos, "moneda", col1)
    crear_tarjeta_kpi("🛒", "Pedidos Totales", pedidos_totales, cambio_pedidos, "numero", col2)
    crear_tarjeta_kpi("🎯", "Ticket Promedio (AOV)", ticket_promedio, None, "moneda", col3)
    crear_tarjeta_kpi("💎", "Beneficio Total", beneficio_total, None, "moneda", col4)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col5, col6, col7, col8 = st.columns(4)
    
    crear_tarjeta_kpi("👥", "Clientes Únicos", clientes_unicos, None, "numero", col5)
    productos_unicos = datos_filtrados['product_id'].nunique()
    crear_tarjeta_kpi("📦", "Productos Vendidos", productos_unicos, None, "numero", col6)
    tasa_conversion = (clientes_unicos / pedidos_totales * 100) if pedidos_totales > 0 else 0
    crear_tarjeta_kpi("🎯", "Tasa de Conversión", tasa_conversion, None, "porcentaje", col7)
    items_promedio = datos_filtrados['quantity'].mean()
    crear_tarjeta_kpi("📊", "Items por Pedido", items_promedio, None, "numero", col8)
    
    crear_seccion_titulo("Evolución Temporal")
    
    datos_temporales = datos_filtrados.copy()
    datos_temporales['fecha'] = pd.to_datetime(datos_temporales['date'])
    datos_temporales_agrupados = datos_temporales.groupby(datos_temporales['fecha'].dt.date).agg({
        'total_amount_usd': 'sum',
        'transaction_id': 'count',
        'profit': 'sum'
    }).reset_index()
    datos_temporales_agrupados.columns = ['Fecha', 'Ingresos', 'Pedidos', 'Beneficio']
    
    fig_evolucion = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Ingresos y Beneficio Diarios', 'Volumen de Pedidos'),
        row_heights=[0.6, 0.4],
        vertical_spacing=0.12
    )
    
    fig_evolucion.add_trace(
        go.Scatter(
            x=datos_temporales_agrupados['Fecha'],
            y=datos_temporales_agrupados['Ingresos'],
            name='Ingresos',
            line=dict(color='#667eea', width=3),
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.2)'
        ),
        row=1, col=1
    )
    
    fig_evolucion.add_trace(
        go.Scatter(
            x=datos_temporales_agrupados['Fecha'],
            y=datos_temporales_agrupados['Beneficio'],
            name='Beneficio',
            line=dict(color='#10B981', width=3),
            fill='tozeroy',
            fillcolor='rgba(16, 185, 129, 0.2)'
        ),
        row=1, col=1
    )
    
    fig_evolucion.add_trace(
        go.Bar(
            x=datos_temporales_agrupados['Fecha'],
            y=datos_temporales_agrupados['Pedidos'],
            name='Pedidos',
            marker_color='#F59E0B'
        ),
        row=2, col=1
    )
    
    fig_evolucion.update_layout(
        height=600,
        showlegend=True,
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter', size=12)
    )
    
    fig_evolucion.update_xaxes(showgrid=True, gridcolor='rgba(0,0,0,0.05)')
    fig_evolucion.update_yaxes(showgrid=True, gridcolor='rgba(0,0,0,0.05)')
    
    st.plotly_chart(fig_evolucion, use_container_width=True)
    
    crear_seccion_titulo("Distribuciones Clave")
    
    col_dist1, col_dist2 = st.columns(2)
    
    with col_dist1:
        top_paises = datos_filtrados.groupby('country')['total_amount_usd'].sum().nlargest(10).reset_index()
        fig_paises = px.bar(
            top_paises,
            x='total_amount_usd',
            y='country',
            orientation='h',
            title='Top 10 Países por Ingresos',
            labels={'total_amount_usd': 'Ingresos (USD)', 'country': 'País'},
            color='total_amount_usd',
            color_continuous_scale='Viridis'
        )
        fig_paises.update_layout(
            showlegend=False,
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_paises, use_container_width=True)
    
    with col_dist2:
        por_categoria = datos_filtrados.groupby('category')['total_amount_usd'].sum().reset_index()
        fig_categorias = px.pie(
            por_categoria,
            values='total_amount_usd',
            names='category',
            title='Distribución de Ingresos por Categoría',
            color_discrete_sequence=px.colors.qualitative.Set3,
            hole=0.4
        )
        fig_categorias.update_layout(
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        fig_categorias.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_categorias, use_container_width=True)

with tab_geografia:
    crear_seccion_titulo("Análisis Geográfico Global")
    
    st.info("🗺️ Esta pestaña está en desarrollo. Próximamente: mapas interactivos, análisis por región y treemaps geográficos.")

with tab_forecasting:
    crear_seccion_titulo("Forecasting y Análisis de Tendencias")
    
    st.info("📈 Esta pestaña está en desarrollo. Próximamente: predicciones Prophet, análisis de estacionalidad y tendencias futuras.")

with tab_productos:
    crear_seccion_titulo("Análisis de Productos")
    
    st.info("📦 Esta pestaña está en desarrollo. Próximamente: matriz BCG, análisis de categorías y performance de productos.")

with tab_clientes:
    crear_seccion_titulo("Segmentación de Clientes")
    
    st.info("👥 Esta pestaña está en desarrollo. Próximamente: análisis RFM, clustering de clientes y análisis de cohortes.")

with tab_canal:
    crear_seccion_titulo("Análisis de Canal")
    
    st.info("📱 Esta pestaña está en desarrollo. Próximamente: análisis de dispositivos, fuentes de tráfico y métodos de pago.")

with tab_ml:
    crear_seccion_titulo("ML & IA Insights")
    
    st.info("🤖 Esta pestaña está en desarrollo. Próximamente: clustering avanzado, detección de anomalías y recomendaciones.")

with tab_finanzas:
    crear_seccion_titulo("Análisis Financiero")
    
    st.info("💰 Esta pestaña está en desarrollo. Próximamente: P&L, análisis de márgenes, waterfall financiero y métricas avanzadas.")

with tab_operacional:
    crear_seccion_titulo("Métricas Operacionales")
    
    st.info("⚙️ Esta pestaña está en desarrollo. Próximamente: KPIs operativos, eficiencia logística y análisis de inventario.")

crear_pie_pagina()
