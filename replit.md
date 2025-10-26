# Global Ecommerce Analytics Platform

## 📋 Descripción del Proyecto

Dashboard profesional de Business Intelligence para análisis global de ecommerce que integra:

- ✅ **Business Intelligence**: KPIs avanzados, análisis multidimensional
- ✅ **Big Data**: Procesamiento de 100,000 transacciones, 50,000 clientes, 500 productos
- ✅ **Machine Learning**: Modelos predictivos (forecasting, clustering, churn)
- ✅ **Análisis Geoespacial**: Mapas interactivos de ventas por país/región
- ✅ **API RESTful**: FastAPI con documentación Swagger
- ✅ **Base de Datos**: PostgreSQL para persistencia optimizada
- ✅ **Exportación**: Reportes PDF y Excel profesionales

## 🏗️ Arquitectura del Sistema

### Stack Tecnológico

**Frontend:**
- Streamlit - Dashboard interactivo (Puerto 5000)
- Plotly - Gráficos avanzados e interactivos
- Folium - Mapas geoespaciales

**Backend:**
- FastAPI - API RESTful (Puerto 8000)
- PostgreSQL - Base de datos principal
- SQLAlchemy - ORM

**Machine Learning:**
- Prophet - Forecasting de series temporales
- Scikit-learn - Clustering (K-Means), Anomaly Detection (Isolation Forest)
- XGBoost - Modelos de predicción avanzados

**Exportación:**
- ReportLab - Generación de PDFs
- OpenPyXL - Exportación a Excel

### Estructura del Proyecto

```
ecommerce-ai-dashboard/
├── app.py                     # Dashboard Streamlit principal
├── api/
│   ├── main.py               # API FastAPI principal
│   └── ml_endpoints.py       # Endpoints de Machine Learning
├── database/
│   ├── schema.py             # Modelos SQLAlchemy
│   └── migration.py          # Script de migración de datos
├── utils/
│   ├── data_generator.py     # Generación de datos sintéticos
│   ├── data_loader.py        # Carga de datos desde Parquet
│   ├── data_loader_pg.py     # Carga de datos desde PostgreSQL
│   └── export_utils.py       # Utilidades de exportación
└── data/                      # Datos en formato Parquet (backup)
```

## 🚀 Características Implementadas

### 1. Dashboard Interactivo (Streamlit)

**KPIs Principales (8 tarjetas):**
- Total Revenue con comparación vs periodo anterior
- Total Orders con % de cambio
- Average Order Value (AOV)
- Gross Profit y margen
- Total Customers con nuevos clientes
- Conversion Rate
- Customer Lifetime Value (LTV)
- Churn Rate

**Análisis Geoespacial:**
- Mapa mundial choropleth coloreado por revenue
- Top 15 países con tablas ranking
- Treemap jerárquico: País → Ciudad → Categoría
- Gráfico de concentración de ventas (pie/donut)

**Forecasting & Tendencias:**
- Serie temporal de revenue y orders con granularidad ajustable (día/semana/mes)
- Forecasting de 90 días con Prophet
- Bandas de confianza 95% y 80%
- Métricas del modelo: MAPE, RMSE, R²
- Análisis de growth rate y distribución de revenue

**Análisis de Productos:**
- Product Performance Matrix (BCG) - Stars, Cash Cows, Question Marks, Dogs
- Top 20 productos con métricas detalladas
- Revenue by category (treemap)
- Análisis de margen y profit por categoría

**Segmentación de Clientes:**
- RFM Analysis con 11 segmentos (Champions, Loyal, At Risk, etc.)
- Customer Lifetime Value distribution con percentiles
- Cohort Analysis con heatmap de retention rates
- Churn Prediction con top 100 clientes en riesgo

**ML Insights:**
- Customer Clustering con K-Means y reducción PCA
- Anomaly Detection con Isolation Forest
- Channel Performance Analysis (device, traffic source, payment methods)

**Tablas Detalladas:**
- DataTable interactiva con todas las transacciones
- Paginación (50/100/500/1000 filas)
- Descarga en CSV

### 2. API RESTful (FastAPI)

**Documentación:** http://localhost:8000/docs (Swagger UI)

**Endpoints de Datos:**

```
GET /api/kpis
- Obtiene KPIs principales
- Parámetros: start_date, end_date, country, category
- Retorna: revenue, orders, AOV, profit, customers, conversion rate

GET /api/transactions
- Lista transacciones con paginación
- Parámetros: limit, offset, country, category, start_date, end_date
- Retorna: array de transacciones con metadata

GET /api/customers
- Lista clientes con filtros
- Parámetros: limit, offset, country, rfm_segment, min_ltv
- Retorna: datos de clientes

GET /api/products
- Lista productos
- Parámetros: limit, offset, category, min_rating
- Retorna: catálogo de productos

GET /api/analytics/countries
- Análisis agregado por país
- Retorna: revenue, orders, AOV, customers por país

GET /api/analytics/categories
- Análisis agregado por categoría
- Retorna: revenue, profit, margin por categoría

GET /api/analytics/time-series
- Serie temporal de métricas
- Parámetros: granularity (day/week/month), start_date, end_date
- Retorna: serie temporal de revenue y orders

GET /api/analytics/top-products
- Top productos por métrica
- Parámetros: limit, metric (revenue/orders/margin)
- Retorna: ranking de productos
```

