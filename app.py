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

# Configuración de página
st.set_page_config(
    page_title="Global Ecommerce Analytics Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E40AF;
        text-align: center;
        padding: 1rem 0;
        border-bottom: 3px solid #10B981;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    .kpi-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .kpi-change {
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1E40AF;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #E5E7EB;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: #F3F4F6;
        border-radius: 5px 5px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# Importar funciones
from utils.data_loader import load_or_generate_data, filter_data, get_date_range_preset

# Cargar datos
@st.cache_resource
def load_data():
    return load_or_generate_data()

transactions_df, customers_df, products_df = load_data()

# Header
st.markdown('<div class="main-header">🌍 Global Ecommerce Analytics Platform</div>', unsafe_allow_html=True)

# Sidebar - Filtros
st.sidebar.header("📊 Filtros de Análisis")

# Selector de periodo
date_preset = st.sidebar.selectbox(
    "Periodo",
    ['Last 7 Days', 'Last 30 Days', 'Last 90 Days', 'Last Year', 'All Time']
)
start_date, end_date = get_date_range_preset(date_preset)

# Filtros adicionales
st.sidebar.markdown("---")
st.sidebar.subheader("🌍 Geografía")
all_countries = sorted(transactions_df['country'].unique())
selected_countries = st.sidebar.multiselect("Países", all_countries, default=all_countries[:5])

st.sidebar.subheader("📦 Productos")
all_categories = sorted(transactions_df['category'].unique())
selected_categories = st.sidebar.multiselect("Categorías", all_categories, default=all_categories)

st.sidebar.subheader("👥 Clientes")
all_segments = sorted(transactions_df['customer_segment'].unique())
selected_segments = st.sidebar.multiselect("Segmentos", all_segments, default=all_segments)

st.sidebar.subheader("💳 Transacciones")
all_payment_methods = sorted(transactions_df['payment_method'].unique())
selected_payment = st.sidebar.multiselect("Métodos de Pago", all_payment_methods, default=all_payment_methods)

all_devices = sorted(transactions_df['device_type'].unique())
selected_devices = st.sidebar.multiselect("Dispositivos", all_devices, default=all_devices)

all_traffic = sorted(transactions_df['traffic_source'].unique())
selected_traffic = st.sidebar.multiselect("Fuente de Tráfico", all_traffic, default=all_traffic)

price_range = st.sidebar.slider(
    "Rango de Precio ($)",
    float(transactions_df['unit_price'].min()),
    float(transactions_df['unit_price'].max()),
    (float(transactions_df['unit_price'].min()), float(transactions_df['unit_price'].max()))
)

show_ml_predictions = st.sidebar.checkbox("🤖 Mostrar Predicciones ML", value=True)

# Aplicar filtros
filters = {
    'date_range': (start_date, end_date),
    'countries': selected_countries if selected_countries else all_countries,
    'categories': selected_categories if selected_categories else all_categories,
    'segments': selected_segments if selected_segments else all_segments,
    'payment_methods': selected_payment if selected_payment else all_payment_methods,
    'device_types': selected_devices if selected_devices else all_devices,
    'traffic_sources': selected_traffic if selected_traffic else all_traffic,
    'price_range': price_range
}

filtered_df = filter_data(transactions_df, filters)

# Información de actualización
st.sidebar.markdown("---")
st.sidebar.info(f"📅 Última actualización: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
st.sidebar.success(f"📊 {len(filtered_df):,} transacciones seleccionadas")

# KPIs Principales
st.markdown('<div class="section-header">📈 KPIs Principales</div>', unsafe_allow_html=True)

# Calcular métricas actuales
current_revenue = filtered_df['total_amount_usd'].sum()
current_orders = len(filtered_df)
current_aov = filtered_df['total_amount_usd'].mean()
current_profit = filtered_df['profit'].sum()
current_customers = filtered_df['customer_id'].nunique()
current_conversion = (current_orders / max(current_customers, 1)) * 100

# Calcular métricas periodo anterior para comparación
prev_start = start_date - (end_date - start_date)
prev_end = start_date
prev_df = transactions_df[(transactions_df['date'] >= prev_start) & (transactions_df['date'] < prev_end)]
prev_df = filter_data(prev_df, {k: v for k, v in filters.items() if k != 'date_range'})

prev_revenue = prev_df['total_amount_usd'].sum() if len(prev_df) > 0 else 1
prev_orders = len(prev_df) if len(prev_df) > 0 else 1
prev_aov = prev_df['total_amount_usd'].mean() if len(prev_df) > 0 else 1
prev_profit = prev_df['profit'].sum() if len(prev_df) > 0 else 1

# Calcular cambios
revenue_change = ((current_revenue - prev_revenue) / prev_revenue * 100) if prev_revenue > 0 else 0
orders_change = ((current_orders - prev_orders) / prev_orders * 100) if prev_orders > 0 else 0
aov_change = ((current_aov - prev_aov) / prev_aov * 100) if prev_aov > 0 else 0
profit_change = ((current_profit - prev_profit) / prev_profit * 100) if prev_profit > 0 else 0

# Mostrar KPIs
kpi_cols = st.columns(4)

with kpi_cols[0]:
    st.metric(
        "💰 Total Revenue",
        f"${current_revenue/1e6:.2f}M",
        f"{revenue_change:+.1f}%",
        delta_color="normal"
    )

with kpi_cols[1]:
    st.metric(
        "📦 Total Orders",
        f"{current_orders:,}",
        f"{orders_change:+.1f}%",
        delta_color="normal"
    )

with kpi_cols[2]:
    st.metric(
        "🛒 Avg Order Value",
        f"${current_aov:.2f}",
        f"{aov_change:+.1f}%",
        delta_color="normal"
    )

with kpi_cols[3]:
    st.metric(
        "💵 Gross Profit",
        f"${current_profit/1e6:.2f}M",
        f"{profit_change:+.1f}%",
        delta_color="normal"
    )

kpi_cols2 = st.columns(4)

with kpi_cols2[0]:
    st.metric(
        "👥 Total Customers",
        f"{current_customers:,}",
        f"New: {len(filtered_df[filtered_df['customer_segment'] == 'Recent Customers']):,}"
    )

with kpi_cols2[1]:
    st.metric(
        "📊 Conversion Rate",
        f"{current_conversion:.2f}%",
        f"{current_conversion - 2.5:+.2f}pp"
    )

with kpi_cols2[2]:
    ltv = customers_df['lifetime_value'].mean()
    st.metric(
        "💎 Customer LTV",
        f"${ltv:.0f}",
        f"Median: ${customers_df['lifetime_value'].median():.0f}"
    )

with kpi_cols2[3]:
    churn_rate = customers_df['churn_probability'].mean() * 100
    st.metric(
        "⚠️ Churn Rate",
        f"{churn_rate:.1f}%",
        f"{-1.2:+.1f}%",
        delta_color="inverse"
    )

# Tabs para diferentes secciones
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🌍 Análisis Geoespacial",
    "📈 Forecasting & Tendencias",
    "🛍️ Análisis de Productos",
    "👥 Segmentación de Clientes",
    "🤖 ML Insights",
    "📊 Tablas Detalladas"
])

