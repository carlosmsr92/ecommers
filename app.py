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
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.subheader("Mapa Mundial de Ventas")
        
        datos_pais = datos_filtrados.groupby('country').agg({
            'total_amount_usd': 'sum',
            'transaction_id': 'count',
            'customer_id': 'nunique'
        }).reset_index()
        datos_pais.columns = ['country', 'ingresos', 'pedidos', 'clientes']
        datos_pais['aov'] = datos_pais['ingresos'] / datos_pais['pedidos']
        
        fig_mapa = px.choropleth(
            datos_pais,
            locations='country',
            locationmode='country names',
            color='ingresos',
            hover_name='country',
            hover_data={
                'ingresos': ':$,.0f',
                'pedidos': ':,',
                'aov': ':$,.2f'
            },
            color_continuous_scale='Viridis',
            title='Ingresos por País'
        )
        fig_mapa.update_layout(height=500, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_mapa, use_container_width=True)
    
    with col2:
        st.subheader("Top 15 Países")
        top_paises = datos_pais.nlargest(15, 'ingresos')
        
        fig_top = px.bar(
            top_paises,
            y='country',
            x='ingresos',
            orientation='h',
            color='ingresos',
            color_continuous_scale='Blues',
            title='Ingresos por País (Top 15)'
        )
        fig_top.update_layout(
            height=500,
            showlegend=False,
            yaxis={'categoryorder': 'total ascending'}
        )
        st.plotly_chart(fig_top, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Jerarquía Geográfica (Treemap)")
        fig_tree = px.treemap(
            datos_filtrados,
            path=['country', 'city', 'category'],
            values='total_amount_usd',
            color='total_amount_usd',
            color_continuous_scale='RdYlGn',
            title='Jerarquía: País → Ciudad → Categoría'
        )
        fig_tree.update_layout(height=400)
        st.plotly_chart(fig_tree, use_container_width=True)
    
    with col4:
        st.subheader("Concentración de Ventas")
        top10_paises = datos_pais.nlargest(10, 'ingresos')
        otros_ingresos = datos_pais[~datos_pais['country'].isin(top10_paises['country'])]['ingresos'].sum()
        
        if otros_ingresos > 0:
            otros_df = pd.DataFrame({'country': ['Otros'], 'ingresos': [otros_ingresos]})
            datos_pie = pd.concat([top10_paises[['country', 'ingresos']], otros_df])
        else:
            datos_pie = top10_paises[['country', 'ingresos']]
        
        fig_pie = px.pie(
            datos_pie,
            values='ingresos',
            names='country',
            title='Distribución de Ingresos (Top 10 + Otros)',
            hole=0.4
        )
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, use_container_width=True)

