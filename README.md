# 📊 Dashboard Avanzado de Analytics Ecommerce Global

**Desarrollado por:** cmsr92  
**Versión:** 2.0  
**Fecha:** 2025

---

## 🎯 Descripción del Proyecto

Plataforma profesional de Business Intelligence que integra **Big Data**, **Machine Learning** e **Inteligencia Artificial** para análisis predictivo avanzado de ecommerce global. Este dashboard analiza **763,884 transacciones** que abarcan **16 años** (2010-2025), combinando datos reales con expansión sintética coherente para proporcionar insights accionables de negocio.

### 🌟 Características Principales

- ✅ **Business Intelligence Avanzado**: KPIs completos, análisis multidimensional y métricas financieras
- ✅ **Big Data**: Procesamiento de 763K+ transacciones con 47,580 clientes y 4,161 productos
- ✅ **Machine Learning**: Forecasting con Prophet, clustering K-Means, detección de anomalías con Isolation Forest
- ✅ **Análisis Predictivo**: Predicción de churn, recomendaciones de productos, forecast de demanda
- ✅ **Análisis Geoespacial**: Mapas interactivos mundiales con 37 países
- ✅ **API RESTful**: FastAPI con documentación Swagger completa
- ✅ **Visualizaciones Avanzadas**: Heatmaps, treemaps, Sankey, sunburst, waterfall, radar charts
- ✅ **Análisis Financiero**: P&L, cash flow, ROAS, CAC, LTV/CAC, waterfall financiero
- ✅ **Exportación**: Reportes profesionales en Excel (8 hojas) y PDF

---

## 🏗️ Arquitectura del Sistema

### Stack Tecnológico

**Frontend:**
- Streamlit - Dashboard interactivo responsive
- Plotly - Visualizaciones avanzadas e interactivas
- Folium - Mapas geoespaciales

**Backend:**
- FastAPI - API RESTful de alto rendimiento
- PostgreSQL - Base de datos relacional ACID
- SQLAlchemy - ORM robusto

**Machine Learning & IA:**
- Prophet (Meta) - Forecasting de series temporales
- Scikit-learn - Clustering, clasificación, anomalías
- XGBoost - Modelos predictivos avanzados

**Exportación & Reportes:**
- ReportLab - Generación de PDFs profesionales
- OpenPyXL - Exportación a Excel avanzada

---

## 📊 Base de Datos

###  Dataset Unificado (Real + Sintético)

**Composición de Datos:**
- **763,884 transacciones** cubriendo 16 años completos (2010-2025)
  - 541,909 transacciones reales (Online Retail dataset UK, 2010-2011)
  - 221,975 transacciones sintéticas coherentes (gap-fill 2012-2022 + extensión 2023-2025)
- **47,580 clientes** únicos con historial completo y análisis RFM
- **4,161 productos** en 8 categorías principales
- **37 países** con distribución geográfica realista

**Características:**
- Evolución temporal coherente con patrones estacionales
- Segmentación RFM calculada sobre historial de 16 años
- Probabilidad de churn basada en análisis comportamental
- Categorización completa de productos con márgenes y costos

---

## 🎨 Características del Dashboard

### 1. Navegación Profesional por Pestañas

- 🏠 **Resumen General**: KPIs principales, evolución temporal, distribuciones
- 🌍 **Análisis Geográfico**: Mapas interactivos, rankings por país/región
- 📈 **Forecasting & Tendencias**: Predicciones Prophet, análisis de tendencias
- 📦 **Análisis de Productos**: Matriz BCG, treemaps, top productos
- 👥 **Segmentación de Clientes**: RFM, cohors, clustering, LTV
- 📱 **Análisis de Canal**: Dispositivos, fuentes tráfico, métodos pago
- 🤖 **ML & IA Insights**: Clustering, anomalías, recomendaciones
- 💰 **Análisis Financiero**: P&L, waterfall, métricas financieras
- ⚙️ **Métricas Operacionales**: KPIs operativos, eficiencia

### 2. Tema Claro/Oscuro Dinámico

