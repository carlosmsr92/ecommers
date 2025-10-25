# Proyecto Profesional: Dashboard Avanzado de Ecommerce con IA, Big Data y Análisis Predictivo

## 🎯 Descripción del Proyecto

Dashboard profesional de Business Intelligence para análisis global de ecommerce que integra:

- ✅ **Business Intelligence**: KPIs avanzados, análisis multidimensional
- ✅ **Big Data**: Procesamiento de millones de transacciones
- ✅ **Machine Learning**: Modelos predictivos (forecasting, clustering, churn)
- ✅ **Análisis Geoespacial**: Mapas interactivos de ventas por país/región
- ✅ **Proyecciones Precisas**: Prophet + ARIMA para forecasting
- ✅ **Segmentación Inteligente**: Clustering de clientes con K-Means
- ✅ **Recomendaciones**: Sistema de recomendación de productos
- ✅ **Alertas Automáticas**: Detección de anomalías en ventas

---

## 📊 ARQUITECTURA DEL PROYECTO

### Stack Tecnológico Profesional

**Frontend & Visualización:**
- Streamlit (Python) - Dashboard interactivo
- Plotly + Folium - Gráficos avanzados + mapas
- Altair - Visualizaciones estadísticas

**Data Processing & Big Data:**
- Pandas + NumPy - Manipulación datos
- Dask - Procesamiento paralelo Big Data
- PySpark (opcional) - Distributed computing

**Machine Learning & AI:**
- Scikit-learn - Modelos ML (clustering, classification)
- Prophet - Forecasting avanzado (Facebook)
- XGBoost - Gradient boosting (predicciones precisas)
- TensorFlow/Keras (opcional) - Deep Learning

**Base de Datos:**
- PostgreSQL - Datos estructurados
- MongoDB (opcional) - Datos no estructurados
- Redis - Cache para queries rápidas

**APIs & Integración:**
- Shopify API - Datos reales ecommerce
- Google Analytics API - Métricas web
- Stripe API - Transacciones financieras

---

## PARTE 1: PROYECTO AVANZADO CON REPLIT AGENT

### Prompt Profesional Optimizado

Copia y pega este prompt completo en **Replit Agent**:

```
Crea un dashboard avanzado de Business Intelligence para análisis global de ecommerce con las siguientes características profesionales:

=== ARQUITECTURA ===
Backend: Python FastAPI
Frontend: HTML5 + JavaScript + Chart.js + D3.js
Base datos: PostgreSQL con 100,000+ registros simulados
Cache: Redis para queries frecuentes
API RESTful para todas las operaciones

=== DATOS SIMULADOS PROFESIONALES ===
Genera dataset realista de ecommerce global con:

TRANSACCIONES (100,000 filas):
- transaction_id (UUID único)
- date (últimos 24 meses, hourly granularity)
- customer_id (50,000 clientes únicos)
- country (30 países: USA, UK, Germany, France, Spain, Italy, Canada, Australia, Brazil, Mexico, etc.)
- region (state/province para análisis regional)
- city (principales ciudades por país)
- product_id (500 productos únicos)
- product_name (nombres realistas por categoría)
- category (Electronics, Fashion, Home, Sports, Books, Beauty, Toys, Groceries)
- subcategory (nivel 2 de categorización)
- quantity (1-10 unidades)
- unit_price (rango realista por categoría)
- total_amount (quantity * unit_price)
- discount_applied (0-30%)
- payment_method (Credit Card, PayPal, Apple Pay, Google Pay, Bank Transfer)
- shipping_cost (basado en country + weight)
- delivery_time (5-30 días según country)
- customer_segment (VIP, Regular, New, Churned)
- device_type (Desktop, Mobile, Tablet)
- traffic_source (Organic, Paid, Social, Email, Direct)
- currency (USD, EUR, GBP, etc.)
- exchange_rate (conversión a USD)

CLIENTES (50,000 filas):
- customer_id
- registration_date
- country
- age (18-80)
- gender
- lifetime_value (LTV calculado)
- total_orders
- avg_order_value
- last_purchase_date
- recency_score (días desde última compra)
- frequency_score (número de compras/año)
- monetary_score (gasto total)
- rfm_segment (RFM analysis)
- churn_probability (0-1)
- preferred_category

PRODUCTOS (500 filas):
- product_id
- product_name
- category
- subcategory
- brand
- base_price
- cost_price
- margin_percentage
- stock_quantity
- supplier_country
- weight (kg)
- rating (1-5 estrellas)
- reviews_count
- launch_date

=== DASHBOARD PRINCIPAL ===

HEADER:
- Logo empresa + título "Global Ecommerce Analytics Platform"
- Selector de periodo (Today, Last 7 Days, Last 30 Days, Last 90 Days, Last Year, Custom)
- Selector multi-país (checkboxes con flags)
- Botón "Refresh Data" + último timestamp actualización
- Botón "Export Report" (PDF + Excel)

SIDEBAR AVANZADO:
Filtros dinámicos:
- 🌍 País/Región/Ciudad (multi-select con búsqueda)
- 📦 Categoría/Subcategoría de producto
- 👥 Segmento de cliente (VIP, Regular, New, At-Risk)
- 💳 Método de pago
- 📱 Tipo de dispositivo
- 🎯 Fuente de tráfico
- 💰 Rango de precio (slider)
- 📊 Métrica principal (Revenue, Orders, Units, Profit)
- 🤖 Mostrar/ocultar predicciones ML

=== KPIs PRINCIPALES (8 cards superiores) ===
Con iconos, colores por métrica, sparklines, y comparación vs periodo anterior:

1. Total Revenue: $XXX.XM (↑+15.3% vs last period)
2. Total Orders: XX,XXX (↑+8.2%)
3. Avg Order Value (AOV): $XXX (↓-2.1%)
4. Gross Profit: $XX.XM (Margin: XX%)
5. Total Customers: XX,XXX (New: X,XXX)
6. Conversion Rate: X.XX% (↑+0.5pp)
7. Customer Lifetime Value (LTV): $X,XXX
8. Churn Rate: X.X% (↓-1.2pp)

=== SECCIÓN 1: ANÁLISIS GEOESPACIAL ===

ROW 1:
[Columna 1 - 70%] Mapa mundial interactivo (Leaflet/D3.js):
- Choropleth map coloreado por revenue/país
- Hover tooltip: País, Revenue, Orders, AOV, Top Product
- Click en país → drill-down a regiones/ciudades
- Tamaño de círculos = volumen de ventas
- Color intensity = growth rate
- Líneas entre países = flujos de productos (trading routes)

[Columna 2 - 30%] Top 15 Countries:
- Tabla ranking con flags de países
- Columnas: Country, Revenue, Orders, AOV, Growth%, Market Share%
- Barras horizontales inline para visualización rápida
- Ordenar por cualquier columna

ROW 2:
[Columna 1] Revenue by Region (Treemap):
- Jerarquía: Continent → Country → Region → City
- Drill-down interactivo
- Color por growth rate (verde = crecimiento, rojo = decline)

[Columna 2] Sales Concentration (Pie/Donut):
- Top 10 países + "Others"
- % revenue contribution
- Click para filtrar dashboard

=== SECCIÓN 2: ANÁLISIS TEMPORAL & FORECASTING ===

ROW 1:
[Full Width] Revenue & Orders Over Time:
- Dual-axis chart (columnas = revenue, línea = orders)
- Granularidad ajustable (Hour, Day, Week, Month, Quarter)
- Línea de tendencia (regresión lineal)
- Área sombreada = forecast 90 días adelante (Prophet model)
- Bandas de confianza 95% para predicción
- Anotaciones de eventos (Black Friday, Navidad, campañas)
- Estacionalidad detectada automáticamente

ROW 2:
[Columna 1] Forecasting 90 Días (Prophet):
- Gráfico de predicción con:
  * Datos históricos (azul)
  * Predicción puntual (línea roja)
  * Intervalo confianza 80% (área gris oscuro)
  * Intervalo confianza 95% (área gris claro)
- Métricas modelo: MAPE, RMSE, R²
- Componentes descompuestos:
  * Trend
  * Weekly seasonality
  * Yearly seasonality
  * Holidays effect

[Columna 2] Growth Rate Analysis:
- Gráfico cascada (Waterfall Chart):
  * Starting Revenue
  * + New Customers Revenue
  * + Upsells/Cross-sells
  * - Churn Revenue
  * - Discounts/Returns
  * = Ending Revenue
- MoM (Month over Month) growth rate timeline
- YoY (Year over Year) comparison

=== SECCIÓN 3: ANÁLISIS DE PRODUCTOS ===

ROW 1:
[Columna 1 - 60%] Product Performance Matrix:
- Scatter plot: X = Units Sold, Y = Profit Margin, Size = Revenue
- Cuadrantes:
  * Top-Right: Stars (high volume + high margin)
  * Top-Left: Question Marks (low volume + high margin)
  * Bottom-Right: Cash Cows (high volume + low margin)
  * Bottom-Left: Dogs (low volume + low margin)
- Color por categoría
- Hover: Producto, Revenue, Units, Margin%, Growth%

[Columna 2 - 40%] Top 20 Products:
- Ranking table con mini-charts inline
- Columnas: Product, Category, Revenue, Units, Margin%, Trend (sparkline)
- Badges: "🔥 Trending", "⭐ Top Seller", "📈 Fast Growing"

ROW 2:
[Columna 1] Revenue by Category (Stacked Bar):
- Bars por mes
- Stack = subcategorías
- Toggle para view absoluto vs. relativo (%)

[Columna 2] Category Performance (Radar Chart):
- Ejes: Revenue, Profit, Growth, Customer Satisfaction, Stock Turnover
- Una línea por categoría principal
- Identificar categorías balanceadas

ROW 3:
[Columna 1] Product Affinity Matrix (Heatmap):
- Market Basket Analysis
- Filas = Producto A, Columnas = Producto B
- Color intensity = frecuencia de compra conjunta
- Hover: "X% de compradores de A también compran B"
- Útil para cross-selling

[Columna 2] Product Lifecycle:
- Scatter plot: X = Days Since Launch, Y = Revenue
- Curva de ciclo de vida típica (introducción, crecimiento, madurez, declive)
- Identificar productos en fase de declive para promociones

=== SECCIÓN 4: ANÁLISIS DE CLIENTES & SEGMENTACIÓN ===

ROW 1:
[Columna 1 - 50%] Customer Segmentation (Scatter):
- RFM Analysis 3D → proyección 2D
- X = Recency, Y = Frequency, Size = Monetary
- Color por segmento:
  * Champions (dark green)
  * Loyal Customers (green)
  * Potential Loyalists (light green)
  * Recent Customers (blue)
  * Promising (cyan)
  * Customers Needing Attention (yellow)
  * About to Sleep (orange)
  * At Risk (red)
  * Can't Lose Them (dark red)
  * Hibernating (grey)
  * Lost (black)
- Cluster statistics table below

[Columna 2 - 50%] Customer Lifetime Value Distribution:
- Histograma con curva de densidad
- Percentiles marcados (P25, P50, P75, P90, P95)
- Valor medio vs mediana
- Top 20% customers = XX% revenue (Pareto principle)

ROW 2:
[Columna 1] Cohort Analysis (Heatmap):
- Filas = Cohorte de registro (mes/año)
- Columnas = Meses desde registro (0-24)
- Valores = Retention rate %
- Color: Verde (alta retención) → Rojo (baja retención)
- Identificar cohortes más valiosas

[Columna 2] Churn Prediction (Gauge + Table):
- Gauge: Current Churn Rate con threshold normal
- Table: Top 100 clientes en riesgo de churn
  * Columnas: Customer ID, Country, LTV, Last Purchase, Churn Probability, Recommended Action
  * Ordenar por churn probability DESC
- Botón "Export At-Risk Customers" para email campaigns

ROW 3:
[Full Width] Customer Journey Funnel:
- Sankey Diagram:
  * Traffic Source → Landing Page → Product View → Add to Cart → Checkout → Purchase → Repeat Purchase
  * Ancho de flujo = número de usuarios
  * Drop-offs visibles en cada etapa
- Conversion rates entre etapas
- Benchmark vs industria

=== SECCIÓN 5: ANÁLISIS DE CANAL & MARKETING ===

ROW 1:
[Columna 1] Attribution Model (Sunburst Chart):
- Centro = Total Revenue
- 1er anillo = Traffic Source (Organic, Paid, Social, Email, Direct)
- 2do anillo = Device Type
- 3er anillo = Country
- Drill-down interactivo

[Columna 2] Channel Performance (Grouped Bar):
- X axis = Canal
- Bars: Revenue, Orders, AOV, Conversion Rate
- Color por métrica

ROW 2:
[Columna 1] Device Type Breakdown (Donut + Stats):
- Donut: Desktop, Mobile, Tablet
- Stats cards: Revenue, Orders, AOV, Conversion Rate por device
- Trend over time (mobile increasing?)

[Columna 2] Payment Methods (Horizontal Bar):
- Bars ordenadas por revenue
- Inline sparklines = trend últimos 6 meses
- Success rate % por método

=== SECCIÓN 6: MACHINE LEARNING INSIGHTS ===

ROW 1:
[Columna 1 - 50%] Customer Clustering (K-Means):
- Scatter plot: PCA reduction de features a 2D
- Color por cluster (4-6 clusters óptimos)
- Cluster characteristics table:
  * Cluster ID, Size, Avg Revenue, Avg Orders, Avg AOV, Top Category, Dominant Country
- Recommendations por cluster

[Columna 2 - 50%] Anomaly Detection:
- Time series con puntos anómalos marcados
- Algorithm: Isolation Forest o Z-score
- Alerts table: Date, Metric, Expected Value, Actual Value, Deviation %, Possible Cause
- Color code: 🔴 Critical, 🟡 Warning, 🟢 Normal

ROW 2:
[Full Width] Product Recommendation Engine:
- Input: Selecciona un producto
- Output: Top 10 productos recomendados con scores
- Algorithm: Collaborative Filtering (ALS) + Content-Based
- Metrics: Precision@10, Recall@10, NDCG
- Use case: "Customers who bought X also bought Y"

ROW 3:
[Columna 1] Demand Forecasting por Producto:
- Table con top 50 productos
- Columnas: Product, Current Stock, Forecasted Demand (30/60/90 days), Stock-out Risk, Recommended Reorder
- Color code: 🔴 Critical (stock-out risk), 🟡 Low stock, 🟢 Sufficient

[Columna 2] Price Elasticity Analysis:
- Scatter plot: X = % Price Change, Y = % Demand Change
- Regression line para calcular elasticidad
- Identify: Elastic products (demand sensible a precio) vs Inelastic

=== SECCIÓN 7: ANÁLISIS FINANCIERO ===

ROW 1:
[Columna 1] Profit & Loss Statement:
- Waterfall chart:
  * Revenue
  * - Cost of Goods Sold (COGS)
  * = Gross Profit
  * - Marketing Costs
  * - Shipping Costs
  * - Transaction Fees
  * - Operating Expenses
  * = Net Profit
- Margin %'s calculados
- Comparison vs budget/forecast

[Columna 2] Revenue Breakdown (Treemap):
- Hierarchy: Total Revenue → Category → Brand → Product
- Color by profit margin
- Size by revenue

ROW 2:
[Columna 1] Cash Flow Analysis:
- Stacked area chart: Inflows vs Outflows over time
- Cumulative net cash flow line
- Burn rate metric

[Columna 2] Key Financial Metrics (Cards):
- Gross Profit Margin
- Net Profit Margin
- Return on Ad Spend (ROAS)
- Customer Acquisition Cost (CAC)
- CAC Payback Period
- LTV/CAC Ratio

=== SECCIÓN 8: ANÁLISIS OPERACIONAL ===

ROW 1:
[Columna 1] Fulfillment Metrics:
- Gauge: Avg Delivery Time (días)
- Histogram: Distribution of delivery times
- Table: Delivery time by country + carrier
- % on-time deliveries

[Columna 2] Inventory Turnover:
- Bar chart: Turnover ratio por categoría
- Slow-moving products list
- Overstock alerts

ROW 2:
[Full Width] Shipping Cost Analysis:
- Map: Avg shipping cost by destination
- Scatter: Distance vs Shipping Cost (regression)
- Carrier comparison table

=== TABLA DETALLADA INTERACTIVA ===
Full-width DataTable con todas las transacciones:
- Paginación (50/100/500 rows per page)
- Sorting por cualquier columna
- Búsqueda global
- Filtros por columna (dropdowns, range sliders)
- Columnas: Date, Transaction ID, Customer ID, Country, Product, Category, Quantity, Price, Total, Payment Method, Device
- Botones: "View Customer Profile", "View Product Details"
- Export: CSV, Excel, JSON

=== FEATURES TÉCNICAS AVANZADAS ===

1. PERFORMANCE:
- Lazy loading de gráficos (carga on-scroll)
- Websockets para real-time updates
- Server-side pagination para tablas grandes
- Debouncing en filtros (espera 500ms antes de re-render)
- Caching agresivo de queries frecuentes (Redis)

2. INTERACTIVIDAD:
- Cross-filtering: Click en cualquier gráfico filtra todo el dashboard
- Drill-down: Click para explorar niveles de detalle
- Tooltips informativos en hover (todos los charts)
- Zoom & pan en time-series charts
- Brush selection para seleccionar rangos

3. RESPONSIVE DESIGN:
- Breakpoints: Desktop (>1200px), Tablet (768-1200px), Mobile (<768px)
- Grid adaptativo con CSS Grid
- Gráficos redimensionan automáticamente
- Sidebar colapsable en mobile

4. DARK MODE:
- Toggle dark/light mode (persistente en localStorage)
- Paleta de colores adaptada
- Gráficos ajustan colores automáticamente

5. EXPORTACIÓN:
- PDF report con logo, fecha, filtros aplicados
- Excel con múltiples sheets (summary, transactions, customers, products)
- Programar envío automático email (diario/semanal/mensual)

6. ALERTAS & NOTIFICACIONES:
- Alert cuando métrica cae bajo threshold
- Email/Slack notification automática
- Dashboard de alertas activas

7. VERSIONADO:
- Guardar configuraciones de dashboard
- Comparar snapshots de diferentes periodos
- Historial de cambios en datos

=== TECNOLOGÍAS A USAR ===

Backend:
- Python FastAPI (async, high performance)
- PostgreSQL + SQLAlchemy ORM
- Redis for caching
- Celery for background tasks (ML model training)

Frontend:
- HTML5 + CSS3 (CSS Grid + Flexbox)
- JavaScript ES6+
- Chart.js (2D charts)
- D3.js (custom visualizations, maps)
- Leaflet (interactive maps)
- DataTables.js (advanced tables)
- ApexCharts (financial charts)

ML Libraries (Python):
- scikit-learn (clustering, classification)
- Prophet (Facebook's forecasting)
- XGBoost (gradient boosting)
- TensorFlow (optional, deep learning)

Data Processing:
- Pandas, NumPy
- Dask (parallel computing)
- PySpark (optional, for very large datasets)

=== ESTILO & UX ===

Color Palette:
- Primary: #1E40AF (blue-800)
- Secondary: #10B981 (green-500)
- Accent: #F59E0B (amber-500)
- Danger: #EF4444 (red-500)
- Background: #0F172A (slate-900)
- Card Background: #1E293B (slate-800)
- Text: #F1F5F9 (slate-100)

Typography:
- Headings: Inter Bold
- Body: Inter Regular
- Numbers: JetBrains Mono (monospaced for tables)

Animations:
- Fade-in on load (0.3s ease-in-out)
- Smooth transitions en hover (0.2s)
- Loading spinners con skeleton screens
- Progress bars para procesos largos

Icons:
- Font Awesome or Heroicons
- Iconos consistentes en todo el dashboard

=== GENERACIÓN DE DATOS REALISTAS ===

Usa Faker + custom logic para generar:
- Nombres de productos realistas por categoría
- Distribución geográfica realista (concentración USA, Europe)
- Estacionalidad en ventas (picos en Black Friday, Navidad)
- Correlaciones entre variables (high AOV countries, price sensitivity)
- Customer behavior patterns (repeat purchase likelihood, churn)
- Realistic price ranges per category
- Product ratings & reviews distributions

=== SALIDA ESPERADA ===

Un dashboard completamente funcional con:
- Backend API RESTful (FastAPI) con endpoints documentados (Swagger)
- Frontend interactivo responsive
- Base de datos PostgreSQL con schema optimizado
- Scripts de seed data para generar 100K+ registros
- README con instrucciones de setup
- Docker Compose para deployment fácil
- Guía de usuario con screenshots

PRIORIDAD:
1. Datos realistas y bien estructurados
2. Visualizaciones informativas y profesionales
3. Performance (carga < 3 segundos)
4. UX intuitiva
5. Código limpio y documentado

Genera el proyecto completo y funcionando.
```

