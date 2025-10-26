"""
Migración de datos unificados (2010-2025) a PostgreSQL
"""

import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.schema import get_engine, Base, Transaction, Customer, Product
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import numpy as np

def migrate_unified_data_to_postgres():
    """Migra los datos unificados de Parquet a PostgreSQL"""
    
    print("🔄 MIGRACIÓN DE DATOS UNIFICADOS A POSTGRESQL")
    print("=" * 80)
    
    engine = get_engine()
    
    # ============================================================================
    # 1. CREAR TABLAS
    # ============================================================================
    print("\n1️⃣ Creando tablas en PostgreSQL...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("   ✅ Tablas creadas")
    
    # ============================================================================
    # 2. MIGRAR PRODUCTOS
    # ============================================================================
    print("\n2️⃣ Migrando productos...")
    df_products = pd.read_parquet('data/products_unified.parquet')
    
    # Limpiar datos
    df_products = df_products.replace({np.nan: None})
    df_products['launch_date'] = pd.to_datetime(df_products['launch_date'])
    
    # Insertar en batches
    batch_size = 500
    total_inserted = 0
    
    with engine.connect() as conn:
        for i in range(0, len(df_products), batch_size):
            batch = df_products.iloc[i:i+batch_size]
            batch.to_sql('products', conn, if_exists='append', index=False, method='multi')
            total_inserted += len(batch)
            print(f"   Productos insertados: {total_inserted:,}/{len(df_products):,}", end='\r')
    
    print(f"\n   ✅ {total_inserted:,} productos migrados")
    
    # ============================================================================
    # 3. MIGRAR CLIENTES
    # ============================================================================
    print("\n3️⃣ Migrando clientes...")
    df_customers = pd.read_parquet('data/customers_unified.parquet')
    
    # Limpiar datos
    df_customers = df_customers.replace({np.nan: None})
    df_customers['registration_date'] = pd.to_datetime(df_customers['registration_date'])
    df_customers['last_purchase_date'] = pd.to_datetime(df_customers['last_purchase_date'])
    
    # Asegurar tipos correctos
    df_customers['age'] = df_customers['age'].astype(int)
    df_customers['total_orders'] = df_customers['total_orders'].astype(int)
    df_customers['recency_score'] = df_customers['recency_score'].astype(int)
    df_customers['frequency_score'] = df_customers['frequency_score'].astype(int)
    df_customers['monetary_score'] = df_customers['monetary_score'].astype(int)
    
    # Seleccionar solo columnas que existen en el schema
    columns_to_keep = [
        'customer_id', 'registration_date', 'country', 'age', 'gender',
        'lifetime_value', 'total_orders', 'avg_order_value', 'last_purchase_date',
        'recency_score', 'frequency_score', 'monetary_score', 'rfm_segment',
        'churn_probability', 'preferred_category'
    ]
    df_customers = df_customers[columns_to_keep]
    
    # Insertar en batches
    total_inserted = 0
    with engine.connect() as conn:
        for i in range(0, len(df_customers), batch_size):
            batch = df_customers.iloc[i:i+batch_size]
            batch.to_sql('customers', conn, if_exists='append', index=False, method='multi')
            total_inserted += len(batch)
            print(f"   Clientes insertados: {total_inserted:,}/{len(df_customers):,}", end='\r')
    
    print(f"\n   ✅ {total_inserted:,} clientes migrados")
    
    # ============================================================================
    # 4. MIGRAR TRANSACCIONES (en batches grandes)
    # ============================================================================
    print("\n4️⃣ Migrando transacciones...")
    print("   Cargando archivo (puede tardar un momento)...")
    
    # Leer en chunks para no sobrecargar memoria
    chunk_size = 50000
    total_transactions = 0
    
    with engine.connect() as conn:
        for chunk_num, df_chunk in enumerate(pd.read_parquet('data/transactions_unified.parquet', 
                                                              chunksize=chunk_size), 1):
            # Limpiar datos
            df_chunk = df_chunk.replace({np.nan: None})
            df_chunk['date'] = pd.to_datetime(df_chunk['date'])
            
            # Asegurar tipos correctos
            df_chunk['quantity'] = df_chunk['quantity'].astype(int)
            df_chunk['delivery_time'] = df_chunk['delivery_time'].astype(int)
            
            # Renombrar columna 'id' si existe (conflict con SQLAlchemy)
            if 'id' in df_chunk.columns:
                df_chunk = df_chunk.drop(columns=['id'])
            
            # Insertar batch
            df_chunk.to_sql('transactions', conn, if_exists='append', index=False, method='multi')
            total_transactions += len(df_chunk)
            
            print(f"   Transacciones insertadas: {total_transactions:,}", end='\r')
    
    print(f"\n   ✅ {total_transactions:,} transacciones migradas")
    
    # ============================================================================
    # 5. CREAR ÍNDICES PARA PERFORMANCE
    # ============================================================================
    print("\n5️⃣ Creando índices...")
    
    indexes = [
        "CREATE INDEX IF NOT EXISTS idx_transactions_date ON transactions(date)",
        "CREATE INDEX IF NOT EXISTS idx_transactions_customer ON transactions(customer_id)",
        "CREATE INDEX IF NOT EXISTS idx_transactions_product ON transactions(product_id)",
        "CREATE INDEX IF NOT EXISTS idx_transactions_country ON transactions(country)",
        "CREATE INDEX IF NOT EXISTS idx_transactions_category ON transactions(category)",
        "CREATE INDEX IF NOT EXISTS idx_customers_country ON customers(country)",
        "CREATE INDEX IF NOT EXISTS idx_customers_segment ON customers(rfm_segment)",
        "CREATE INDEX IF NOT EXISTS idx_products_category ON products(category)"
    ]
    
    with engine.connect() as conn:
        for idx_query in indexes:
            conn.execute(text(idx_query))
            conn.commit()
    
    print("   ✅ Índices creados")
    
    # ============================================================================
    # 6. VALIDAR MIGRACIÓN
    # ============================================================================
    print("\n6️⃣ Validando migración...")
    
    with engine.connect() as conn:
        # Contar registros
        result_trans = conn.execute(text("SELECT COUNT(*) FROM transactions")).fetchone()
        result_cust = conn.execute(text("SELECT COUNT(*) FROM customers")).fetchone()
        result_prod = conn.execute(text("SELECT COUNT(*) FROM products")).fetchone()
        
        count_trans = result_trans[0]
        count_cust = result_cust[0]
        count_prod = result_prod[0]
        
        print(f"   Transacciones en BD: {count_trans:,}")
        print(f"   Clientes en BD: {count_cust:,}")
        print(f"   Productos en BD: {count_prod:,}")
        
        # Validar rango de fechas
        date_query = text("SELECT MIN(date), MAX(date) FROM transactions")
        min_date, max_date = conn.execute(date_query).fetchone()
        print(f"\n   Rango de fechas: {min_date.date()} a {max_date.date()}")
        
        # Estadísticas rápidas
        stats_query = text("""
            SELECT 
                COUNT(*) as total_orders,
                SUM(total_amount_usd) as total_revenue,
                AVG(total_amount_usd) as avg_order_value
            FROM transactions
        """)
        stats = conn.execute(stats_query).fetchone()
        
        print(f"\n   📊 Estadísticas globales:")
        print(f"      • Total órdenes: {stats[0]:,}")
        print(f"      • Revenue total: ${stats[1]:,.2f}")
        print(f"      • AOV: ${stats[2]:.2f}")
    
    print("\n" + "=" * 80)
    print("✅ MIGRACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 80)
    print(f"\n🎉 Base de datos lista con:")
    print(f"   • {count_trans:,} transacciones")
    print(f"   • {count_cust:,} clientes")
    print(f"   • {count_prod:,} productos")
    print(f"   • Cobertura: {(max_date.year - min_date.year + 1)} años ({min_date.year}-{max_date.year})")
    
    return True

if __name__ == "__main__":
    migrate_unified_data_to_postgres()
