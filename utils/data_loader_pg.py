import pandas as pd
import streamlit as st
from sqlalchemy import text
from database.schema import get_engine, get_session
from datetime import datetime, timedelta
from utils.traducciones import aplicar_traducciones_df

@st.cache_data(ttl=300)
def load_data_from_postgres():
    """Carga datos desde archivos unificados (Parquet) o PostgreSQL"""
    import os
    
    # Verificar si existen archivos unificados
    use_unified = os.path.exists('data/transactions_unified.parquet')
    
    if use_unified:
        try:
            # Cargar desde archivos unificados
            transactions_df = pd.read_parquet('data/transactions_unified.parquet')
            customers_df = pd.read_parquet('data/customers_unified.parquet')
            products_df = pd.read_parquet('data/products_unified.parquet')
            
            # Convertir fechas
            transactions_df['date'] = pd.to_datetime(transactions_df['date'])
            customers_df['registration_date'] = pd.to_datetime(customers_df['registration_date'])
            customers_df['last_purchase_date'] = pd.to_datetime(customers_df['last_purchase_date'])
            if 'launch_date' in products_df.columns:
                products_df['launch_date'] = pd.to_datetime(products_df['launch_date'])
            
            # Traducir categorías al español
            transactions_df = aplicar_traducciones_df(transactions_df, 'category')
            products_df = aplicar_traducciones_df(products_df, 'category')
            if 'subcategory' in transactions_df.columns:
                transactions_df = aplicar_traducciones_df(transactions_df, 'subcategory')
            if 'subcategory' in products_df.columns:
                products_df = aplicar_traducciones_df(products_df, 'subcategory')
            
            return transactions_df, customers_df, products_df
            
        except Exception as e:
            pass
    
    # Fallback a PostgreSQL
    engine = get_engine()
    
    try:
        # Cargar transacciones
        transactions_df = pd.read_sql_table('transactions', engine)
        
        # Cargar clientes
        customers_df = pd.read_sql_table('customers', engine)
        
        # Cargar productos
        products_df = pd.read_sql_table('products', engine)
        
        # Convertir fechas
        transactions_df['date'] = pd.to_datetime(transactions_df['date'])
        customers_df['registration_date'] = pd.to_datetime(customers_df['registration_date'])
        customers_df['last_purchase_date'] = pd.to_datetime(customers_df['last_purchase_date'])
        products_df['launch_date'] = pd.to_datetime(products_df['launch_date'])
        
        # Traducir categorías al español
        transactions_df = aplicar_traducciones_df(transactions_df, 'category')
        products_df = aplicar_traducciones_df(products_df, 'category')
        if 'subcategory' in transactions_df.columns:
            transactions_df = aplicar_traducciones_df(transactions_df, 'subcategory')
        if 'subcategory' in products_df.columns:
            products_df = aplicar_traducciones_df(products_df, 'subcategory')
        
        return transactions_df, customers_df, products_df
        
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None, None

@st.cache_data
def load_or_generate_data():
    """Carga datos desde fuente disponible"""
    # Cargar directamente sin mensajes
    return load_data_from_postgres()

def filter_data(df, filters):
    """Aplica filtros al DataFrame"""
    filtered_df = df.copy()
    
    if 'date_range' in filters and filters['date_range']:
        start_date, end_date = filters['date_range']
        filtered_df = filtered_df[(filtered_df['date'] >= pd.Timestamp(start_date)) & 
                                   (filtered_df['date'] <= pd.Timestamp(end_date))]
    
    if 'countries' in filters and filters['countries']:
        filtered_df = filtered_df[filtered_df['country'].isin(filters['countries'])]
    
    if 'categories' in filters and filters['categories']:
        filtered_df = filtered_df[filtered_df['category'].isin(filters['categories'])]
    
    if 'segments' in filters and filters['segments']:
        filtered_df = filtered_df[filtered_df['customer_segment'].isin(filters['segments'])]
    
    if 'payment_methods' in filters and filters['payment_methods']:
        filtered_df = filtered_df[filtered_df['payment_method'].isin(filters['payment_methods'])]
    
    if 'device_types' in filters and filters['device_types']:
        filtered_df = filtered_df[filtered_df['device_type'].isin(filters['device_types'])]
    
    if 'traffic_sources' in filters and filters['traffic_sources']:
        filtered_df = filtered_df[filtered_df['traffic_source'].isin(filters['traffic_sources'])]
    
    if 'price_range' in filters and filters['price_range']:
        min_price, max_price = filters['price_range']
        filtered_df = filtered_df[(filtered_df['unit_price'] >= min_price) & 
                                   (filtered_df['unit_price'] <= max_price)]
    
    return filtered_df

def get_date_range_preset(preset):
    """Devuelve rango de fechas basado en preset"""
    end_date = datetime.now()
    
    if preset == 'Today':
        start_date = end_date - timedelta(days=1)
    elif preset == 'Last 7 Days':
        start_date = end_date - timedelta(days=7)
    elif preset == 'Last 30 Days':
        start_date = end_date - timedelta(days=30)
    elif preset == 'Last 90 Days':
        start_date = end_date - timedelta(days=90)
    elif preset == 'Last Year':
        start_date = end_date - timedelta(days=365)
    elif preset == 'All Time':
        start_date = end_date - timedelta(days=730)
    else:
        start_date = end_date - timedelta(days=30)
    
    return start_date, end_date

@st.cache_data(ttl=60)
def get_kpis_from_db(start_date, end_date, filters=None):
    """Obtiene KPIs directamente desde PostgreSQL con query optimizada"""
    engine = get_engine()
    
    query = f"""
    SELECT 
        COUNT(*) as total_orders,
        SUM(total_amount_usd) as total_revenue,
        AVG(total_amount_usd) as avg_order_value,
        SUM(profit) as total_profit,
        COUNT(DISTINCT customer_id) as total_customers
    FROM transactions
    WHERE date >= '{start_date}' AND date <= '{end_date}'
    """
    
    if filters:
        if 'countries' in filters and filters['countries']:
            countries_str = "','".join(filters['countries'])
            query += f" AND country IN ('{countries_str}')"
        
        if 'categories' in filters and filters['categories']:
            categories_str = "','".join(filters['categories'])
            query += f" AND category IN ('{categories_str}')"
    
    try:
        result = pd.read_sql_query(query, engine)
        return result.iloc[0].to_dict()
    except:
        return None