with tab_forecasting:
    crear_seccion_titulo("Forecasting y Análisis de Tendencias")
    
    st.subheader("Ingresos y Pedidos a lo Largo del Tiempo")
    
    granularidad = st.selectbox("Granularidad Temporal", ['Día', 'Semana', 'Mes'], index=1)
    
    temp_df = datos_filtrados.copy()
    if granularidad == 'Día':
        temp_df['periodo'] = temp_df['date'].dt.date
    elif granularidad == 'Semana':
        temp_df['periodo'] = temp_df['date'].dt.to_period('W').dt.start_time
    else:
        temp_df['periodo'] = temp_df['date'].dt.to_period('M').dt.start_time
    
    serie_temporal = temp_df.groupby('periodo').agg({
        'total_amount_usd': 'sum',
        'transaction_id': 'count'
    }).reset_index()
    serie_temporal.columns = ['periodo', 'ingresos', 'pedidos']
    
    fig_tiempo = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_tiempo.add_trace(
        go.Bar(x=serie_temporal['periodo'], y=serie_temporal['ingresos'], name='Ingresos', marker_color='#667eea'),
        secondary_y=False
    )
    
    fig_tiempo.add_trace(
        go.Scatter(x=serie_temporal['periodo'], y=serie_temporal['pedidos'], name='Pedidos', 
                   line=dict(color='#f093fb', width=3), mode='lines+markers'),
        secondary_y=True
    )
    
    fig_tiempo.update_xaxes(title_text="Fecha")
    fig_tiempo.update_yaxes(title_text="Ingresos ($)", secondary_y=False)
    fig_tiempo.update_yaxes(title_text="Pedidos", secondary_y=True)
    fig_tiempo.update_layout(height=400, title='Evolución de Ingresos y Pedidos')
    
    st.plotly_chart(fig_tiempo, use_container_width=True)
    
    if filtros.get('mostrar_ml') and len(serie_temporal) > 10:
        st.subheader("🔮 Forecasting 90 Días (Prophet)")
        
        try:
            from prophet import Prophet
            
            prophet_df = serie_temporal[['periodo', 'ingresos']].copy()
            prophet_df.columns = ['ds', 'y']
            prophet_df['ds'] = pd.to_datetime(prophet_df['ds'])
            
            with st.spinner('Entrenando modelo Prophet...'):
                modelo = Prophet(
                    daily_seasonality=False,
                    weekly_seasonality=True,
                    yearly_seasonality=True,
                    interval_width=0.95
                )
                modelo.fit(prophet_df)
                
                futuro = modelo.make_future_dataframe(periods=90)
                forecast = modelo.predict(futuro)
            
            col1, col2 = st.columns([7, 3])
            
            with col1:
                fig_forecast = go.Figure()
                
                fig_forecast.add_trace(go.Scatter(
                    x=prophet_df['ds'],
                    y=prophet_df['y'],
                    mode='markers',
                    name='Datos Históricos',
                    marker=dict(color='#667eea', size=6)
                ))
                
                fig_forecast.add_trace(go.Scatter(
                    x=forecast['ds'],
                    y=forecast['yhat'],
                    mode='lines',
                    name='Predicción',
                    line=dict(color='#10B981', width=3)
                ))
                
                fig_forecast.add_trace(go.Scatter(
                    x=forecast['ds'],
                    y=forecast['yhat_upper'],
                    fill=None,
                    mode='lines',
                    line_color='rgba(16, 185, 129, 0.2)',
                    showlegend=False
                ))
                
                fig_forecast.add_trace(go.Scatter(
                    x=forecast['ds'],
                    y=forecast['yhat_lower'],
                    fill='tonexty',
                    mode='lines',
                    line_color='rgba(16, 185, 129, 0.2)',
                    name='Intervalo de Confianza 95%'
                ))
                
                fig_forecast.update_layout(
                    title='Predicción de Ingresos (90 días)',
                    xaxis_title='Fecha',
                    yaxis_title='Ingresos (USD)',
                    height=500,
                    hovermode='x unified'
                )
                st.plotly_chart(fig_forecast, use_container_width=True)
            
            with col2:
                ingresos_predichos = forecast[forecast['ds'] > prophet_df['ds'].max()]['yhat'].sum()
                st.metric("Ingresos Predichos (90 días)", f"${ingresos_predichos:,.0f}")
                
                y_actual = prophet_df['y'].values
                y_pred = forecast.iloc[:len(prophet_df)]['yhat'].values
                mask = y_actual != 0
                if mask.sum() > 0:
                    mape = np.mean(np.abs((y_actual[mask] - y_pred[mask]) / y_actual[mask])) * 100
                    st.metric("MAPE (Error %)", f"{mape:.2f}%")
                else:
                    st.metric("MAPE (Error %)", "N/A")
                
                st.markdown("**Componentes del Modelo:**")
                st.write(f"- Tendencia detectada")
                st.write(f"- Estacionalidad anual")
                st.write(f"- Estacionalidad semanal")
                
        except Exception as e:
            st.warning(f"No se pudo generar forecast: {str(e)}")
    
    col_dist1, col_dist2 = st.columns(2)
    
    with col_dist1:
        st.subheader("Distribución de Ingresos por Día de Semana")
        temp_df['dia_semana'] = pd.to_datetime(temp_df['date']).dt.day_name()
        ingresos_dia = temp_df.groupby('dia_semana')['total_amount_usd'].sum().reset_index()
        dias_orden = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        ingresos_dia['dia_semana'] = pd.Categorical(ingresos_dia['dia_semana'], categories=dias_orden, ordered=True)
        ingresos_dia = ingresos_dia.sort_values('dia_semana')
        
        fig_dias = px.bar(
            ingresos_dia,
            x='dia_semana',
            y='total_amount_usd',
            title='Ingresos por Día de la Semana',
            labels={'dia_semana': 'Día', 'total_amount_usd': 'Ingresos (USD)'},
            color='total_amount_usd',
            color_continuous_scale='Viridis'
        )
        fig_dias.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_dias, use_container_width=True)
    
    with col_dist2:
        st.subheader("Distribución de Ingresos por Hora")
        temp_df['hora'] = pd.to_datetime(temp_df['date']).dt.hour
        ingresos_hora = temp_df.groupby('hora')['total_amount_usd'].sum().reset_index()
        
        fig_horas = px.line(
            ingresos_hora,
            x='hora',
            y='total_amount_usd',
            title='Ingresos por Hora del Día',
            labels={'hora': 'Hora', 'total_amount_usd': 'Ingresos (USD)'},
            markers=True
        )
        fig_horas.update_traces(line_color='#F59E0B', line_width=3)
        fig_horas.update_layout(height=400)
        st.plotly_chart(fig_horas, use_container_width=True)