# TAB 1: Análisis Geoespacial
with tab1:
    st.markdown('<div class="section-header">🌍 Análisis Geoespacial</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.subheader("Mapa Mundial de Ventas")
        
        # Agrupar por país
        country_data = filtered_df.groupby('country').agg({
            'total_amount_usd': 'sum',
            'transaction_id': 'count',
            'customer_id': 'nunique'
        }).reset_index()
        country_data.columns = ['country', 'revenue', 'orders', 'customers']
        country_data['aov'] = country_data['revenue'] / country_data['orders']
        
        # Crear mapa choropleth
        fig_map = px.choropleth(
            country_data,
            locations='country',
            locationmode='country names',
            color='revenue',
            hover_name='country',
            hover_data={
                'revenue': ':$,.0f',
                'orders': ':,',
                'aov': ':$,.2f'
            },
            color_continuous_scale='Viridis',
            title='Revenue por País'
        )
        fig_map.update_layout(height=500, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_map, use_container_width=True)
    
    with col2:
        st.subheader("Top 15 Países")
        top_countries = country_data.nlargest(15, 'revenue')
        
        fig_top = px.bar(
            top_countries,
            y='country',
            x='revenue',
            orientation='h',
            color='revenue',
            color_continuous_scale='Blues',
            title='Revenue por País (Top 15)'
        )
        fig_top.update_layout(
            height=500,
            showlegend=False,
            yaxis={'categoryorder': 'total ascending'}
        )
        st.plotly_chart(fig_top, use_container_width=True)
    
    # Row 2: Treemap y Donut
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Revenue by Region (Treemap)")
        fig_tree = px.treemap(
            filtered_df,
            path=['country', 'city', 'category'],
            values='total_amount_usd',
            color='total_amount_usd',
            color_continuous_scale='RdYlGn',
            title='Jerarquía: País → Ciudad → Categoría'
        )
        fig_tree.update_layout(height=400)
        st.plotly_chart(fig_tree, use_container_width=True)
    
    with col4:
        st.subheader("Sales Concentration")
        top10_countries = country_data.nlargest(10, 'revenue')
        others_revenue = country_data[~country_data['country'].isin(top10_countries['country'])]['revenue'].sum()
        
        if others_revenue > 0:
            others_df = pd.DataFrame({'country': ['Others'], 'revenue': [others_revenue]})
            pie_data = pd.concat([top10_countries[['country', 'revenue']], others_df])
        else:
            pie_data = top10_countries[['country', 'revenue']]
        
        fig_pie = px.pie(
            pie_data,
            values='revenue',
            names='country',
            title='Distribución de Revenue (Top 10 + Others)',
            hole=0.4
        )
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, use_container_width=True)

