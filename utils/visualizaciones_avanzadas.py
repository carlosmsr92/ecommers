"""
Utilidades de visualizaciones avanzadas para el dashboard
Autor: cmsr92
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

COLORES_PRIMARIOS = ['#667eea', '#764ba2', '#10B981', '#F59E0B', '#EF4444', '#3B82F6', '#8B5CF6', '#EC4899']
COLORES_VIRIDIS = px.colors.sequential.Viridis

def crear_tarjeta_kpi_html(icono, etiqueta, valor, cambio=None, formato='numero'):
    """Crea HTML para tarjeta KPI profesional"""
    if formato == 'moneda':
        valor_formateado = f"${valor:,.0f}"
    elif formato == 'porcentaje':
        valor_formateado = f"{valor:.1f}%"
    else:
        valor_formateado = f"{valor:,}"
    
    html_cambio = ""
    if cambio is not None:
        icono_tendencia = "📈" if cambio >= 0 else "📉"
        clase_cambio = "positivo" if cambio >= 0 else "negativo"
        html_cambio = f'''
        <div class="kpi-cambio {clase_cambio}">
            {icono_tendencia} {abs(cambio):.1f}% vs periodo anterior
        </div>
        '''
    
    return f'''
    <div class="tarjeta-kpi">
        <div class="kpi-icono">{icono}</div>
        <div class="kpi-etiqueta">{etiqueta}</div>
        <div class="kpi-valor">{valor_formateado}</div>
        {html_cambio}
    </div>
    '''

def crear_grafico_evolucion_temporal(datos, columna_fecha, columna_valor, titulo, color='#667eea'):
    """Crea gráfico de evolución temporal con área"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=datos[columna_fecha],
        y=datos[columna_valor],
        mode='lines',
        name=titulo,
        line=dict(color=color, width=3),
        fill='tozeroy',
        fillcolor=f'rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.2)'
    ))
    
    fig.update_layout(
        title=titulo,
        xaxis_title="Fecha",
        yaxis_title="Valor",
        height=400,
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter', size=12)
    )
    
    fig.update_xaxes(showgrid=True, gridcolor='rgba(0,0,0,0.05)')
    fig.update_yaxes(showgrid=True, gridcolor='rgba(0,0,0,0.05)')
    
    return fig

def crear_heatmap_correlacion(datos, titulo="Matriz de Correlación"):
    """Crea heatmap de correlación"""
    columnas_numericas = datos.select_dtypes(include=[np.number]).columns
    correlacion = datos[columnas_numericas].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=correlacion.values,
        x=correlacion.columns,
        y=correlacion.columns,
        colorscale='RdBu',
        zmid=0,
        text=correlacion.values.round(2),
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Correlación")
    ))
    
    fig.update_layout(
        title=titulo,
        height=500,
        font=dict(family='Inter', size=11)
    )
    
    return fig

def crear_treemap(datos, path, values, titulo="Treemap Jerárquico"):
    """Crea treemap jerárquico"""
    fig = px.treemap(
        datos,
        path=path,
        values=values,
        title=titulo,
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        height=500,
        font=dict(family='Inter', size=12)
    )
    
    return fig

def crear_sunburst(datos, path, values, titulo="Diagrama Sunburst"):
    """Crea diagrama sunburst"""
    fig = px.sunburst(
        datos,
        path=path,
        values=values,
        title=titulo,
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        height=600,
        font=dict(family='Inter', size=12)
    )
    
    return fig

def crear_grafico_waterfall(categorias, valores, titulo="Análisis Waterfall"):
    """Crea gráfico waterfall (cascada)"""
    fig = go.Figure(go.Waterfall(
        name="",
        orientation="v",
        measure=["relative"] * (len(categorias) - 1) + ["total"],
        x=categorias,
        y=valores,
        connector={"line": {"color": "rgb(63, 63, 63)"}},
    ))
    
    fig.update_layout(
        title=titulo,
        showlegend=False,
        height=500,
        font=dict(family='Inter', size=12)
    )
    
    return fig

def crear_grafico_sankey(source, target, value, labels, titulo="Flujo Sankey"):
    """Crea diagrama de Sankey"""
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color=COLORES_PRIMARIOS
        ),
        link=dict(
            source=source,
            target=target,
            value=value
        )
    )])
    
    fig.update_layout(
        title=titulo,
        height=600,
        font=dict(family='Inter', size=12)
    )
    
    return fig

def crear_grafico_radar(categorias, valores, nombres_series, titulo="Análisis Radar"):
    """Crea gráfico radar"""
    fig = go.Figure()
    
    for i, (valores_serie, nombre) in enumerate(zip(valores, nombres_series)):
        fig.add_trace(go.Scatterpolar(
            r=valores_serie,
            theta=categorias,
            fill='toself',
            name=nombre,
            line_color=COLORES_PRIMARIOS[i % len(COLORES_PRIMARIOS)]
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max([max(v) for v in valores])]
            )
        ),
        showlegend=True,
        title=titulo,
        height=500,
        font=dict(family='Inter', size=12)
    )
    
    return fig