**Endpoints de Machine Learning:**

```
POST /api/ml/forecast
- Genera forecast con Prophet
- Parámetros: days_ahead (7-180), metric (revenue/orders)
- Retorna: predicciones, bandas de confianza, métricas del modelo

GET /api/ml/clustering/customers
- Clustering de clientes con K-Means
- Parámetros: n_clusters (3-10)
- Retorna: clusters con características y tamaño

GET /api/ml/churn/at-risk
- Clientes con alto riesgo de churn
- Parámetros: threshold (0.5-0.9), limit
- Retorna: clientes en riesgo con acciones recomendadas

GET /api/ml/recommendations/{product_id}
- Recomendaciones de productos (Market Basket Analysis)
- Parámetros: product_id, top_n (5-20)
- Retorna: productos recomendados con scores

GET /api/ml/demand-forecast
- Forecast de demanda por producto
- Parámetros: top_n
- Retorna: forecast 30/60/90 días, stock-out risk, recomendaciones de reorder

GET /api/ml/anomalies
- Detección de anomalías con Isolation Forest
- Parámetros: contamination (0.01-0.1), days_back (30-365)
- Retorna: anomalías detectadas con severity level
```

**Endpoints de Exportación:**

```
GET /api/export/excel
- Exporta reporte completo en Excel
- Parámetros: start_date, end_date, country, category
- Retorna: archivo .xlsx con 8 hojas de análisis

GET /api/export/pdf
- Exporta reporte en PDF profesional
- Parámetros: start_date, end_date, country, category
- Retorna: archivo .pdf con tablas y gráficos
```

### 3. Base de Datos PostgreSQL

**Tablas:**

```sql
transactions (100,000 registros)
- transaction_id, date, customer_id, country, region, city
- product_id, product_name, category, subcategory
- quantity, unit_price, total_amount, discount_applied
- payment_method, shipping_cost, delivery_time
- customer_segment, device_type, traffic_source
- currency, exchange_rate, total_amount_usd
- cost_price, profit

customers (50,000 registros)
- customer_id, registration_date, country, age, gender
- lifetime_value, total_orders, avg_order_value
- last_purchase_date, recency_score, frequency_score, monetary_score
- rfm_segment, churn_probability, preferred_category

products (500 registros)
- product_id, product_name, category, subcategory, brand
- base_price, cost_price, margin_percentage
- stock_quantity, supplier_country, weight
- rating, reviews_count, launch_date
```

**Índices Optimizados:**
- Índices en: transaction_id, customer_id, product_id, date, country, category
- Índices para consultas frecuentes y JOINs

### 4. Sistema de Filtros Avanzados

El sidebar incluye filtros dinámicos que se aplican a todo el dashboard:

- 📅 Periodo: Today, Last 7 Days, Last 30 Days, Last 90 Days, Last Year, All Time
- 🌍 País/Región/Ciudad (multi-select)
- 📦 Categoría/Subcategoría
- 👥 Segmento de cliente (VIP, Regular, New, At-Risk)
- 💳 Método de pago
- 📱 Tipo de dispositivo
- 🎯 Fuente de tráfico
- 💰 Rango de precio (slider)
- 🤖 Toggle para mostrar/ocultar predicciones ML

### 5. Exportación de Reportes

**Excel (8 hojas):**
1. Resumen - KPIs principales
2. Transacciones - Últimas 1000 transacciones
3. Por País - Análisis agregado por país
4. Por Categoría - Análisis de categorías con márgenes
5. Top 100 Productos - Ranking de productos
6. Clientes VIP - Top 100 clientes por LTV
7. Segmentación RFM - Análisis por segmento
8. Serie Temporal - Revenue y orders últimos 90 días

**PDF:**
- Reporte profesional con branding
- Tablas formateadas con colores
- KPIs resumidos
- Top 10 países y productos
- Análisis por categoría

**CSV:**
- Descarga directa de transacciones filtradas
- Compatible con Excel y herramientas de análisis

## 📊 Datos Generados

El sistema genera automáticamente datos sintéticos realistas:

**Características de los Datos:**
- 100,000 transacciones en últimos 24 meses
- 50,000 clientes únicos
- 500 productos en 8 categorías
- 13 países con distribución realista (USA 35%, UK 12%, etc.)
- Estacionalidad (picos en Nov-Dec para Black Friday/Navidad)
- Distribución realista de precios por categoría
- RFM scores calculados automáticamente
- Churn probability basada en recency