# TAB 2: Forecasting & Tendencias
with tab2:
    st.markdown('<div class="section-header">📈 Forecasting & Tendencias</div>', unsafe_allow_html=True)
    
    # Análisis temporal
    st.subheader("Revenue & Orders Over Time")
    
    # Selector de granularidad
    granularity = st.selectbox("Granularidad", ['Day', 'Week', 'Month'], index=1)
    
    # Agrupar datos
    temp_df = filtered_df.copy()
    if granularity == 'Day':
        temp_df['period'] = temp_df['date'].dt.date
    elif granularity == 'Week':
        temp_df['period'] = temp_df['date'].dt.to_period('W').dt.start_time
    else:
        temp_df['period'] = temp_df['date'].dt.to_period('M').dt.start_time
    
    time_series = temp_df.groupby('period').agg({
        'total_amount_usd': 'sum',
        'transaction_id': 'count'
    }).reset_index()
    time_series.columns = ['period', 'revenue', 'orders']
    
    # Gráfico dual-axis
    fig_time = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_time.add_trace(
        go.Bar(x=time_series['period'], y=time_series['revenue'], name='Revenue', marker_color='#667eea'),
        secondary_y=False
    )
    
    fig_time.add_trace(
        go.Scatter(x=time_series['period'], y=time_series['orders'], name='Orders', 
                   line=dict(color='#f093fb', width=3), mode='lines+markers'),
        secondary_y=True
    )
    
    fig_time.update_xaxes(title_text="Fecha")
    fig_time.update_yaxes(title_text="Revenue ($)", secondary_y=False)
    fig_time.update_yaxes(title_text="Orders", secondary_y=True)
    fig_time.update_layout(height=400, title='Revenue y Orders a lo Largo del Tiempo')
    
    st.plotly_chart(fig_time, use_container_width=True)
    
    # Forecasting con Prophet
    if show_ml_predictions and len(time_series) > 10:
        st.subheader("🔮 Forecasting 90 Días (Prophet)")
        
        try:
            from prophet import Prophet
            
            # Preparar datos para Prophet
            prophet_df = time_series[['period', 'revenue']].copy()
            prophet_df.columns = ['ds', 'y']
            prophet_df['ds'] = pd.to_datetime(prophet_df['ds'])
            
            # Entrenar modelo
            with st.spinner('Entrenando modelo Prophet...'):
                model = Prophet(
                    daily_seasonality=False,
                    weekly_seasonality=True,
                    yearly_seasonality=True,
                    interval_width=0.95
                )
                model.fit(prophet_df)
                
                # Crear fechas futuras
                future = model.make_future_dataframe(periods=90)
                forecast = model.predict(future)
            
            # Visualizar predicción
            col1, col2 = st.columns([7, 3])
            
            with col1:
                fig_forecast = go.Figure()
                
                # Datos históricos
                fig_forecast.add_trace(go.Scatter(
                    x=prophet_df['ds'],
                    y=prophet_df['y'],
                    mode='markers',
                    name='Datos Históricos',
                    marker=dict(color='#1E40AF', size=8)
                ))
                
                # Predicción
                fig_forecast.add_trace(go.Scatter(
                    x=forecast['ds'],
                    y=forecast['yhat'],
                    mode='lines',
                    name='Predicción',
                    line=dict(color='#EF4444', width=2)
                ))
                
                # Banda de confianza 95%
                fig_forecast.add_trace(go.Scatter(
                    x=forecast['ds'],
                    y=forecast['yhat_upper'],
                    fill=None,
                    mode='lines',
                    line_color='rgba(200,200,200,0.3)',
                    showlegend=False
                ))
                
                fig_forecast.add_trace(go.Scatter(
                    x=forecast['ds'],
                    y=forecast['yhat_lower'],
                    fill='tonexty',
                    mode='lines',
                    line_color='rgba(200,200,200,0.3)',
                    name='95% Intervalo Confianza'
                ))
                
                fig_forecast.update_layout(
                    title='Predicción de Revenue 90 Días',
                    xaxis_title='Fecha',
                    yaxis_title='Revenue ($)',
                    height=400
                )
                
                st.plotly_chart(fig_forecast, use_container_width=True)
            
            with col2:
                st.subheader("Métricas del Modelo")
                
                # Calcular métricas
                from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
                
                y_true = prophet_df['y'].values
                y_pred = forecast.iloc[:len(prophet_df)]['yhat'].values
                
                mae = mean_absolute_error(y_true, y_pred)
                rmse = np.sqrt(mean_squared_error(y_true, y_pred))
                mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
                r2 = r2_score(y_true, y_pred)
                
                st.metric("MAPE", f"{mape:.2f}%")
                st.metric("RMSE", f"${rmse:,.0f}")
                st.metric("R²", f"{r2:.3f}")
                
                # Predicción próximos 30 días
                next_30_days = forecast.tail(30)['yhat'].sum()
                st.metric("Revenue Predicho (30d)", f"${next_30_days:,.0f}")
                
        except Exception as e:
            st.warning(f"No se pudo generar forecast: {str(e)}")
    
    # Growth Rate Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Growth Rate Analysis")
        if len(time_series) > 1:
            time_series['growth_rate'] = time_series['revenue'].pct_change() * 100
            
            fig_growth = px.line(
                time_series,
                x='period',
                y='growth_rate',
                title='Growth Rate (%) Over Time',
                labels={'growth_rate': 'Growth Rate (%)'}
            )
            fig_growth.add_hline(y=0, line_dash="dash", line_color="gray")
            fig_growth.update_layout(height=350)
            st.plotly_chart(fig_growth, use_container_width=True)
    
    with col2:
        st.subheader("Revenue Distribution")
        fig_dist = px.histogram(
            filtered_df,
            x='total_amount_usd',
            nbins=50,
            title='Distribución de Revenue por Transacción',
            labels={'total_amount_usd': 'Revenue ($)'}
        )
        fig_dist.update_layout(height=350)
        st.plotly_chart(fig_dist, use_container_width=True)