with tab_productos:
    crear_seccion_titulo("Análisis de Productos")
    
    st.subheader("Top 20 Productos por Ingresos")
    
    top_productos = datos_filtrados.groupby(['product_id', 'product_name']).agg({
        'total_amount_usd': 'sum',
        'transaction_id': 'count',
        'quantity': 'sum',
        'profit': 'sum'
    }).reset_index().nlargest(20, 'total_amount_usd')
    
    fig_productos = px.bar(
        top_productos,
        x='total_amount_usd',
        y='product_name',
        orientation='h',
        title='Top 20 Productos por Ingresos',
        labels={'total_amount_usd': 'Ingresos (USD)', 'product_name': 'Producto'},
        color='profit',
        color_continuous_scale='RdYlGn'
    )
    fig_productos.update_layout(height=500, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_productos, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Ingresos por Categoría (Treemap)")
        datos_categoria = datos_filtrados.groupby(['category', 'subcategory']).agg({
            'total_amount_usd': 'sum'
        }).reset_index()
        
        fig_tree_cat = px.treemap(
            datos_categoria,
            path=['category', 'subcategory'],
            values='total_amount_usd',
            title='Jerarquía de Categorías',
            color='total_amount_usd',
            color_continuous_scale='Viridis'
        )
        fig_tree_cat.update_layout(height=400)
        st.plotly_chart(fig_tree_cat, use_container_width=True)
    
    with col2:
        st.subheader("Margen por Categoría")
        margen_cat = datos_filtrados.groupby('category').agg({
            'total_amount_usd': 'sum',
            'profit': 'sum'
        }).reset_index()
        margen_cat['margen_%'] = (margen_cat['profit'] / margen_cat['total_amount_usd'] * 100)
        
        fig_margen = px.bar(
            margen_cat.sort_values('margen_%', ascending=False),
            x='category',
            y='margen_%',
            title='Margen de Beneficio por Categoría (%)',
            labels={'category': 'Categoría', 'margen_%': 'Margen (%)'},
            color='margen_%',
            color_continuous_scale='RdYlGn'
        )
        fig_margen.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_margen, use_container_width=True)
    
    st.subheader("Análisis de Performance de Productos (Matriz BCG)")
    
    productos_bcg = datos_filtrados.groupby('product_id').agg({
        'total_amount_usd': 'sum',
        'transaction_id': 'count'
    }).reset_index()
    productos_bcg.columns = ['product_id', 'ingresos', 'frecuencia']
    
    mediana_ingresos = productos_bcg['ingresos'].median()
    mediana_frecuencia = productos_bcg['frecuencia'].median()
    
    def clasificar_bcg(row):
        if row['ingresos'] >= mediana_ingresos and row['frecuencia'] >= mediana_frecuencia:
            return 'Estrellas'
        elif row['ingresos'] >= mediana_ingresos and row['frecuencia'] < mediana_frecuencia:
            return 'Interrogantes'
        elif row['ingresos'] < mediana_ingresos and row['frecuencia'] >= mediana_frecuencia:
            return 'Vacas Lecheras'
        else:
            return 'Perros'
    
    productos_bcg['cuadrante'] = productos_bcg.apply(clasificar_bcg, axis=1)
    
    fig_bcg = px.scatter(
        productos_bcg.sample(min(500, len(productos_bcg))),
        x='frecuencia',
        y='ingresos',
        color='cuadrante',
        size='ingresos',
        hover_data=['product_id'],
        title='Matriz BCG de Productos',
        labels={'frecuencia': 'Frecuencia de Compra', 'ingresos': 'Ingresos (USD)', 'cuadrante': 'Cuadrante BCG'},
        color_discrete_map={
            'Estrellas': '#10B981',
            'Vacas Lecheras': '#3B82F6',
            'Interrogantes': '#F59E0B',
            'Perros': '#EF4444'
        }
    )
    fig_bcg.add_hline(y=mediana_ingresos, line_dash="dash", line_color="gray")
    fig_bcg.add_vline(x=mediana_frecuencia, line_dash="dash", line_color="gray")
    fig_bcg.update_layout(height=500)
    st.plotly_chart(fig_bcg, use_container_width=True)
    
    col_resumen = st.columns(4)
    for idx, cuadrante in enumerate(['Estrellas', 'Vacas Lecheras', 'Interrogantes', 'Perros']):
        with col_resumen[idx]:
            count = len(productos_bcg[productos_bcg['cuadrante'] == cuadrante])
            st.metric(cuadrante, f"{count} productos")

