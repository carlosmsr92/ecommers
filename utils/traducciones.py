"""
Traducciones de categorías y subcategorías al español
"""

# Diccionario de traducción de categorías
CATEGORIAS_TRADUCCION = {
    # Categorías principales
    'Books': 'Libros',
    'Electronics': 'Electrónica',
    'Clothing': 'Ropa',
    'Home & Garden': 'Hogar y Jardín',
    'Sports': 'Deportes',
    'Toys': 'Juguetes',
    'Beauty': 'Belleza',
    'Food': 'Alimentos',
    'Health': 'Salud',
    'Automotive': 'Automotriz',
    'Office': 'Oficina',
    'Pet Supplies': 'Mascotas',
    'Music': 'Música',
    'Movies': 'Películas',
    'Games': 'Videojuegos',
    'Baby': 'Bebé',
    'Tools': 'Herramientas',
    'Jewelry': 'Joyería',
    'Shoes': 'Calzado',
    'Outdoor': 'Exterior',
    
    # Subcategorías comunes
    'book': 'libros',
    'electronics': 'electrónica',
    'clothing': 'ropa',
    'home': 'hogar',
    'garden': 'jardín',
    'sports': 'deportes',
    'toys': 'juguetes',
    'beauty': 'belleza',
    'food': 'alimentos',
    'health': 'salud',
    'automotive': 'automotriz',
    'office': 'oficina',
    'pet': 'mascotas',
    'music': 'música',
    'movies': 'películas',
    'games': 'videojuegos',
    'baby': 'bebé',
    'tools': 'herramientas',
    'jewelry': 'joyería',
    'shoes': 'calzado',
    'outdoor': 'exterior'
}

# Diccionario inverso (español -> inglés) para filtros
CATEGORIAS_INVERSO = {v: k for k, v in CATEGORIAS_TRADUCCION.items()}

def traducir_categoria(categoria):
    """Traduce una categoría del inglés al español"""
    if not categoria:
        return categoria
    
    # Buscar traducción exacta
    if categoria in CATEGORIAS_TRADUCCION:
        return CATEGORIAS_TRADUCCION[categoria]
    
    # Buscar traducción case-insensitive
    categoria_lower = categoria.lower()
    if categoria_lower in CATEGORIAS_TRADUCCION:
        return CATEGORIAS_TRADUCCION[categoria_lower]
    
    # Si no hay traducción, capitalizar la primera letra
    return categoria.capitalize()

def traducir_categoria_inverso(categoria_es):
    """Traduce una categoría del español al inglés (para filtros)"""
    if not categoria_es:
        return categoria_es
    
    if categoria_es in CATEGORIAS_INVERSO:
        return CATEGORIAS_INVERSO[categoria_es]
    
    # Si no hay traducción inversa, devolver como está
    return categoria_es

def aplicar_traducciones_df(df, columna='category'):
    """Aplica traducciones a una columna de DataFrame"""
    if columna in df.columns:
        df[columna] = df[columna].apply(traducir_categoria)
    return df

# Diccionario de labels profesionales para gráficos
LABELS_PROFESIONALES = {
    # Columnas comunes
    'total_amount_usd': 'Ingresos (USD)',
    'transaction_id': 'Transacciones',
    'profit': 'Beneficio (USD)',
    'quantity': 'Cantidad',
    'unit_price': 'Precio Unitario (USD)',
    'customer_id': 'ID Cliente',
    'product_id': 'ID Producto',
    'product_name': 'Producto',
    'category': 'Categoría',
    'subcategory': 'Subcategoría',
    'country': 'País',
    'city': 'Ciudad',
    'date': 'Fecha',
    'device_type': 'Dispositivo',
    'traffic_source': 'Fuente de Tráfico',
    'payment_method': 'Método de Pago',
    'customer_segment': 'Segmento',
    
    # RFM y segmentación
    'recency': 'Recencia (días)',
    'frequency': 'Frecuencia (compras)',
    'monetary': 'Valor Monetario (USD)',
    'rfm_segment': 'Segmento RFM',
    'churn_probability': 'Probabilidad de Churn (%)',
    'lifetime_value': 'Valor de Vida (USD)',
    'count': 'Cantidad',
    'value': 'Valor',
    
    # Análisis especiales
    'margen_%': 'Margen (%)',
    'churn_risk': 'Riesgo de Churn (%)',
    'ltv': 'Valor de Vida (USD)',
    'aov': 'Ticket Promedio (USD)',
    'es_anomalia': 'Anomalía',
    
    # Temporal
    'dia_semana': 'Día de la Semana',
    'hora': 'Hora del Día',
    'mes': 'Mes',
    'año': 'Año',
    'periodo': 'Período',
    'Fecha': 'Fecha',
    'Ingresos': 'Ingresos (USD)',
    'Pedidos': 'Pedidos',
    'Beneficio': 'Beneficio (USD)',
    
    # Agregaciones
    'ingresos': 'Ingresos (USD)',
    'pedidos': 'Pedidos',
    'beneficio': 'Beneficio (USD)',
    'cantidad': 'Cantidad',
    'clientes': 'Clientes',
    'productos': 'Productos',
    'producto': 'Producto',
    'transacciones': 'Transacciones',
    'metodo': 'Método de Pago',
    'segmento': 'Segmento',
    'nivel_riesgo': 'Nivel de Riesgo',
    'cluster': 'Cluster',
    'cuadrante': 'Cuadrante BCG',
    'velocidad': 'Velocidad de Rotación',
    'frecuencia': 'Frecuencia'
}

def obtener_labels_profesionales():
    """Retorna diccionario de labels profesionales para gráficos"""
    return LABELS_PROFESIONALES.copy()
