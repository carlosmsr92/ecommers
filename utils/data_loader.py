import pandas as pd
import streamlit as st
import os
from datetime import datetime, timedelta

@st.cache_data
def load_or_generate_data():
    """Carga o genera datos si no existen"""
    from utils.data_generator import generate_all_data
    
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)
    
    transactions_path = os.path.join(data_dir, 'transactions.parquet')
    customers_path = os.path.join(data_dir, 'customers.parquet')
    products_path = os.path.join(data_dir, 'products.parquet')
    
    # Verificar si los datos ya existen
    if os.path.exists(transactions_path) and os.path.exists(customers_path) and os.path.exists(products_path):
        transactions_df = pd.read_parquet(transactions_path)
        customers_df = pd.read_parquet(customers_path)
        products_df = pd.read_parquet(products_path)
    else:
        # Generar datos
        with st.spinner('Generando datos simulados (100K transacciones, 50K clientes, 500 productos)... Esto puede tardar un momento...'):
            transactions_df, customers_df, products_df = generate_all_data(
                n_transactions=100000,
                n_customers=50000,
                n_products=500
            )
            
            # Guardar para uso futuro
            transactions_df.to_parquet(transactions_path)
            customers_df.to_parquet(customers_path)
            products_df.to_parquet(products_path)
    
    # Convertir fecha a datetime
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])
    customers_df['registration_date'] = pd.to_datetime(customers_df['registration_date'])
    customers_df['last_purchase_date'] = pd.to_datetime(customers_df['last_purchase_date'])
    products_df['launch_date'] = pd.to_datetime(products_df['launch_date'])
    
    return transactions_df, customers_df, products_df

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