---

## PARTE 2: IMPLEMENTACIÓN AVANZADA EN STREAMLIT

### Estructura del Proyecto

```
ecommerce-ai-dashboard/
├── app.py                          # Aplicación principal Streamlit
├── requirements.txt                # Dependencias Python
├── config.py                       # Configuración (API keys, DB credentials)
├── .streamlit/
│   └── config.toml                # Tema Streamlit
│
├── data/
│   ├── raw/
│   │   ├── transactions.csv       # Transacciones (100K+ filas)
│   │   ├── customers.csv          # Clientes (50K filas)
│   │   └── products.csv           # Productos (500 filas)
│   ├── processed/
│   │   ├── aggregated_daily.csv   # Datos agregados por día
│   │   └── customer_features.csv  # Features para ML
│   └── geo/
│       └── countries.geojson      # Datos geográficos
│
├── models/
│   ├── forecasting/
│   │   ├── prophet_model.pkl      # Modelo Prophet entrenado
│   │   └── arima_params.json      # Parámetros ARIMA
│   ├── clustering/
│   │   ├── kmeans_customers.pkl   # Clustering de clientes
│   │   └── scaler.pkl             # Scaler para normalización
│   ├── churn/
│   │   ├── xgboost_churn.pkl      # Modelo predicción churn
│   │   └── feature_importance.csv # Importancia de features
│   └── recommendation/
│       ├── als_model.pkl          # Sistema recomendación ALS
│       └── product_similarity.pkl # Matriz similaridad productos
│
├── utils/
│   ├── data_loader.py             # Funciones cargar datos
│   ├── data_generator.py          # Generar datos sintéticos realistas
│   ├── preprocessing.py           # Limpieza y transformación
│   ├── metrics.py                 # Cálculo KPIs y métricas
│   └── ml_models.py               # Entrenamiento modelos ML
│
├── components/
│   ├── kpis.py                    # Componente KPIs principales
│   ├── geo_analysis.py            # Análisis geoespacial + mapas
│   ├── forecasting.py             # Predicciones Prophet
│   ├── product_analysis.py        # Análisis de productos
│   ├── customer_segmentation.py   # RFM + clustering
│   ├── marketing_analysis.py      # Análisis de canales
│   ├── ml_insights.py             # Insights ML (anomalías, recomendaciones)
│   └── financial_analysis.py      # P&L, cash flow
│
├── pages/
│   ├── 1_📊_Overview.py          # Dashboard principal
│   ├── 2_🌍_Geographic_Analysis.py
│   ├── 3_📈_Forecasting.py
│   ├── 4_🛍️_Product_Analytics.py
│   ├── 5_👥_Customer_Intelligence.py
│   ├── 6_🤖_ML_Insights.py
│   └── 7_💰_Financial_Reports.py
│
├── notebooks/
│   ├── 01_data_exploration.ipynb  # EDA
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
│
└── tests/
    ├── test_data_loader.py
    ├── test_metrics.py
    └── test_models.py
```

