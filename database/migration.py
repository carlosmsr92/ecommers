import pandas as pd
import os
from database.schema import get_session, create_tables, drop_tables, Transaction, Customer, Product
from sqlalchemy.exc import IntegrityError
from tqdm import tqdm

def migrate_data_to_postgres():
    """Migra datos desde Parquet a PostgreSQL"""
    
    # Crear tablas
    print("📊 Creando esquema de base de datos...")
    create_tables()
    
    # Verificar que existen los archivos Parquet
    data_dir = 'data'
    transactions_path = os.path.join(data_dir, 'transactions.parquet')
    customers_path = os.path.join(data_dir, 'customers.parquet')
    products_path = os.path.join(data_dir, 'products.parquet')
    
    if not all([os.path.exists(p) for p in [transactions_path, customers_path, products_path]]):
        print("❌ No se encontraron archivos Parquet. Genera los datos primero.")
        return False
    
    session = get_session()
    
    try:
        # Migrar productos
        print("\n📦 Migrando productos...")
        products_df = pd.read_parquet(products_path)
        
        for _, row in tqdm(products_df.iterrows(), total=len(products_df)):
            product = Product(
                product_id=row['product_id'],
                product_name=row['product_name'],
                category=row['category'],
                subcategory=row['subcategory'],
                brand=row['brand'],
                base_price=float(row['base_price']),
                cost_price=float(row['cost_price']),
                margin_percentage=float(row['margin_percentage']),
                stock_quantity=int(row['stock_quantity']),
                supplier_country=row['supplier_country'],
                weight=float(row['weight']),
                rating=float(row['rating']),
                reviews_count=int(row['reviews_count']),
                launch_date=pd.to_datetime(row['launch_date']).date()
            )
            session.add(product)
        
        session.commit()
        print(f"✅ {len(products_df)} productos migrados")
        
        # Migrar clientes
        print("\n👥 Migrando clientes...")
        customers_df = pd.read_parquet(customers_path)
        
        for _, row in tqdm(customers_df.iterrows(), total=len(customers_df)):
            customer = Customer(
                customer_id=row['customer_id'],
                registration_date=pd.to_datetime(row['registration_date']).date(),
                country=row['country'],
                age=int(row['age']),
                gender=row['gender'],
                lifetime_value=float(row['lifetime_value']),
                total_orders=int(row['total_orders']),
                avg_order_value=float(row['avg_order_value']),
                last_purchase_date=pd.to_datetime(row['last_purchase_date']),
                recency_score=int(row['recency_score']),
                frequency_score=int(row['frequency_score']),
                monetary_score=float(row['monetary_score']),
                rfm_segment=row['rfm_segment'],
                churn_probability=float(row['churn_probability']),
                preferred_category=row['preferred_category']
            )
            session.add(customer)
        
        session.commit()
        print(f"✅ {len(customers_df)} clientes migrados")
        
        # Migrar transacciones (en batches para mejor performance)
        print("\n💳 Migrando transacciones...")
        transactions_df = pd.read_parquet(transactions_path)
        
        batch_size = 1000
        for i in tqdm(range(0, len(transactions_df), batch_size)):
            batch = transactions_df.iloc[i:i+batch_size]
            
            for _, row in batch.iterrows():
                transaction = Transaction(
                    transaction_id=row['transaction_id'],
                    date=pd.to_datetime(row['date']),
                    customer_id=row['customer_id'],
                    country=row['country'],
                    region=row['region'],
                    city=row['city'],
                    product_id=row['product_id'],
                    product_name=row['product_name'],
                    category=row['category'],
                    subcategory=row['subcategory'],
                    quantity=int(row['quantity']),
                    unit_price=float(row['unit_price']),
                    total_amount=float(row['total_amount']),
                    discount_applied=float(row['discount_applied']),
                    payment_method=row['payment_method'],
                    shipping_cost=float(row['shipping_cost']),
                    delivery_time=int(row['delivery_time']),
                    customer_segment=row['customer_segment'],
                    device_type=row['device_type'],
                    traffic_source=row['traffic_source'],
                    currency=row['currency'],
                    exchange_rate=float(row['exchange_rate']),
                    total_amount_usd=float(row['total_amount_usd']),
                    cost_price=float(row['cost_price']),
                    profit=float(row['profit'])
                )
                session.add(transaction)
            
            session.commit()
        
        print(f"✅ {len(transactions_df)} transacciones migradas")
        
        print("\n🎉 ¡Migración completada exitosamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error durante la migración: {str(e)}")
        session.rollback()
        return False
    finally:
        session.close()

if __name__ == "__main__":
    migrate_data_to_postgres()