**Categorías de Productos:**
1. Electronics (Smartphones, Laptops, Tablets, Headphones, Cameras)
2. Fashion (Clothing, Shoes, Accessories, Jewelry)
3. Home (Furniture, Kitchen, Decor, Bedding)
4. Sports (Fitness, Outdoor, Team Sports, Cycling, Yoga)
5. Books (Fiction, Non-Fiction, Educational, Comics)
6. Beauty (Skincare, Makeup, Haircare, Fragrance)
7. Toys (Action Figures, Board Games, Educational)
8. Groceries (Snacks, Beverages, Organic, Frozen)

## 🔧 Uso del Sistema

### Acceder al Dashboard
```
URL: http://localhost:5000
```

### Acceder a la API
```
URL: http://localhost:8000
Documentación Swagger: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc
```

### Ejemplo de Uso de la API

```python
import requests

# Obtener KPIs
response = requests.get('http://localhost:8000/api/kpis', params={
    'start_date': '2024-01-01',
    'end_date': '2024-12-31',
    'country': 'USA'
})
kpis = response.json()
print(f"Revenue: ${kpis['total_revenue']:,.2f}")

# Generar forecast
forecast_response = requests.post('http://localhost:8000/api/ml/forecast', params={
    'days_ahead': 90,
    'metric': 'revenue'
})
forecast = forecast_response.json()
print(f"MAPE: {forecast['model_metrics']['mape']}%")

# Obtener recomendaciones de productos
rec_response = requests.get('http://localhost:8000/api/ml/recommendations/P00001', params={
    'top_n': 10
})
recommendations = rec_response.json()
for rec in recommendations['recommendations']:
    print(f"{rec['product_name']}: {rec['score']}% similarity")

# Descargar reporte Excel
excel_response = requests.get('http://localhost:8000/api/export/excel', params={
    'start_date': '2024-01-01',
    'end_date': '2024-12-31'
})
with open('report.xlsx', 'wb') as f:
    f.write(excel_response.content)
```

## ✅ Estado del Proyecto

**Estado:** PRODUCCIÓN READY 🚀

El proyecto está completamente funcional y listo para deployment:
- ✅ 100,000 transacciones migradas a PostgreSQL
- ✅ Dashboard interactivo con 8 KPIs y 6 tabs de análisis
- ✅ API RESTful con 20+ endpoints documentados (Swagger)
- ✅ 6 modelos de Machine Learning operacionales
- ✅ Sistema de exportación PDF/Excel completo
- ✅ Seguridad verificada (sin SQL injection)
- ✅ Tests end-to-end pasando exitosamente
- ✅ Workflows corriendo estables (Dashboard:5000, API:8000)

## 🎯 Mejoras Futuras (No Implementadas)

- Redis para caching de queries frecuentes
- WebSockets para updates en tiempo real
- Sistema de alertas automáticas (email/Slack)
- Deep Learning para recomendaciones más precisas
- A/B testing framework
- Multi-tenancy para múltiples empresas
- Autenticación y autorización (OAuth2)
- Dashboards personalizables por usuario
- Rate limiting para endpoints de API

## 📝 Notas Técnicas

**Performance:**
- Carga inicial del dashboard: ~3-5 segundos
- PostgreSQL indexado para queries rápidas
- Caching de Streamlit para datos frecuentes (@st.cache_data)
- Prophet training: ~2-3 segundos para 700+ datos históricos

**Escalabilidad:**
- Diseñado para manejar 100K+ transacciones
- API puede escalar horizontalmente
- Base de datos optimizada con índices

**Seguridad:**
- Variables de entorno para credenciales (DATABASE_URL, SESSION_SECRET)
- No hay API keys hardcodeadas
- CORS configurado para producción
- **SQL Injection Protection:** Todas las consultas SQL usan parámetros vinculados (SQLAlchemy text() con params) en lugar de interpolación de strings
- **Input Validation:** Whitelist approach para valores dinámicos (granularity, metric)
- **Parameterized Queries:** Todos los endpoints de API (main.py y ml_endpoints.py) usan consultas parametrizadas seguras
- **Array Binding:** Listas de IDs usan ANY() con parámetros vinculados para prevenir inyección

## 🐛 Troubleshooting

**Dashboard no carga:**
- Verificar que PostgreSQL esté funcionando: `echo $DATABASE_URL`
- Verificar logs del workflow Dashboard

**API no responde:**
- Verificar que el workflow API esté corriendo en puerto 8000
- Revisar logs: `/tmp/logs/API_*.log`

**Datos no se muestran:**
- Ejecutar migración manual: `python -c "from database.migration import migrate_data_to_postgres; migrate_data_to_postgres()"`

**Exportación falla:**
- Verificar que ReportLab y OpenPyXL estén instalados
- Revisar permisos de escritura

## 🎓 Créditos

Dashboard creado siguiendo mejores prácticas de:
- Business Intelligence y Data Analytics
- Machine Learning en producción
- API RESTful design
- Visualización de datos interactiva

**Librerías Principales:**
- Streamlit, FastAPI, SQLAlchemy
- Plotly, Folium, Matplotlib
- Prophet, Scikit-learn, XGBoost
- Pandas, NumPy
- ReportLab, OpenPyXL
