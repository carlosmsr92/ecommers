"""
Script unificado para integrar datos reales (Online Retail 2010-2011)
con datos sintéticos (2023-2025) y generar datos para el gap temporal (2012-2023)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from faker import Faker
import random

fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

print("🔄 INTEGRACIÓN UNIFICADA DE DATOS")
print("=" * 80)

# ============================================================================
# 1. CARGAR DATOS REALES (2010-2011)
# ============================================================================
print("\n1️⃣ Cargando datos reales del Online Retail (2010-2011)...")
df_real = pd.read_csv('data/dataUK.csv', encoding='ISO-8859-1')
df_real['InvoiceDate'] = pd.to_datetime(df_real['InvoiceDate'])

# Limpiar datos
df_real = df_real[df_real['Quantity'] > 0]  # Solo ventas positivas
df_real = df_real[df_real['UnitPrice'] > 0]  # Precios válidos
df_real = df_real.dropna(subset=['CustomerID'])  # Solo con customer ID

print(f"   ✅ {len(df_real):,} transacciones reales cargadas")
print(f"   Período: {df_real['InvoiceDate'].min().date()} a {df_real['InvoiceDate'].max().date()}")

# ============================================================================
# 2. MAPEAR CATEGORÍAS DE PRODUCTOS REALES
# ============================================================================
print("\n2️⃣ Mapeando productos reales a categorías...")

# Definir keywords para categorizar productos automáticamente
category_keywords = {
    'Electronics': ['PHONE', 'CAMERA', 'LAPTOP', 'TABLET', 'HEADPHONE', 'CHARGER', 'CABLE'],
    'Fashion': ['T-SHIRT', 'SHIRT', 'DRESS', 'SHOE', 'BAG', 'PURSE', 'GLOVE', 'SCARF', 'HAT'],
    'Home': ['LAMP', 'CUSHION', 'CANDLE', 'HOLDER', 'FRAME', 'VASE', 'BOWL', 'PLATE', 'CUP', 'MUG', 'STORAGE', 'BOX', 'BASKET'],
    'Beauty': ['SOAP', 'CREAM', 'LOTION', 'PERFUME', 'MAKEUP', 'BRUSH'],
    'Toys': ['TOY', 'GAME', 'DOLL', 'TEDDY', 'PUZZLE', 'BALL'],
    'Books': ['BOOK', 'NOTEBOOK', 'DIARY', 'CARD'],
    'Sports': ['BALL', 'BIKE', 'FITNESS', 'YOGA', 'SPORT'],
    'Groceries': ['TEA', 'COFFEE', 'CHOCOLATE', 'CAKE', 'BISCUIT']
}

def categorize_product(description):
    """Categoriza un producto basándose en su descripción"""
    if pd.isna(description):
        return 'Home', 'Decor'
    
    desc_upper = str(description).upper()
    
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in desc_upper:
                # Subcategorías simples
                if category == 'Electronics':
                    return category, 'Gadgets'
                elif category == 'Fashion':
                    return category, 'Accessories'
                elif category == 'Home':
                    return category, 'Decor'
                else:
                    return category, 'General'
    
    # Default
    return 'Home', 'Decor'

# Aplicar categorización
df_real[['category', 'subcategory']] = df_real['Description'].apply(
    lambda x: pd.Series(categorize_product(x))
)

print(f"   ✅ Categorías asignadas:")
for cat, count in df_real['category'].value_counts().head(5).items():
    print(f"      - {cat}: {count:,} ({count/len(df_real)*100:.1f}%)")

# ============================================================================
# 3. CREAR MAPEOS DE IDS
# ============================================================================
print("\n3️⃣ Creando mapeos de IDs...")

# Productos: StockCode → product_id
unique_products = df_real[['StockCode', 'Description', 'category', 'subcategory', 'UnitPrice']].drop_duplicates(subset=['StockCode'])
product_mapping = {}
for idx, (stock_code, desc, cat, subcat, price) in enumerate(zip(
    unique_products['StockCode'],
    unique_products['Description'],
    unique_products['category'],
    unique_products['subcategory'],
    unique_products['UnitPrice']
), start=1):
    product_mapping[stock_code] = {
        'product_id': f'R{idx:05d}',  # R para Real
        'product_name': desc if pd.notna(desc) else f'Product {stock_code}',
        'category': cat,
        'subcategory': subcat,
        'base_price': float(price)
    }

# Clientes: CustomerID → customer_id
unique_customers = df_real['CustomerID'].unique()
customer_mapping = {}
for idx, cust_id in enumerate(unique_customers, start=1):
    customer_mapping[cust_id] = f'R{idx:05d}'  # R para Real

print(f"   ✅ {len(product_mapping):,} productos mapeados")
print(f"   ✅ {len(customer_mapping):,} clientes mapeados")

# ============================================================================
# 4. TRANSFORMAR DATOS REALES AL ESQUEMA UNIFICADO
# ============================================================================
print("\n4️⃣ Transformando datos reales al esquema unificado...")

transactions_real = []

for idx, row in df_real.iterrows():
    if idx % 50000 == 0:
        print(f"   Procesando: {idx:,}/{len(df_real):,}", end='\r')
    
    stock_code = row['StockCode']
    if stock_code not in product_mapping:
        continue
    
    product = product_mapping[stock_code]
    customer_id = customer_mapping.get(row['CustomerID'], 'R00001')
    
    # Calcular valores
    quantity = int(row['Quantity'])
    unit_price = float(row['UnitPrice'])
    total_amount = quantity * unit_price
    discount = 0  # Dataset real no tiene descuentos explícitos
    cost_price = unit_price * 0.65  # Asumimos 35% margen
    profit = total_amount - (cost_price * quantity)
    
    # País y región
    country = row['Country']
    if country == 'United Kingdom':
        region = random.choice(['London', 'Manchester', 'Birmingham', 'Liverpool', 'Leeds'])
        city = region
    elif country == 'Germany':
        region = random.choice(['Berlin', 'Munich', 'Hamburg', 'Frankfurt'])
        city = region
    elif country == 'France':
        region = random.choice(['Paris', 'Lyon', 'Marseille', 'Nice'])
        city = region
    else:
        region = country
        city = country
    
    transaction = {
        'transaction_id': f"R{idx+1:07d}",
        'date': row['InvoiceDate'],
        'customer_id': customer_id,
        'country': country,
        'region': region,
        'city': city,
        'product_id': product['product_id'],
        'product_name': product['product_name'],
        'category': product['category'],
        'subcategory': product['subcategory'],
        'quantity': quantity,
        'unit_price': unit_price,
        'total_amount': total_amount,
        'discount_applied': discount,
        'payment_method': random.choice(['Credit Card', 'Debit Card', 'PayPal']),
        'shipping_cost': round(random.uniform(5, 25), 2) if total_amount > 50 else 0,
        'delivery_time': random.randint(2, 10),
        'customer_segment': random.choice(['Regular', 'VIP', 'New']),
        'device_type': random.choice(['Desktop', 'Mobile', 'Tablet']),
        'traffic_source': random.choice(['Organic', 'Direct', 'Paid Ads']),
        'currency': 'GBP',
        'exchange_rate': 1.25,  # GBP to USD aproximado
        'total_amount_usd': total_amount * 1.25,
        'cost_price': cost_price,
        'profit': profit
    }
    
    transactions_real.append(transaction)

df_transactions_real = pd.DataFrame(transactions_real)
print(f"\n   ✅ {len(df_transactions_real):,} transacciones reales transformadas")

# ============================================================================
# 5. CARGAR DATOS SINTÉTICOS ACTUALES (2023-2025)
# ============================================================================
print("\n5️⃣ Cargando datos sintéticos actuales (2023-2025)...")
df_synthetic = pd.read_parquet('data/transactions.parquet')
print(f"   ✅ {len(df_synthetic):,} transacciones sintéticas cargadas")
print(f"   Período: {df_synthetic['date'].min().date()} a {df_synthetic['date'].max().date()}")

# ============================================================================
# 6. GENERAR DATOS PARA EL GAP TEMPORAL (2012-2023)
# ============================================================================
print("\n6️⃣ Generando datos para el gap temporal (2012-2023)...")
print("   Esto creará una evolución coherente entre datasets...")

# Parámetros de generación
start_gap = pd.Timestamp('2012-01-01')
end_gap = pd.Timestamp('2022-12-31')
years_gap = 11

# Calcular transacciones por año con crecimiento gradual
# 2011: ~541K transacciones anuales
# 2023: ~50K transacciones anuales (sintéticos)
# Generaremos cantidades moderadas para mantener performance

transactions_per_year = {
    2012: 35000,
    2013: 32000,
    2014: 30000,
    2015: 28000,
    2016: 26000,
    2017: 24000,
    2018: 22000,
    2019: 20000,
    2020: 18000,  # COVID impact
    2021: 16000,
    2022: 15000
}

total_gap_transactions = sum(transactions_per_year.values())
print(f"   Generando {total_gap_transactions:,} transacciones para 2012-2022")

# Reutilizar productos y clientes de ambos datasets
all_products_real = list(product_mapping.values())
all_customers_real = list(customer_mapping.values())

# Obtener también productos sintéticos
synthetic_products = df_synthetic[['product_id', 'product_name', 'category', 'subcategory']].drop_duplicates()
synthetic_customers = df_synthetic['customer_id'].unique()

gap_transactions = []
transaction_counter = len(df_transactions_real) + 1

for year, num_transactions in transactions_per_year.items():
    print(f"   Generando año {year}: {num_transactions:,} transacciones...", end='\r')
    
    # Distribución temporal dentro del año
    year_start = pd.Timestamp(f'{year}-01-01')
    year_end = pd.Timestamp(f'{year}-12-31')
    
    for _ in range(num_transactions):
        # Fecha aleatoria en el año
        days_in_year = (year_end - year_start).days
        random_day = random.randint(0, days_in_year)
        date = year_start + timedelta(days=random_day, 
                                       hours=random.randint(8, 20),
                                       minutes=random.randint(0, 59))
        
        # Mix de productos reales y sintéticos (favoreciendo reales en años tempranos)
        use_real_product = random.random() < (1 - (year - 2012) / 11 * 0.5)
        
        if use_real_product and all_products_real:
            product = random.choice(all_products_real)
            product_id = product['product_id']
            product_name = product['product_name']
            category = product['category']
            subcategory = product['subcategory']
            unit_price = product['base_price'] * (1 + (year - 2012) * 0.03)  # Inflación 3% anual
        else:
            prod_row = synthetic_products.sample(n=1).iloc[0]
            product_id = prod_row['product_id']
            product_name = prod_row['product_name']
            category = prod_row['category']
            subcategory = prod_row['subcategory']
            unit_price = round(random.uniform(10, 500), 2)
        
        # Mix de clientes
        use_real_customer = random.random() < 0.7
        customer_id = random.choice(all_customers_real) if use_real_customer else random.choice(synthetic_customers)
        
        # Cantidad y cálculos
        quantity = random.randint(1, 10)
        discount = round(random.uniform(0, 0.2), 2) if random.random() < 0.3 else 0
        total_amount = quantity * unit_price * (1 - discount)
        cost_price = unit_price * 0.65
        profit = total_amount - (cost_price * quantity)
        
        # País (basado en distribución histórica)
        country_weights = {
            'USA': 0.35, 'UK': 0.12, 'Germany': 0.10, 'France': 0.08,
            'Canada': 0.07, 'Spain': 0.05, 'Italy': 0.05, 'Netherlands': 0.04,
            'Belgium': 0.03, 'Switzerland': 0.03, 'Sweden': 0.03, 'Norway': 0.03, 'Denmark': 0.02
        }
        country = random.choices(list(country_weights.keys()), weights=list(country_weights.values()))[0]
        
        # Región y ciudad simplificadas
        region = country
        city = country
        
        transaction = {
            'transaction_id': f"G{transaction_counter:07d}",  # G para Gap
            'date': date,
            'customer_id': customer_id,
            'country': country,
            'region': region,
            'city': city,
            'product_id': product_id,
            'product_name': product_name[:100] if pd.notna(product_name) else 'Product',
            'category': category,
            'subcategory': subcategory,
            'quantity': quantity,
            'unit_price': unit_price,
            'total_amount': total_amount,
            'discount_applied': discount,
            'payment_method': random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Google Pay', 'Apple Pay']),
            'shipping_cost': round(random.uniform(5, 30), 2),
            'delivery_time': random.randint(2, 15),
            'customer_segment': random.choice(['Regular', 'VIP', 'New', 'At-Risk']),
            'device_type': random.choice(['Desktop', 'Mobile', 'Tablet']),
            'traffic_source': random.choice(['Organic', 'Direct', 'Paid Ads', 'Social Media']),
            'currency': 'USD',
            'exchange_rate': 1.0,
            'total_amount_usd': total_amount,
            'cost_price': cost_price,
            'profit': profit
        }
        
        gap_transactions.append(transaction)
        transaction_counter += 1

df_gap = pd.DataFrame(gap_transactions)
print(f"\n   ✅ {len(df_gap):,} transacciones del gap generadas")

# ============================================================================
# 7. COMBINAR TODOS LOS DATASETS
# ============================================================================
print("\n7️⃣ Combinando todos los datasets...")

# Asegurar que todos tengan las mismas columnas
all_columns = set(df_transactions_real.columns) | set(df_synthetic.columns) | set(df_gap.columns)
for col in all_columns:
    if col not in df_transactions_real.columns:
        df_transactions_real[col] = None
    if col not in df_synthetic.columns:
        df_synthetic[col] = None
    if col not in df_gap.columns:
        df_gap[col] = None

# Combinar
df_unified = pd.concat([df_transactions_real, df_gap, df_synthetic], ignore_index=True)
df_unified = df_unified.sort_values('date').reset_index(drop=True)

print(f"\n   ✅ Dataset unificado creado:")
print(f"      • Total transacciones: {len(df_unified):,}")
print(f"      • Período: {df_unified['date'].min().date()} a {df_unified['date'].max().date()}")
print(f"      • Años cubiertos: {(df_unified['date'].max().year - df_unified['date'].min().year + 1)} años")
print(f"\n   📊 Distribución por origen:")
print(f"      • Datos reales (2010-2011): {len(df_transactions_real):,}")
print(f"      • Datos gap (2012-2022): {len(df_gap):,}")
print(f"      • Datos sintéticos (2023-2025): {len(df_synthetic):,}")

# ============================================================================
# 8. GUARDAR DATASET UNIFICADO
# ============================================================================
print("\n8️⃣ Guardando dataset unificado...")
df_unified.to_parquet('data/transactions_unified.parquet', index=False)
print(f"   ✅ Guardado en data/transactions_unified.parquet")

# Guardar también información de productos y clientes
print("\n9️⃣ Generando catálogos de productos y clientes...")

# Productos unificados
all_products = df_unified[['product_id', 'product_name', 'category', 'subcategory']].drop_duplicates()
all_products['base_price'] = df_unified.groupby('product_id')['unit_price'].mean()
all_products['brand'] = 'Various'
all_products['cost_price'] = all_products['base_price'] * 0.65
all_products['margin_percentage'] = 35.0
all_products['stock_quantity'] = np.random.randint(50, 1000, size=len(all_products))
all_products['supplier_country'] = 'UK'
all_products['weight'] = np.round(np.random.uniform(0.1, 5.0, size=len(all_products)), 2)
all_products['rating'] = np.round(np.random.uniform(3.0, 5.0, size=len(all_products)), 1)
all_products['reviews_count'] = np.random.randint(10, 1000, size=len(all_products))
all_products['launch_date'] = pd.Timestamp('2010-01-01')

all_products.to_parquet('data/products_unified.parquet', index=False)
print(f"   ✅ {len(all_products):,} productos guardados")

# Clientes unificados
all_customers_list = df_unified['customer_id'].unique()
customers_data = []

for cust_id in all_customers_list:
    cust_transactions = df_unified[df_unified['customer_id'] == cust_id]
    
    customers_data.append({
        'customer_id': cust_id,
        'registration_date': cust_transactions['date'].min(),
        'country': cust_transactions['country'].mode()[0] if len(cust_transactions) > 0 else 'USA',
        'age': random.randint(18, 70),
        'gender': random.choice(['Male', 'Female']),
        'lifetime_value': cust_transactions['total_amount_usd'].sum(),
        'total_orders': len(cust_transactions),
        'avg_order_value': cust_transactions['total_amount_usd'].mean(),
        'last_purchase_date': cust_transactions['date'].max(),
        'recency_score': 5,
        'frequency_score': min(len(cust_transactions) // 10, 5),
        'monetary_score': 5,
        'rfm_segment': 'Regular',
        'churn_probability': 0.3,
        'preferred_category': cust_transactions['category'].mode()[0] if len(cust_transactions) > 0 else 'Home'
    })

df_customers_unified = pd.DataFrame(customers_data)
df_customers_unified.to_parquet('data/customers_unified.parquet', index=False)
print(f"   ✅ {len(df_customers_unified):,} clientes guardados")

print("\n" + "=" * 80)
print("✅ INTEGRACIÓN COMPLETADA EXITOSAMENTE")
print("=" * 80)
print(f"\n📊 RESUMEN FINAL:")
print(f"   • Transacciones totales: {len(df_unified):,}")
print(f"   • Productos únicos: {len(all_products):,}")
print(f"   • Clientes únicos: {len(df_customers_unified):,}")
print(f"   • Período temporal: {df_unified['date'].min().date()} a {df_unified['date'].max().date()}")
print(f"   • Años cubiertos: {(df_unified['date'].max().year - df_unified['date'].min().year + 1)} años")
print(f"\n🎯 Archivos generados:")
print(f"   • data/transactions_unified.parquet")
print(f"   • data/products_unified.parquet")
print(f"   • data/customers_unified.parquet")
print(f"\n🚀 Listo para migración a PostgreSQL!")