---

### Código Completo: `app.py` (Aplicación Principal)

```python
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

# Importar componentes personalizados
from utils.data_loader import load_all_data, filter_data
from utils.metrics import calculate_kpis, calculate_growth_rates
from components.kpis import render_kpis
from components.geo_analysis import render_geo_analysis
from components.forecasting import render_forecasting
from components.product_analysis import render_product_analysis
from components.customer_segmentation import render_customer_segmentation
from components.ml_insights import render_ml_insights

# ============================================
# CONFIGURACIÓN DE PÁGINA
# ============================================
st.set_page_config(
    page_title="Global Ecommerce Analytics Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado profesional
st.markdown("""
<style>
    /* Fondo oscuro profesional */
    .main {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
    }
    
    /* KPI Cards */
    .stMetric {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        border-left: 4px solid #3B82F6;
    }
    
    .stMetric:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #F1F5F9;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    
    h1 {
        font-size: 2.5rem;
        background: linear-gradient(90deg, #3B82F6 0%, #10B981 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #1E293B;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
        transform: translateY(-2px);
    }
    
    /* Tablas */
    .dataframe {
        background-color: #1E293B;
        border-radius: 8px;
    }
    
    /* Selectbox */
    .stSelectbox {
        background-color: #334155;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #334155;
        border-radius: 8px;
    }
    
    /* Divider */
    hr {
        border-color: #334155;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# CACHE DE DATOS
# ============================================
@st.cache_data(ttl=3600)  # Cache por 1 hora
def load_data():
    """Carga todos los datasets con cache"""
    return load_all_data()

@st.cache_data(ttl=1800)
def calculate_metrics(df_transactions, df_customers, df_products, date_range, countries, categories):
    """Calcula métricas con cache"""
    df_filtered = filter_data(df_transactions, date_range, countries, categories)
    kpis = calculate_kpis(df_filtered, df_customers, df_products)
    return df_filtered, kpis

# ============================================
# CARGAR DATOS
# ============================================
with st.spinner("🔄 Cargando datos del ecosistema global..."):
    try:
        df_transactions, df_customers, df_products = load_data()
        data_loaded = True
    except Exception as e:
        st.error(f"❌ Error cargando datos: {str(e)}")
        st.info("💡 Ejecuta `python utils/data_generator.py` primero para generar datos")
        data_loaded = False
        st.stop()

# ============================================
# HEADER
# ============================================
col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    st.markdown("# 🌍 Global Ecommerce Analytics Platform")
    st.markdown("**AI-Powered Business Intelligence & Predictive Analytics**")

with col2:
    # Timestamp última actualización
    st.metric(
        label="📅 Last Updated",
        value=datetime.now().strftime("%H:%M"),
        delta=datetime.now().strftime("%d %b %Y")
    )

with col3:
    # Botones de acción
    col_refresh, col_export = st.columns(2)
    with col_refresh:
        if st.button("🔄 Refresh"):
            st.cache_data.clear()
            st.rerun()
    with col_export:
        if st.button("📥 Export"):
            st.info("Feature próximamente")

st.divider()

# ============================================
# SIDEBAR - FILTROS AVANZADOS
# ============================================
st.sidebar.image("https://via.placeholder.com/200x80/1E40AF/FFFFFF?text=EcommerceAI", use_container_width=True)
st.sidebar.markdown("## 🔍 Advanced Filters")

# Filtro de periodo
st.sidebar.markdown("### 📅 Time Period")
period_options = {
    "Today": 1,
    "Last 7 Days": 7,
    "Last 30 Days": 30,
    "Last 90 Days": 90,
    "Last Year": 365,
    "All Time": len(df_transactions),
    "Custom": 0
}
selected_period = st.sidebar.selectbox(
    "Quick Select",
    options=list(period_options.keys()),
    index=3  # Default: Last 90 Days
)

if selected_period == "Custom":
    min_date = df_transactions['date'].min().date()
    max_date = df_transactions['date'].max().date()
    date_range = st.sidebar.date_input(
        "Date Range",
        value=(max_date - timedelta(days=90), max_date),
        min_value=min_date,
        max_value=max_date
    )
else:
    days_back = period_options[selected_period]
    max_date = df_transactions['date'].max()
    min_date_calc = max_date - timedelta(days=days_back)
    date_range = (min_date_calc.date(), max_date.date())

st.sidebar.markdown(f"*{date_range[0]} to {date_range[1]}*")

# Filtro de países
st.sidebar.markdown("### 🌍 Geography")
all_countries = sorted(df_transactions['country'].unique())
selected_countries = st.sidebar.multiselect(
    "Countries",
    options=all_countries,
    default=all_countries[:10],  # Top 10 por defecto
    help="Select countries to analyze"
)

# Filtro de categorías
st.sidebar.markdown("### 📦 Products")
all_categories = sorted(df_transactions['category'].unique())
selected_categories = st.sidebar.multiselect(
    "Categories",
    options=all_categories,
    default=all_categories,
    help="Select product categories"
)

# Filtro de segmento de cliente
st.sidebar.markdown("### 👥 Customer Segment")
all_segments = ['All'] + sorted(df_customers['customer_segment'].unique())
selected_segment = st.sidebar.selectbox(
    "Segment",
    options=all_segments,
    index=0
)

# Filtro de método de pago
st.sidebar.markdown("### 💳 Payment Method")
all_payment_methods = ['All'] + sorted(df_transactions['payment_method'].unique())
selected_payment = st.sidebar.selectbox(
    "Payment",
    options=all_payment_methods,
    index=0
)

# Filtro de dispositivo
st.sidebar.markdown("### 📱 Device Type")
all_devices = ['All'] + sorted(df_transactions['device_type'].unique())
selected_device = st.sidebar.selectbox(
    "Device",
    options=all_devices,
    index=0
)

# Toggle predicciones ML
st.sidebar.markdown("### 🤖 AI & ML")
show_predictions = st.sidebar.checkbox(
    "Show ML Predictions",
    value=True,
    help="Display forecasts and AI insights"
)

show_anomalies = st.sidebar.checkbox(
    "Highlight Anomalies",
    value=True,
    help="Mark unusual patterns in data"
)

st.sidebar.divider()
st.sidebar.markdown("### ℹ️ About")
st.sidebar.info("""
**Version**: 1.0.0  
**Data Points**: 100K+ transactions  
**Countries**: 30+  
**ML Models**: 5 active  
**Last Training**: 2 days ago
""")

# ============================================
# FILTRAR DATOS
# ============================================
with st.spinner("⚙️ Aplicando filtros y calculando métricas..."):
    df_filtered, kpis = calculate_metrics(
        df_transactions,
        df_customers,
        df_products,
        date_range,
        selected_countries,
        selected_categories
    )
    
    # Aplicar filtros adicionales
    if selected_segment != 'All':
        customer_ids = df_customers[df_customers['customer_segment'] == selected_segment]['customer_id']
        df_filtered = df_filtered[df_filtered['customer_id'].isin(customer_ids)]
    
    if selected_payment != 'All':
        df_filtered = df_filtered[df_filtered['payment_method'] == selected_payment]
    
    if selected_device != 'All':
        df_filtered = df_filtered[df_filtered['device_type'] == selected_device]

# ============================================
# SECCIÓN 1: KPIs PRINCIPALES
# ============================================
st.markdown("## 📊 Key Performance Indicators")

render_kpis(kpis, date_range)

st.divider()

# ============================================
# SECCIÓN 2: ANÁLISIS GEOESPACIAL
# ============================================
st.markdown("## 🌍 Geographic Analysis")

with st.expander("🗺️ Interactive World Map & Regional Insights", expanded=True):
    render_geo_analysis(df_filtered, df_customers, df_products)

st.divider()

# ============================================
# SECCIÓN 3: FORECASTING & TENDENCIAS
# ============================================
st.markdown("## 📈 Revenue Forecasting & Trends")

if show_predictions:
    with st.expander("🔮 90-Day Revenue Forecast (Prophet Model)", expanded=True):
        render_forecasting(df_filtered, forecast_days=90)
else:
    st.info("💡 Enable 'Show ML Predictions' in sidebar to view forecasts")

st.divider()

# ============================================
# SECCIÓN 4: ANÁLISIS DE PRODUCTOS
# ============================================
st.markdown("## 🛍️ Product Performance & Analytics")

with st.expander("📦 Product Matrix & Top Performers", expanded=True):
    render_product_analysis(df_filtered, df_products)

st.divider()

# ============================================
# SECCIÓN 5: SEGMENTACIÓN DE CLIENTES
# ============================================
st.markdown("## 👥 Customer Intelligence & Segmentation")

with st.expander("🎯 RFM Analysis & Customer Clustering", expanded=True):
    render_customer_segmentation(df_filtered, df_customers)

st.divider()

# ============================================
# SECCIÓN 6: ML INSIGHTS
# ============================================
if show_predictions:
    st.markdown("## 🤖 AI & Machine Learning Insights")
    
    with st.expander("🔬 Anomaly Detection & Predictive Models", expanded=True):
        render_ml_insights(df_filtered, df_customers, df_products, show_anomalies)

st.divider()

# ============================================
# TABLA DETALLADA
# ============================================
st.markdown("## 📋 Detailed Transaction Log")

# Configuración de tabla
show_table = st.checkbox("Show detailed data table", value=False)

if show_table:
    st.markdown(f"**Total transactions in view**: {len(df_filtered):,}")
    
    # Preparar datos para mostrar
    df_display = df_filtered.copy()
    df_display = df_display.sort_values('date', ascending=False)
    
    # Formatear columnas
    df_display['date'] = df_display['date'].dt.strftime('%Y-%m-%d %H:%M')
    df_display['total_amount'] = df_display['total_amount'].apply(lambda x: f"${x:,.2f}")
    
    # Seleccionar columnas a mostrar
    columns_to_show = [
        'date', 'transaction_id', 'customer_id', 'country', 
        'product_name', 'category', 'quantity', 'total_amount', 
        'payment_method', 'device_type'
    ]
    
    st.dataframe(
        df_display[columns_to_show].head(100),
        use_container_width=True,
        hide_index=True
    )
    
    # Botón exportar
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Full Dataset (CSV)",
        data=csv,
        file_name=f'ecommerce_data_{datetime.now().strftime("%Y%m%d_%H%M")}.csv',
        mime='text/csv',
    )

# ============================================
# FOOTER
# ============================================
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Global Ecommerce Analytics Platform**")
    st.markdown("*Powered by AI & Machine Learning*")

with col2:
    st.markdown(f"**Data Coverage**: {date_range[0]} to {date_range[1]}")
    st.markdown(f"**Transactions Analyzed**: {len(df_filtered):,}")

with col3:
    st.markdown(f"**Last Refresh**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown("**Status**: 🟢 All Systems Operational")
```

---

Continúa en siguiente archivo debido a límite de caracteres...