**Toggle Inteligente de Modo:**
- 🌙 **Modo Claro** (por defecto): Fondo blanco, texto oscuro, alta legibilidad
- ☀️ **Modo Oscuro**: Fondo oscuro, texto claro, reducción de fatiga visual
- Toggle ubicado en sidebar superior con cambio instantáneo
- Persistencia de preferencia durante la sesión
- Contraste optimizado para WCAG 2.1 AA
- Adaptación automática de gráficos y KPIs

### 3. Sistema de Filtros Optimizado

**Filtros Colapsables Organizados:**
- 📅 Periodo de Análisis (con presets y fechas personalizadas)
- 🌍 Geografía (países, regiones, ciudades con búsqueda)
- 📦 Productos (categorías, subcategorías)
- 👥 Clientes (segmentos, RFM)
- 💳 Canal y Pago (métodos, dispositivos, fuentes)
- 💰 Rango de Precios (slider interactivo)
- 🤖 Opciones ML/IA (activar/desactivar análisis avanzados)

**Mejoras UX:**
- Sin solapamiento entre filtros
- Búsqueda activa en selectores múltiples
- Labels claros y tooltips explicativos
- Agrupación lógica por categorías
- Navegación responsive con scroll horizontal en móviles
- Media queries para pantallas pequeñas (<768px)

### 4. Visualizaciones Avanzadas

**Gráficos Implementados:**
- 📊 Heatmaps de correlación
- 🌳 Treemaps jerárquicos con tooltips limpios
- ☀️ Sunburst diagrams
- 💧 Waterfall charts (cascada)
- 🔄 Sankey diagrams (flujos)
- 🎯 Radar charts multidimensionales
- 📈 Scatterplots con clustering
- 📉 Gráficos de cohortes
- 🗺️ Mapas choropleth interactivos

**Optimización de Tooltips:**
- Tooltips profesionales sin labels técnicos
- Formato monetario consistente ($XXX,XXX)
- Información contextual clara y relevante
- Compatible con temas claro y oscuro

### 5. Análisis ML e IA

**Modelos Implementados:**
- **Forecasting**: Prophet con intervalos de confianza 80% y 95%
- **Clustering K-Means**: 
  - Cálculo dinámico de métricas RFM desde transacciones filtradas
  - 4 segmentos: Premium, Activo, En Riesgo, Inactivo
  - Visualización 3D interactiva (Recencia, Frecuencia, Monetario)
  - Validación automática de datos suficientes (mín. 100 transacciones)
  - Manejo robusto de errores con mensajes en español
- **Anomalías**: Isolation Forest para detección de outliers
- **Churn Prediction**: Modelo basado en RFM y comportamiento
- **Recomendaciones**: Market Basket Analysis y similitud
- **Demand Forecasting**: Predicción de demanda por producto

**Métricas de Evaluación:**
- MAPE (Mean Absolute Percentage Error) - calculado solo en datos históricos
- RMSE (Root Mean Squared Error)
- R² (Coefficient of Determination)
- Silhouette Score (clustering)
- Precision/Recall (clasificación)

### 6. Análisis Financiero Completo

**Métricas Implementadas:**
- P&L (Profit & Loss Statement)
- Cash Flow Analysis
- ROAS (Return on Ad Spend)
- CAC (Customer Acquisition Cost)
- LTV/CAC Ratio
- Waterfall financiero de ingresos
- Análisis de márgenes por categoría/producto
- Break-even analysis

---

## 🚀 Instalación y Uso

### Requisitos Previos