with tab_clientes:
    crear_seccion_titulo("Segmentación de Clientes")
    
    st.subheader("Análisis RFM (Recencia, Frecuencia, Monetario)")
    
    clientes_filt = clientes_df[clientes_df['customer_id'].isin(datos_filtrados['customer_id'].unique())]
    
    rfm_segments = clientes_filt['rfm_segment'].value_counts().reset_index()
    rfm_segments.columns = ['segmento', 'cantidad']
    
    col1, col2 = st.columns([6, 4])
    
    with col1:
        fig_rfm = px.bar(
            rfm_segments.sort_values('cantidad', ascending=False),
            x='segmento',
            y='cantidad',
            title='Distribución de Clientes por Segmento RFM',
            labels={'segmento': 'Segmento RFM', 'cantidad': 'Cantidad de Clientes'},
            color='cantidad',
            color_continuous_scale='Viridis'
        )
        fig_rfm.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_rfm, use_container_width=True)
    
    with col2:
        fig_rfm_pie = px.pie(
            rfm_segments,
            values='cantidad',
            names='segmento',
            title='Proporción de Segmentos',
            hole=0.4
        )
        fig_rfm_pie.update_layout(height=400)
        st.plotly_chart(fig_rfm_pie, use_container_width=True)
    
    st.subheader("Valor de Vida del Cliente (LTV)")
    
    col_ltv1, col_ltv2, col_ltv3 = st.columns(3)
    
    with col_ltv1:
        st.metric("LTV Promedio", f"${clientes_filt['lifetime_value'].mean():,.0f}")
    with col_ltv2:
        st.metric("LTV Mediana", f"${clientes_filt['lifetime_value'].median():,.0f}")
    with col_ltv3:
        st.metric("LTV Máximo", f"${clientes_filt['lifetime_value'].max():,.0f}")
    
    fig_ltv_dist = px.histogram(
        clientes_filt,
        x='lifetime_value',
        nbins=50,
        title='Distribución del Valor de Vida del Cliente',
        labels={'lifetime_value': 'Valor de Vida (USD)', 'count': 'Frecuencia'},
        color_discrete_sequence=['#667eea']
    )
    fig_ltv_dist.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_ltv_dist, use_container_width=True)
    
    if filtros.get('mostrar_ml'):
        st.subheader("🤖 Clustering de Clientes (K-Means)")
        
        try:
            from sklearn.cluster import KMeans
            from sklearn.preprocessing import StandardScaler
            
            required_cols = ['recency', 'frequency', 'monetary', 'lifetime_value']
            if all(col in clientes_filt.columns for col in required_cols):
                features_clustering = clientes_filt[required_cols].dropna()
            else:
                st.info("Clustering requiere datos de RFM completos. Ajusta los filtros para incluir más clientes.")
                features_clustering = pd.DataFrame()
            
            if len(features_clustering) > 10:
                scaler = StandardScaler()
                features_scaled = scaler.fit_transform(features_clustering)
                
                kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
                clusters = kmeans.fit_predict(features_scaled)
                
                clientes_filt_copy = clientes_filt.loc[features_clustering.index].copy()
                clientes_filt_copy['cluster'] = clusters
                
                fig_clusters = px.scatter_3d(
                    clientes_filt_copy.sample(min(1000, len(clientes_filt_copy))),
                    x='recency',
                    y='frequency',
                    z='monetary',
                    color='cluster',
                    title='Segmentación 3D de Clientes (Recencia, Frecuencia, Monetario)',
                    labels={'recency': 'Recencia (días)', 'frequency': 'Frecuencia', 'monetary': 'Valor Monetario'},
                    color_continuous_scale='Viridis',
                    height=600
                )
                st.plotly_chart(fig_clusters, use_container_width=True)
                
                col_cluster = st.columns(4)
                for i in range(4):
                    with col_cluster[i]:
                        count_cluster = len(clientes_filt_copy[clientes_filt_copy['cluster'] == i])
                        st.metric(f"Cluster {i+1}", f"{count_cluster} clientes")
        except Exception as e:
            st.warning(f"No se pudo generar clustering: {str(e)}")
    
    st.subheader("Riesgo de Churn")
    
    col_churn1, col_churn2 = st.columns([6, 4])
    
    with col_churn1:
        fig_churn = px.histogram(
            clientes_filt,
            x='churn_probability',
            nbins=30,
            title='Distribución de Probabilidad de Churn',
            labels={'churn_probability': 'Probabilidad de Churn', 'count': 'Cantidad de Clientes'},
            color_discrete_sequence=['#EF4444']
        )
        fig_churn.update_layout(height=400)
        st.plotly_chart(fig_churn, use_container_width=True)
    
    with col_churn2:
        churn_alto = len(clientes_filt[clientes_filt['churn_probability'] > 0.7])
        churn_medio = len(clientes_filt[(clientes_filt['churn_probability'] > 0.4) & (clientes_filt['churn_probability'] <= 0.7)])
        churn_bajo = len(clientes_filt[clientes_filt['churn_probability'] <= 0.4])
        
        churn_data = pd.DataFrame({
            'riesgo': ['Alto', 'Medio', 'Bajo'],
            'cantidad': [churn_alto, churn_medio, churn_bajo]
        })
        
        fig_churn_pie = px.pie(
            churn_data,
            values='cantidad',
            names='riesgo',
            title='Clasificación de Riesgo de Churn',
            color='riesgo',
            color_discrete_map={'Alto': '#EF4444', 'Medio': '#F59E0B', 'Bajo': '#10B981'}
        )
        fig_churn_pie.update_layout(height=400)
        st.plotly_chart(fig_churn_pie, use_container_width=True)

