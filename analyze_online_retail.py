import pandas as pd

df = pd.read_excel('data/Online Retail.xlsx')

print('📊 RESUMEN DEL DATASET "Online Retail"')
print('=' * 70)
print(f'Total de registros: {len(df):,}')
print(f'Total de columnas: {len(df.columns)}')
print(f'\n📋 Columnas:')
for col in df.columns:
    print(f'  - {col} ({df[col].dtype})')

print(f'\n📅 Período de datos:')
print(f'  Desde: {df["InvoiceDate"].min()}')
print(f'  Hasta: {df["InvoiceDate"].max()}')

print(f'\n🔢 Datos únicos:')
print(f'  Clientes únicos: {df["CustomerID"].nunique():,}')
print(f'  Productos únicos: {df["StockCode"].nunique():,}')
print(f'  Facturas únicas: {df["InvoiceNo"].nunique():,}')
print(f'  Países: {df["Country"].nunique()}')

print(f'\n🌍 Top 10 países por transacciones:')
print(df["Country"].value_counts().head(10))

print(f'\n💰 Estadísticas de precios:')
print(f'  Precio mínimo: ${df["UnitPrice"].min():.2f}')
print(f'  Precio máximo: ${df["UnitPrice"].max():.2f}')
print(f'  Precio promedio: ${df["UnitPrice"].mean():.2f}')

print(f'\n📦 Estadísticas de cantidad:')
print(f'  Cantidad mínima: {df["Quantity"].min()}')
print(f'  Cantidad máxima: {df["Quantity"].max()}')
print(f'  Cantidad promedio: {df["Quantity"].mean():.1f}')

print(f'\n🛍️ Productos más vendidos (Top 10):')
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
for product, qty in top_products.items():
    print(f'  {product}: {qty:,} unidades')

print(f'\n✅ Archivo leído exitosamente!')