# TAB 3: Análisis de Productos
with tab3:
    st.markdown('<div class="section-header">🛍️ Análisis de Productos</div>', unsafe_allow_html=True)
    
    # Product Performance Matrix
    col1, col2 = st.columns([6, 4])
    
    with col1:
        st.subheader("Product Performance Matrix (BCG)")
        
        # Calcular métricas por producto
        product_metrics = filtered_df.groupby('product_id').agg({
            'quantity': 'sum',
            'total_amount_usd': 'sum',
            'profit': 'sum',
            'product_name': 'first',
            'category': 'first'
        }).reset_index()
        
        product_metrics['margin'] = (product_metrics['profit'] / product_metrics['total_amount_usd'] * 100).fillna(0)
        
        fig_bcg = px.scatter(
            product_metrics,
            x='quantity',
            y='margin',
            size='total_amount_usd',
            color='category',
            hover_name='product_name',
            hover_data={
                'total_amount_usd': ':$,.0f',
                'quantity': ':,',
                'margin': ':.1f%'
            },
            title='Matriz BCG: Volumen vs Margen (tamaño = revenue)',
            labels={'quantity': 'Unidades Vendidas', 'margin': 'Margen de Profit (%)'}
        )
        
        # Añadir líneas de cuadrantes
        median_quantity = product_metrics['quantity'].median()
        median_margin = product_metrics['margin'].median()
        
        fig_bcg.add_hline(y=median_margin, line_dash="dash", line_color="gray", opacity=0.5)
        fig_bcg.add_vline(x=median_quantity, line_dash="dash", line_color="gray", opacity=0.5)
        
        # Añadir anotaciones de cuadrantes
        fig_bcg.add_annotation(x=median_quantity*1.5, y=median_margin*1.5, text="⭐ Stars", showarrow=False, font=dict(size=14, color="green"))
        fig_bcg.add_annotation(x=median_quantity*0.5, y=median_margin*1.5, text="❓ Question Marks", showarrow=False, font=dict(size=14, color="orange"))
        fig_bcg.add_annotation(x=median_quantity*1.5, y=median_margin*0.5, text="🐮 Cash Cows", showarrow=False, font=dict(size=14, color="blue"))
        fig_bcg.add_annotation(x=median_quantity*0.5, y=median_margin*0.5, text="🐕 Dogs", showarrow=False, font=dict(size=14, color="red"))
        
        fig_bcg.update_layout(height=500)
        st.plotly_chart(fig_bcg, use_container_width=True)
    
    with col2:
        st.subheader("Top 20 Products")
        top_products = product_metrics.nlargest(20, 'total_amount_usd')[['product_name', 'category', 'total_amount_usd', 'quantity', 'margin']]
        top_products.columns = ['Product', 'Category', 'Revenue', 'Units', 'Margin %']
        top_products['Revenue'] = top_products['Revenue'].apply(lambda x: f"${x:,.0f}")
        top_products['Units'] = top_products['Units'].apply(lambda x: f"{x:,}")
        top_products['Margin %'] = top_products['Margin %'].apply(lambda x: f"{x:.1f}%")
        
        st.dataframe(top_products, use_container_width=True, height=500)
    
    # Row 2
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Revenue by Category")
        category_revenue = filtered_df.groupby(['category', 'subcategory'])['total_amount_usd'].sum().reset_index()
        
        fig_cat = px.treemap(
            category_revenue,
            path=['category', 'subcategory'],
            values='total_amount_usd',
            color='total_amount_usd',
            color_continuous_scale='Blues',
            title='Treemap: Categoría → Subcategoría'
        )
        fig_cat.update_layout(height=400)
        st.plotly_chart(fig_cat, use_container_width=True)
    
    with col4:
        st.subheader("Category Performance")
        cat_metrics = filtered_df.groupby('category').agg({
            'total_amount_usd': 'sum',
            'profit': 'sum',
            'quantity': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        
        fig_cat_bar = px.bar(
            cat_metrics,
            x='category',
            y='total_amount_usd',
            color='profit',
            title='Revenue y Profit por Categoría',
            labels={'total_amount_usd': 'Revenue ($)', 'profit': 'Profit ($)'}
        )
        fig_cat_bar.update_layout(height=400)
        st.plotly_chart(fig_cat_bar, use_container_width=True)

# TAB 4: Segmentación de Clientes
with tab4:
    st.markdown('<div class="section-header">👥 Segmentación de Clientes</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([5, 5])
    
    with col1:
        st.subheader("Customer Segmentation (RFM Analysis)")
        
        # Filtrar clientes que aparecen en transacciones filtradas
        active_customers = customers_df[customers_df['customer_id'].isin(filtered_df['customer_id'])]
        
        # Scatter plot RFM
        fig_rfm = px.scatter(
            active_customers,
            x='recency_score',
            y='frequency_score',
            size='monetary_score',
            color='rfm_segment',
            hover_name='customer_id',
            hover_data={
                'recency_score': True,
                'frequency_score': True,
                'monetary_score': ':$,.0f',
                'churn_probability': ':.2%'
            },
            title='RFM: Recency vs Frequency (tamaño = Monetary)',
            labels={
                'recency_score': 'Recency (días desde última compra)',
                'frequency_score': 'Frequency (# de compras)'
            },
            color_discrete_map={
                'Champions': 'darkgreen',
                'Loyal Customers': 'green',
                'Potential Loyalists': 'lightgreen',
                'Recent Customers': 'blue',
                'Promising': 'cyan',
                'Customers Needing Attention': 'yellow',
                'About to Sleep': 'orange',
                'At Risk': 'red',
                "Can't Lose Them": 'darkred',
                'Hibernating': 'gray',
                'Lost': 'black'
            }
        )
        fig_rfm.update_layout(height=500)
        st.plotly_chart(fig_rfm, use_container_width=True)
        
        # Tabla de estadísticas por segmento
        st.subheader("Cluster Statistics")
        segment_stats = active_customers.groupby('rfm_segment').agg({
            'customer_id': 'count',
            'lifetime_value': 'mean',
            'total_orders': 'mean',
            'avg_order_value': 'mean'
        }).reset_index()
        segment_stats.columns = ['Segment', 'Count', 'Avg LTV', 'Avg Orders', 'Avg AOV']
        segment_stats = segment_stats.sort_values('Avg LTV', ascending=False)
        
        segment_stats['Avg LTV'] = segment_stats['Avg LTV'].apply(lambda x: f"${x:,.0f}")
        segment_stats['Avg Orders'] = segment_stats['Avg Orders'].apply(lambda x: f"{x:.1f}")
        segment_stats['Avg AOV'] = segment_stats['Avg AOV'].apply(lambda x: f"${x:.2f}")
        
        st.dataframe(segment_stats, use_container_width=True)
    
    with col2:
        st.subheader("Customer Lifetime Value Distribution")
        
        fig_ltv = px.histogram(
            active_customers,
            x='lifetime_value',
            nbins=50,
            title='Distribución de LTV',
            labels={'lifetime_value': 'Lifetime Value ($)'}
        )
        
        # Añadir percentiles
        p25 = active_customers['lifetime_value'].quantile(0.25)
        p50 = active_customers['lifetime_value'].quantile(0.50)
        p75 = active_customers['lifetime_value'].quantile(0.75)
        p90 = active_customers['lifetime_value'].quantile(0.90)
        
        fig_ltv.add_vline(x=p25, line_dash="dash", line_color="blue", annotation_text="P25")
        fig_ltv.add_vline(x=p50, line_dash="dash", line_color="green", annotation_text="P50")
        fig_ltv.add_vline(x=p75, line_dash="dash", line_color="orange", annotation_text="P75")
        fig_ltv.add_vline(x=p90, line_dash="dash", line_color="red", annotation_text="P90")
        
        fig_ltv.update_layout(height=350)
        st.plotly_chart(fig_ltv, use_container_width=True)
        
        # Pareto
        st.metric("Media LTV", f"${active_customers['lifetime_value'].mean():,.0f}")
        st.metric("Mediana LTV", f"${active_customers['lifetime_value'].median():,.0f}")
        
        top20_pct = active_customers.nlargest(int(len(active_customers) * 0.2), 'lifetime_value')['lifetime_value'].sum()
        total_ltv = active_customers['lifetime_value'].sum()
        pareto = (top20_pct / total_ltv * 100) if total_ltv > 0 else 0
        
        st.metric("Top 20% customers", f"{pareto:.1f}% del revenue total", delta="Pareto Principle")
    
    # Cohort Analysis
    st.subheader("📊 Cohort Analysis")
    
    # Preparar datos de cohorte
    cohort_data = filtered_df.merge(customers_df[['customer_id', 'registration_date']], on='customer_id')
    cohort_data['cohort'] = pd.to_datetime(cohort_data['registration_date']).dt.to_period('M')
    cohort_data['transaction_month'] = pd.to_datetime(cohort_data['date']).dt.to_period('M')
    cohort_data['cohort_age'] = (cohort_data['transaction_month'] - cohort_data['cohort']).apply(lambda x: x.n)
    
    # Crear matriz de cohorte
    cohort_matrix = cohort_data.groupby(['cohort', 'cohort_age'])['customer_id'].nunique().reset_index()
    cohort_matrix = cohort_matrix.pivot(index='cohort', columns='cohort_age', values='customer_id')
    
    # Calcular retention rate
    cohort_sizes = cohort_matrix.iloc[:, 0]
    retention_matrix = cohort_matrix.divide(cohort_sizes, axis=0) * 100
    
    # Limitar a 12 meses
    retention_matrix = retention_matrix.iloc[:, :min(12, retention_matrix.shape[1])]
    
    # Heatmap
    fig_cohort = px.imshow(
        retention_matrix.values,
        labels=dict(x="Meses desde Registro", y="Cohorte", color="Retention %"),
        x=[f"M{i}" for i in range(retention_matrix.shape[1])],
        y=[str(c) for c in retention_matrix.index],
        color_continuous_scale='RdYlGn',
        title='Cohort Analysis: Retention Rate (%)'
    )
    fig_cohort.update_layout(height=400)
    st.plotly_chart(fig_cohort, use_container_width=True)
    
    # Churn Prediction
    st.subheader("⚠️ Churn Prediction")
    
    col1, col2 = st.columns([3, 7])
    
    with col1:
        churn_rate = active_customers['churn_probability'].mean() * 100
        st.metric("Current Churn Rate", f"{churn_rate:.1f}%")
        st.metric("At-Risk Customers", f"{len(active_customers[active_customers['churn_probability'] > 0.7]):,}")
        st.metric("High Value At-Risk", f"{len(active_customers[(active_customers['churn_probability'] > 0.7) & (active_customers['lifetime_value'] > 1000)]):,}")
    
    with col2:
        # Top 100 clientes en riesgo
        at_risk = active_customers[active_customers['churn_probability'] > 0.5].nlargest(100, 'churn_probability')
        at_risk_display = at_risk[['customer_id', 'country', 'lifetime_value', 'last_purchase_date', 'churn_probability']].copy()
        at_risk_display.columns = ['Customer ID', 'Country', 'LTV', 'Last Purchase', 'Churn Prob']
        at_risk_display['LTV'] = at_risk_display['LTV'].apply(lambda x: f"${x:,.0f}")
        at_risk_display['Churn Prob'] = at_risk_display['Churn Prob'].apply(lambda x: f"{x:.1%}")
        at_risk_display['Last Purchase'] = pd.to_datetime(at_risk_display['Last Purchase']).dt.strftime('%Y-%m-%d')
        
        st.dataframe(at_risk_display.head(20), use_container_width=True)

# TAB 5: ML Insights
with tab5:
    st.markdown('<div class="section-header">🤖 Machine Learning Insights</div>', unsafe_allow_html=True)
    
    if show_ml_predictions:
        # Customer Clustering con K-Means
        st.subheader("Customer Clustering (K-Means + PCA)")
        
        try:
            from sklearn.cluster import KMeans
            from sklearn.preprocessing import StandardScaler
            from sklearn.decomposition import PCA
            
            # Preparar features
            active_customers = customers_df[customers_df['customer_id'].isin(filtered_df['customer_id'])].copy()
            features = active_customers[['recency_score', 'frequency_score', 'monetary_score', 'age', 'total_orders', 'avg_order_value']]
            
            # Normalizar
            scaler = StandardScaler()
            features_scaled = scaler.fit_transform(features)
            
            # K-Means
            n_clusters = 5
            kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
            active_customers['cluster'] = kmeans.fit_predict(features_scaled)
            
            # PCA para visualización
            pca = PCA(n_components=2)
            pca_features = pca.fit_transform(features_scaled)
            active_customers['pca1'] = pca_features[:, 0]
            active_customers['pca2'] = pca_features[:, 1]
            
            col1, col2 = st.columns([6, 4])
            
            with col1:
                fig_cluster = px.scatter(
                    active_customers,
                    x='pca1',
                    y='pca2',
                    color='cluster',
                    hover_name='customer_id',
                    hover_data={'lifetime_value': ':$,.0f', 'total_orders': True},
                    title='Customer Clusters (PCA Reduction a 2D)',
                    labels={'pca1': 'PC1', 'pca2': 'PC2'}
                )
                fig_cluster.update_layout(height=450)
                st.plotly_chart(fig_cluster, use_container_width=True)
                
                st.info(f"📊 Varianza explicada por PCA: {pca.explained_variance_ratio_.sum()*100:.1f}%")
            
            with col2:
                st.subheader("Cluster Characteristics")
                cluster_stats = active_customers.groupby('cluster').agg({
                    'customer_id': 'count',
                    'lifetime_value': 'mean',
                    'total_orders': 'mean',
                    'avg_order_value': 'mean',
                    'country': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'N/A'
                }).reset_index()
                cluster_stats.columns = ['Cluster', 'Size', 'Avg LTV', 'Avg Orders', 'Avg AOV', 'Top Country']
                
                cluster_stats['Avg LTV'] = cluster_stats['Avg LTV'].apply(lambda x: f"${x:,.0f}")
                cluster_stats['Avg Orders'] = cluster_stats['Avg Orders'].apply(lambda x: f"{x:.1f}")
                cluster_stats['Avg AOV'] = cluster_stats['Avg AOV'].apply(lambda x: f"${x:.2f}")
                
                st.dataframe(cluster_stats, use_container_width=True, height=300)
                
                # Recomendaciones
                st.subheader("💡 Recommendations")
                st.write("**Cluster 0:** Focus on retention")
                st.write("**Cluster 1:** Upsell opportunities")
                st.write("**Cluster 2:** Re-engagement campaign")
                st.write("**Cluster 3:** VIP treatment")
                st.write("**Cluster 4:** Win-back strategy")
        
        except Exception as e:
            st.warning(f"Error en clustering: {str(e)}")
        
        # Anomaly Detection
        st.subheader("🚨 Anomaly Detection")
        
        try:
            from sklearn.ensemble import IsolationForest
            
            # Agrupar por día
            daily_data = filtered_df.groupby(filtered_df['date'].dt.date).agg({
                'total_amount_usd': 'sum',
                'transaction_id': 'count'
            }).reset_index()
            daily_data.columns = ['date', 'revenue', 'orders']
            
            # Isolation Forest
            iso_forest = IsolationForest(contamination=0.05, random_state=42)
            daily_data['anomaly'] = iso_forest.fit_predict(daily_data[['revenue', 'orders']])
            daily_data['is_anomaly'] = daily_data['anomaly'] == -1
            
            # Visualizar
            fig_anomaly = go.Figure()
            
            # Datos normales
            normal_data = daily_data[~daily_data['is_anomaly']]
            fig_anomaly.add_trace(go.Scatter(
                x=normal_data['date'],
                y=normal_data['revenue'],
                mode='lines',
                name='Revenue Normal',
                line=dict(color='#1E40AF', width=2)
            ))
            
            # Anomalías
            anomaly_data = daily_data[daily_data['is_anomaly']]
            fig_anomaly.add_trace(go.Scatter(
                x=anomaly_data['date'],
                y=anomaly_data['revenue'],
                mode='markers',
                name='Anomalía Detectada',
                marker=dict(color='red', size=12, symbol='x')
            ))
            
            fig_anomaly.update_layout(
                title='Detección de Anomalías en Revenue Diario',
                xaxis_title='Fecha',
                yaxis_title='Revenue ($)',
                height=400
            )
            
            st.plotly_chart(fig_anomaly, use_container_width=True)
            
            # Tabla de anomalías
            if len(anomaly_data) > 0:
                st.subheader("Alerts Table")
                anomaly_display = anomaly_data[['date', 'revenue', 'orders']].copy()
                anomaly_display['expected_revenue'] = normal_data['revenue'].mean()
                anomaly_display['deviation'] = ((anomaly_display['revenue'] - anomaly_display['expected_revenue']) / anomaly_display['expected_revenue'] * 100)
                anomaly_display['severity'] = anomaly_display['deviation'].abs().apply(lambda x: '🔴 Critical' if x > 50 else '🟡 Warning')
                
                anomaly_display.columns = ['Date', 'Actual Revenue', 'Orders', 'Expected Revenue', 'Deviation %', 'Severity']
                anomaly_display['Actual Revenue'] = anomaly_display['Actual Revenue'].apply(lambda x: f"${x:,.0f}")
                anomaly_display['Expected Revenue'] = anomaly_display['Expected Revenue'].apply(lambda x: f"${x:,.0f}")
                anomaly_display['Deviation %'] = anomaly_display['Deviation %'].apply(lambda x: f"{x:+.1f}%")
                
                st.dataframe(anomaly_display, use_container_width=True)
            else:
                st.success("✅ No se detectaron anomalías en el periodo seleccionado")
                
        except Exception as e:
            st.warning(f"Error en anomaly detection: {str(e)}")
    
    else:
        st.info("🤖 Activa las predicciones ML en el sidebar para ver insights avanzados")
    
    # Channel Performance Analysis
    st.subheader("📱 Device & Channel Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        device_data = filtered_df.groupby('device_type').agg({
            'total_amount_usd': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        device_data.columns = ['device', 'revenue', 'orders']
        
        fig_device = px.pie(
            device_data,
            values='revenue',
            names='device',
            title='Revenue by Device Type',
            hole=0.4
        )
        st.plotly_chart(fig_device, use_container_width=True)
    
    with col2:
        traffic_data = filtered_df.groupby('traffic_source').agg({
            'total_amount_usd': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        traffic_data.columns = ['source', 'revenue', 'orders']
        traffic_data['aov'] = traffic_data['revenue'] / traffic_data['orders']
        
        fig_traffic = px.bar(
            traffic_data,
            x='source',
            y='revenue',
            color='aov',
            title='Revenue by Traffic Source',
            labels={'revenue': 'Revenue ($)', 'aov': 'AOV ($)'}
        )
        st.plotly_chart(fig_traffic, use_container_width=True)
    
    # Payment Methods
    st.subheader("💳 Payment Methods Performance")
    
    payment_data = filtered_df.groupby('payment_method').agg({
        'total_amount_usd': 'sum',
        'transaction_id': 'count'
    }).reset_index()
    payment_data.columns = ['method', 'revenue', 'transactions']
    payment_data = payment_data.sort_values('revenue', ascending=True)
    
    fig_payment = px.bar(
        payment_data,
        y='method',
        x='revenue',
        orientation='h',
        color='revenue',
        title='Revenue by Payment Method',
        labels={'revenue': 'Revenue ($)', 'method': 'Payment Method'}
    )
    st.plotly_chart(fig_payment, use_container_width=True)

# TAB 6: Tablas Detalladas
with tab6:
    st.markdown('<div class="section-header">📊 Tablas Detalladas</div>', unsafe_allow_html=True)
    
    st.subheader("Transacciones Completas")
    
    # Selector de número de filas
    n_rows = st.selectbox("Mostrar filas", [50, 100, 500, 1000], index=1)
    
    # Mostrar tabla
    display_df = filtered_df[[
        'date', 'transaction_id', 'customer_id', 'country', 'product_name', 
        'category', 'quantity', 'unit_price', 'total_amount_usd', 
        'payment_method', 'device_type', 'traffic_source'
    ]].head(n_rows).copy()
    
    display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d %H:%M')
    display_df['unit_price'] = display_df['unit_price'].apply(lambda x: f"${x:.2f}")
    display_df['total_amount_usd'] = display_df['total_amount_usd'].apply(lambda x: f"${x:.2f}")
    
    st.dataframe(display_df, use_container_width=True, height=600)
    
    # Botón de descarga
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar CSV Completo",
        data=csv,
        file_name=f'transactions_{datetime.now().strftime("%Y%m%d")}.csv',
        mime='text/csv',
    )
    
    # Estadísticas resumidas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Transacciones", f"{len(filtered_df):,}")
        st.metric("Fecha Mínima", filtered_df['date'].min().strftime('%Y-%m-%d'))
    
    with col2:
        st.metric("Total Revenue", f"${filtered_df['total_amount_usd'].sum():,.2f}")
        st.metric("Fecha Máxima", filtered_df['date'].max().strftime('%Y-%m-%d'))
    
    with col3:
        st.metric("Promedio por Transacción", f"${filtered_df['total_amount_usd'].mean():.2f}")
        st.metric("Total Países", f"{filtered_df['country'].nunique()}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6B7280; padding: 2rem 0;'>
    <p><strong>Global Ecommerce Analytics Platform</strong> | Powered by Streamlit, Prophet, scikit-learn & Plotly</p>
    <p>Dashboard Profesional de Business Intelligence con IA y Machine Learning</p>
</div>
""", unsafe_allow_html=True)