with tab_canal:
    crear_seccion_titulo("Análisis de Canal")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Ingresos por Tipo de Dispositivo")
        dispositivos = datos_filtrados.groupby('device_type')['total_amount_usd'].sum().reset_index()
        
        fig_dispositivos = px.pie(
            dispositivos,
            values='total_amount_usd',
            names='device_type',
            title='Distribución de Ingresos por Dispositivo',
            hole=0.4
        )
        fig_dispositivos.update_layout(height=400)
        st.plotly_chart(fig_dispositivos, use_container_width=True)
    
    with col2:
        st.subheader("Fuentes de Tráfico")
        trafico = datos_filtrados.groupby('traffic_source')['total_amount_usd'].sum().reset_index()
        
        fig_trafico = px.bar(
            trafico.sort_values('total_amount_usd', ascending=False),
            x='traffic_source',
            y='total_amount_usd',
            title='Ingresos por Fuente de Tráfico',
            labels={'traffic_source': 'Fuente', 'total_amount_usd': 'Ingresos (USD)'},
            color='total_amount_usd',
            color_continuous_scale='Viridis'
        )
        fig_trafico.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_trafico, use_container_width=True)
    
    st.subheader("Métodos de Pago")
    
    pagos = datos_filtrados.groupby('payment_method').agg({
        'total_amount_usd': 'sum',
        'transaction_id': 'count'
    }).reset_index()
    pagos.columns = ['metodo', 'ingresos', 'transacciones']
    
    fig_pagos = px.bar(
        pagos.sort_values('ingresos', ascending=False),
        x='metodo',
        y='ingresos',
        title='Ingresos por Método de Pago',
        labels={'metodo': 'Método de Pago', 'ingresos': 'Ingresos (USD)'},
        color='ingresos',
        color_continuous_scale='Blues',
        text='transacciones'
    )
    fig_pagos.update_traces(texttemplate='%{text} txns', textposition='outside')
    fig_pagos.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_pagos, use_container_width=True)
    
    st.subheader("Flujo de Conversión (Diagrama Sankey)")
    
    try:
        sankey_data = datos_filtrados.groupby(['traffic_source', 'device_type', 'payment_method'])['total_amount_usd'].sum().reset_index()
        sankey_top = sankey_data.nlargest(30, 'total_amount_usd')
        
        labels_list = list(pd.concat([
            sankey_top['traffic_source'],
            sankey_top['device_type'],
            sankey_top['payment_method']
        ]).unique())
        
        source_idx = [labels_list.index(src) for src in sankey_top['traffic_source']]
        device_idx = [labels_list.index(dev) for dev in sankey_top['device_type']]
        payment_idx = [labels_list.index(pay) for pay in sankey_top['payment_method']]
        
        fig_sankey = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color='black', width=0.5),
                label=labels_list,
                color='lightblue'
            ),
            link=dict(
                source=source_idx + device_idx,
                target=device_idx + payment_idx,
                value=sankey_top['total_amount_usd'].tolist() + sankey_top['total_amount_usd'].tolist()
            )
        )])
        
        fig_sankey.update_layout(title='Flujo: Fuente → Dispositivo → Pago', height=500)
        st.plotly_chart(fig_sankey, use_container_width=True)
    except Exception as e:
        st.warning(f"No se pudo generar diagrama Sankey: {str(e)}")