```bash
Python 3.11+
PostgreSQL 13+
```

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/cmsr92/ecommerce-analytics-dashboard.git
cd ecommerce-analytics-dashboard

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de PostgreSQL
```

### Ejecución

**Dashboard:**
```bash
streamlit run app.py --server.port 5000
```
Acceder a: http://localhost:5000

**API:**
```bash
python -m uvicorn api.main:app --host 0.0.0.0 --port 8000
```
Documentación: http://localhost:8000/docs

---

## 📁 Estructura del Proyecto

```
ecommerce-analytics-dashboard/
├── app.py                           # Dashboard Streamlit principal
├── api/
│   ├── main.py                      # API FastAPI principal
│   └── ml_endpoints.py              # Endpoints ML/IA
├── database/
│   ├── schema.py                    # Modelos SQLAlchemy
│   ├── migration.py                 # Migración datos sintéticos
│   └── migration_unified.py         # Migración datos unificados
├── utils/
│   ├── data_generator.py            # Generación datos sintéticos
│   ├── data_loader.py               # Carga desde Parquet
│   ├── data_loader_pg.py            # Carga desde PostgreSQL
│   ├── unified_data_integration.py  # Integración datos reales
│   ├── visualizaciones_avanzadas.py # Utilidades visualización
│   └── export_utils.py              # Exportación reportes
├── data/
│   ├── transactions_unified.parquet # 763K transacciones
│   ├── customers_unified.parquet    # 47K clientes
│   └── products_unified.parquet     # 4K productos
├── README.md                        # Este archivo
└── requirements.txt                 # Dependencias Python
```

---

## 📊 API Endpoints

### Endpoints de Datos

```
GET /api/kpis
GET /api/transactions
GET /api/customers
GET /api/products
GET /api/aggregated/by_country
GET /api/aggregated/by_category
GET /api/aggregated/time_series
```

### Endpoints ML/IA

```
POST /api/ml/forecast              # Forecasting Prophet
POST /api/ml/cluster_customers     # Clustering K-Means
GET  /api/ml/churn_risk           # Predicción churn
GET  /api/ml/recommendations      # Recomendaciones productos
POST /api/ml/product_demand       # Forecast demanda
POST /api/ml/anomaly_detection    # Detección anomalías
```

### Endpoints de Exportación

```
GET /api/export/excel             # Reporte Excel completo
GET /api/export/pdf               # Reporte PDF profesional
```

---

## 🎯 Casos de Uso

1. **Análisis de Ventas**: Identificar tendencias, estacionalidad y patrones de compra
2. **Segmentación de Clientes**: Clasificar clientes por valor, comportamiento y riesgo
3. **Optimización de Inventario**: Predecir demanda y optimizar stock
4. **Marketing Inteligente**: Identificar mejores canales y segmentos para campañas
5. **Análisis Financiero**: Evaluar rentabilidad, márgenes y ROI
6. **Detección de Fraude**: Identificar transacciones anómalas
7. **Forecasting de Ventas**: Planificar recursos y presupuestos
8. **Análisis de Competencia**: Comparar rendimiento por región/categoría

---

## 🔒 Seguridad

- ✅ Variables de entorno para credenciales
- ✅ Consultas parametrizadas (prevención SQL injection)
- ✅ Validación de inputs en API
- ✅ CORS configurado apropiadamente
- ✅ Gestión segura de secretos

---

## 📈 Roadmap Futuro

- [ ] Integración con Google Analytics
- [ ] Dashboard mobile-first
- [ ] Alertas automatizadas por email
- [ ] A/B Testing framework
- [ ] Integración con CRM (Salesforce, HubSpot)
- [ ] Deploy en cloud (AWS/Azure/GCP)
- [ ] Multi-tenancy para SaaS
- [ ] Real-time streaming analytics

---

## 👨‍💻 Autor

**cmsr92**  
Data Scientist | ML Engineer | Business Intelligence Specialist

[GitHub](https://github.com/cmsr92) | [LinkedIn](https://linkedin.com/in/cmsr92) | [Portfolio](https://cmsr92.dev)

---

## 📄 Licencia

Este proyecto es de código abierto bajo licencia MIT. Ver archivo LICENSE para más detalles.

---

## 🙏 Agradecimientos

- Online Retail Dataset (UCI Machine Learning Repository)
- Prophet by Meta (forecasting)
- Plotly (visualizaciones interactivas)
- Streamlit (framework dashboard)
- Comunidad open source

---

**© 2025 cmsr92 - Dashboard Avanzado de Analytics Ecommerce Global**