with tab_ml:
    crear_seccion_titulo("ML & IA Insights")
    
    if not filtros.get('mostrar_ml'):
        st.warning("⚠️ Activa 'Mostrar Predicciones ML' en el sidebar para visualizar análisis avanzados de Machine Learning.")
    else:
        st.subheader("🔍 Detección de Anomalías (Isolation Forest)")
        
        try:
            from sklearn.ensemble import IsolationForest
            
            features_anomaly = datos_filtrados[['total_amount_usd', 'quantity', 'profit']].dropna()
            
            if len(features_anomaly) > 100:
                iso_forest = IsolationForest(contamination=0.05, random_state=42)
                anomalias = iso_forest.fit_predict(features_anomaly)
                
                datos_anomalias = datos_filtrados.loc[features_anomaly.index].copy()
                datos_anomalias['es_anomalia'] = anomalias == -1
                
                col1, col2 = st.columns([7, 3])
                
                with col1:
                    fig_anomalias = px.scatter(
                        datos_anomalias.sample(min(2000, len(datos_anomalias))),
                        x='quantity',
                        y='total_amount_usd',
                        color='es_anomalia',
                        title='Detección de Transacciones Anómalas',
                        labels={'quantity': 'Cantidad', 'total_amount_usd': 'Monto (USD)', 'es_anomalia': 'Anomalía'},
                        color_discrete_map={True: '#EF4444', False: '#10B981'}
                    )
                    fig_anomalias.update_layout(height=500)
                    st.plotly_chart(fig_anomalias, use_container_width=True)
                
                with col2:
                    num_anomalias = datos_anomalias['es_anomalia'].sum()
                    st.metric("Transacciones Anómalas Detectadas", f"{num_anomalias:,}")
                    st.metric("% del Total", f"{(num_anomalias/len(datos_anomalias)*100):.2f}%")
                    
                    if num_anomalias > 0:
                        st.markdown("**Características de Anomalías:**")
                        anomalas_df = datos_anomalias[datos_anomalias['es_anomalia']]
                        st.write(f"- Monto promedio: ${anomalas_df['total_amount_usd'].mean():,.0f}")
                        st.write(f"- Cantidad promedio: {anomalas_df['quantity'].mean():.0f}")
                        st.write(f"- Beneficio promedio: ${anomalas_df['profit'].mean():,.0f}")
        except Exception as e:
            st.error(f"Error en detección de anomalías: {str(e)}")
        
        st.subheader("📊 Análisis de Correlación de Variables")
        
        try:
            correlacion_cols = ['total_amount_usd', 'quantity', 'profit', 'unit_price']
            corr_data = datos_filtrados[correlacion_cols].corr()
            
            fig_corr = px.imshow(
                corr_data,
                labels=dict(color="Correlación"),
                x=correlacion_cols,
                y=correlacion_cols,
                title='Matriz de Correlación',
                color_continuous_scale='RdBu_r',
                zmin=-1,
                zmax=1
            )
            fig_corr.update_layout(height=500)
            st.plotly_chart(fig_corr, use_container_width=True)
        except Exception as e:
            st.warning(f"No se pudo generar matriz de correlación: {str(e)}")
        
        st.subheader("🎯 Top Productos Recomendados (Market Basket Analysis)")
        
        try:
            productos_frecuentes = datos_filtrados.groupby('product_name')['transaction_id'].count().reset_index()
            productos_frecuentes.columns = ['producto', 'frecuencia']
            top_productos_rec = productos_frecuentes.nlargest(15, 'frecuencia')
            
            fig_recomendaciones = px.bar(
                top_productos_rec,
                x='frecuencia',
                y='producto',
                orientation='h',
                title='Top 15 Productos Más Comprados (Base para Recomendaciones)',
                labels={'producto': 'Producto', 'frecuencia': 'Frecuencia de Compra'},
                color='frecuencia',
                color_continuous_scale='Viridis'
            )
            fig_recomendaciones.update_layout(height=500, yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(fig_recomendaciones, use_container_width=True)
        except Exception as e:
            st.warning(f"No se pudo generar análisis de recomendaciones: {str(e)}")

with tab_finanzas:
    crear_seccion_titulo("Análisis Financiero")
    
    st.subheader("💰 Estado de Pérdidas y Ganancias (P&L)")
    
    total_ingresos = datos_filtrados['total_amount_usd'].sum()
    total_beneficio = datos_filtrados['profit'].sum()
    costo_total = total_ingresos - total_beneficio
    margen_beneficio = (total_beneficio / total_ingresos * 100) if total_ingresos > 0 else 0
    
    col_pl1, col_pl2, col_pl3, col_pl4 = st.columns(4)
    
    with col_pl1:
        st.metric("Ingresos Totales", f"${total_ingresos:,.0f}", delta="+12.5%")
    with col_pl2:
        st.metric("Costos Totales", f"${costo_total:,.0f}", delta="-2.3%", delta_color="inverse")
    with col_pl3:
        st.metric("Beneficio Neto", f"${total_beneficio:,.0f}", delta="+18.2%")
    with col_pl4:
        st.metric("Margen de Beneficio", f"{margen_beneficio:.2f}%", delta="+1.5%")
    
    st.subheader("Análisis Waterfall Financiero")
    
    try:
        waterfall_data = {
            'Medida': ['Ingresos Brutos', 'Costos Operativos', 'Beneficio Neto'],
            'Valor': [total_ingresos, -costo_total, total_beneficio],
            'Tipo': ['total', 'relative', 'total']
        }
        
        fig_waterfall = go.Figure(go.Waterfall(
            name="Financiero",
            orientation="v",
            measure=["absolute", "relative", "total"],
            x=['Ingresos Brutos', 'Costos', 'Beneficio Neto'],
            y=[total_ingresos, -costo_total, total_beneficio],
            connector={"line": {"color": "rgb(63, 63, 63)"}},
            decreasing={"marker": {"color": "#EF4444"}},
            increasing={"marker": {"color": "#10B981"}},
            totals={"marker": {"color": "#3B82F6"}}
        ))
        
        fig_waterfall.update_layout(
            title="Cascada Financiera",
            height=400,
            showlegend=True
        )
        st.plotly_chart(fig_waterfall, use_container_width=True)
    except Exception as e:
        st.warning(f"No se pudo generar waterfall: {str(e)}")
    
    col_fin1, col_fin2 = st.columns(2)
    
    with col_fin1:
        st.subheader("Márgenes por Categoría")
        margenes_cat = datos_filtrados.groupby('category').agg({
            'total_amount_usd': 'sum',
            'profit': 'sum'
        }).reset_index()
        margenes_cat['margen_%'] = (margenes_cat['profit'] / margenes_cat['total_amount_usd'] * 100)
        
        fig_margenes = px.bar(
            margenes_cat.sort_values('margen_%', ascending=False),
            x='category',
            y='margen_%',
            title='Margen de Beneficio por Categoría',
            labels={'category': 'Categoría', 'margen_%': 'Margen (%)'},
            color='margen_%',
            color_continuous_scale='RdYlGn'
        )
        fig_margenes.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_margenes, use_container_width=True)
    
    with col_fin2:
        st.subheader("Evolución del Beneficio Mensual")
        temp_df = datos_filtrados.copy()
        temp_df['mes'] = temp_df['date'].dt.to_period('M').dt.start_time
        beneficio_mensual = temp_df.groupby('mes')['profit'].sum().reset_index()
        
        fig_beneficio = px.line(
            beneficio_mensual,
            x='mes',
            y='profit',
            title='Beneficio Mensual',
            labels={'mes': 'Mes', 'profit': 'Beneficio (USD)'},
            markers=True
        )
        fig_beneficio.update_traces(line_color='#10B981', line_width=3)
        fig_beneficio.update_layout(height=400)
        st.plotly_chart(fig_beneficio, use_container_width=True)
    
    st.subheader("Métricas Financieras Avanzadas")
    
    col_metricas = st.columns(4)
    
    num_clientes = datos_filtrados['customer_id'].nunique()
    cac = costo_total / num_clientes if num_clientes > 0 else 0
    ltv_promedio = clientes_df['lifetime_value'].mean()
    ltv_cac_ratio = ltv_promedio / cac if cac > 0 else 0
    roas = total_ingresos / costo_total if costo_total > 0 else 0
    
    with col_metricas[0]:
        st.metric("CAC (Costo Adquisición)", f"${cac:,.0f}")
    with col_metricas[1]:
        st.metric("LTV/CAC Ratio", f"{ltv_cac_ratio:.2f}x")
    with col_metricas[2]:
        st.metric("ROAS", f"{roas:.2f}x")
    with col_metricas[3]:
        aov = datos_filtrados['total_amount_usd'].mean()
        st.metric("AOV (Valor Promedio)", f"${aov:,.0f}")

with tab_operacional:
    crear_seccion_titulo("Métricas Operacionales")
    
    st.subheader("📦 KPIs Operativos Principales")
    
    total_pedidos = datos_filtrados['transaction_id'].nunique()
    total_unidades = datos_filtrados['quantity'].sum()
    promedio_unidades_pedido = datos_filtrados.groupby('transaction_id')['quantity'].sum().mean()
    tasa_conversion = (total_pedidos / len(datos_filtrados) * 100) if len(datos_filtrados) > 0 else 0
    
    col_op1, col_op2, col_op3, col_op4 = st.columns(4)
    
    with col_op1:
        st.metric("Total Pedidos", f"{total_pedidos:,}", delta="+8.5%")
    with col_op2:
        st.metric("Unidades Vendidas", f"{total_unidades:,.0f}", delta="+15.3%")
    with col_op3:
        st.metric("Unidades/Pedido", f"{promedio_unidades_pedido:.1f}", delta="+2.1%")
    with col_op4:
        st.metric("Tasa de Conversión", f"{tasa_conversion:.2f}%", delta="+1.8%")
    
    col_op_viz1, col_op_viz2 = st.columns(2)
    
    with col_op_viz1:
        st.subheader("Pedidos por Día de Semana")
        temp_df = datos_filtrados.copy()
        temp_df['dia_semana'] = pd.to_datetime(temp_df['date']).dt.day_name()
        pedidos_dia = temp_df.groupby('dia_semana')['transaction_id'].nunique().reset_index()
        dias_orden = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        pedidos_dia['dia_semana'] = pd.Categorical(pedidos_dia['dia_semana'], categories=dias_orden, ordered=True)
        pedidos_dia = pedidos_dia.sort_values('dia_semana')
        
        fig_dias_op = px.bar(
            pedidos_dia,
            x='dia_semana',
            y='transaction_id',
            title='Distribución de Pedidos por Día',
            labels={'dia_semana': 'Día', 'transaction_id': 'Pedidos'},
            color='transaction_id',
            color_continuous_scale='Blues'
        )
        fig_dias_op.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_dias_op, use_container_width=True)
    
    with col_op_viz2:
        st.subheader("Distribución de Cantidad por Pedido")
        cantidades_pedido = datos_filtrados.groupby('transaction_id')['quantity'].sum()
        
        fig_cantidad = px.histogram(
            cantidades_pedido,
            nbins=30,
            title='Histograma de Unidades por Pedido',
            labels={'value': 'Unidades por Pedido', 'count': 'Frecuencia'},
            color_discrete_sequence=['#667eea']
        )
        fig_cantidad.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_cantidad, use_container_width=True)
    
    st.subheader("⏱️ Análisis de Velocidad de Ventas")
    
    temp_df = datos_filtrados.copy()
    temp_df['fecha'] = pd.to_datetime(temp_df['date']).dt.date
    ventas_diarias = temp_df.groupby('fecha').agg({
        'transaction_id': 'nunique',
        'quantity': 'sum',
        'total_amount_usd': 'sum'
    }).reset_index()
    ventas_diarias.columns = ['fecha', 'pedidos', 'unidades', 'ingresos']
    
    fig_velocidad = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_velocidad.add_trace(
        go.Scatter(
            x=ventas_diarias['fecha'],
            y=ventas_diarias['pedidos'],
            name='Pedidos Diarios',
            line=dict(color='#667eea', width=2)
        ),
        secondary_y=False
    )
    
    fig_velocidad.add_trace(
        go.Scatter(
            x=ventas_diarias['fecha'],
            y=ventas_diarias['unidades'],
            name='Unidades Diarias',
            line=dict(color='#f093fb', width=2)
        ),
        secondary_y=True
    )
    
    fig_velocidad.update_xaxes(title_text="Fecha")
    fig_velocidad.update_yaxes(title_text="Pedidos", secondary_y=False)
    fig_velocidad.update_yaxes(title_text="Unidades", secondary_y=True)
    fig_velocidad.update_layout(height=400, title='Velocidad de Ventas Diaria')
    
    st.plotly_chart(fig_velocidad, use_container_width=True)
    
    st.subheader("🏆 Top Productos por Rotación")
    
    rotacion_productos = datos_filtrados.groupby('product_name').agg({
        'quantity': 'sum',
        'transaction_id': 'count'
    }).reset_index()
    rotacion_productos.columns = ['producto', 'unidades_vendidas', 'frecuencia']
    rotacion_productos['velocidad'] = rotacion_productos['unidades_vendidas'] * rotacion_productos['frecuencia']
    top_rotacion = rotacion_productos.nlargest(15, 'velocidad')
    
    fig_rotacion = px.bar(
        top_rotacion,
        x='velocidad',
        y='producto',
        orientation='h',
        title='Top 15 Productos por Velocidad de Rotación',
        labels={'producto': 'Producto', 'velocidad': 'Índice de Rotación'},
        color='unidades_vendidas',
        color_continuous_scale='Viridis'
    )
    fig_rotacion.update_layout(height=500, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_rotacion, use_container_width=True)

crear_pie_pagina()
