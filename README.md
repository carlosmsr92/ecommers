# 📊 Analytics Ecommerce Global - Business Intelligence Dashboard

**Desarrollado por:** CMSR92  
**Versión:** 3.1  
**Última actualización:** Octubre 26, 2025

---

## 🎯 Descripción del Proyecto

Plataforma profesional de **Business Intelligence** de nivel enterprise que combina **Big Data**, **Machine Learning** e **Inteligencia Artificial** para análisis predictivo avanzado de ecommerce global. 

Este dashboard analiza **472,211 transacciones** que abarcan **16 años** (2010-2025), con distribución global realista y datos completamente internacionalizados en español profesional.

### 🌟 Características Destacadas

- ✅ **Interfaz 100% en Español**: Todas las etiquetas, filtros, insights y traducciones
- ✅ **Datos Globales Realistas**: Estados Unidos (19.13%), Reino Unido (24%), distribución balanceada
- ✅ **472K+ Transacciones**: Datos reales UK + sintéticos con distribuciones realistas
- ✅ **9 Pestañas de Análisis**: Desde resumen ejecutivo hasta ML avanzado
- ✅ **Machine Learning Integrado**: Prophet, K-Means, Isolation Forest, XGBoost
- ✅ **Visualizaciones Profesionales**: Sin etiquetas técnicas, listas para presentación
- ✅ **API RESTful Completa**: FastAPI con documentación Swagger
- ✅ **Firma Digital**: Desarrollado por CMSR92

---

## 🏗️ Stack Tecnológico

### Frontend
- **Streamlit** - Dashboard interactivo responsive
- **Plotly** - Visualizaciones interactivas profesionales
- **Folium** - Mapas geoespaciales con ISO-3

### Backend
- **FastAPI** - API RESTful de alto rendimiento
- **PostgreSQL** - Base de datos relacional (opcional)
- **Parquet** - Almacenamiento optimizado de datos

### Machine Learning & AI
- **Prophet (Meta)** - Forecasting con estacionalidad multiplicativa
- **Scikit-learn** - Clustering RFM, detección de anomalías
- **XGBoost** - Modelos predictivos avanzados

### Exportación
- **ReportLab** - Reportes PDF profesionales
- **OpenPyXL** - Exportación Excel (8 hojas)

---

## 📊 Dataset

### Composición de Datos

**472,211 transacciones** (2010-2025):
- 53,036 transacciones reales (UK Online Retail Dataset)
- 419,175 transacciones sintéticas con distribuciones realistas

**Distribución Global Realista:**
- 🇺🇸 Estados Unidos: 19.13%
- 🇬🇧 Reino Unido: 24.00%
- 🇩🇪 Alemania: 9.81%
- 🇫🇷 Francia: 7.30%
- 🇨🇳 China: 7.13%
- 40+ países más

**Categorías Balanceadas:**
- 🏠 Hogar: 34.13%
- 📱 Electrónica: 14.25%
- 👗 Moda: 14.89%
- 🛒 Comestibles: 11.09%
- 📚 Libros: 8.72%
- 🧸 Juguetes: 7.02%

**Métricas del Cliente:**
- 4,338 clientes únicos
- Segmentación RFM (9 segmentos)
- Churn probability (media: 18.4%)
- Lifetime Value calculado

---

## 🎨 Características del Dashboard

### 1. Navegación por Pestañas (9 Secciones)

| Pestaña | Contenido |
|---------|-----------|
| 📊 **Resumen General** | 8 KPIs core, evolución temporal, insights ejecutivos |
| 🌍 **Análisis Geográfico** | Mapa mundial ISO-3, treemap País→Categoría |
| 📈 **Forecasting & Tendencias** | Prophet 90 días, análisis de tendencias |
| 📦 **Análisis de Productos** | BCG Matrix, top productos, rendimiento |
| 👥 **Segmentación de Clientes** | RFM, clustering K-Means, análisis de cohortes |
| 📱 **Optimización de Canales** | Dispositivos, tráfico, Sankey profesional |
| 🤖 **ML & IA Insights** | Anomalías, clustering 3D, recomendaciones |
| 💰 **Análisis Financiero** | P&L, waterfall, métricas financieras |
| ⚙️ **Análisis Operacional** | KPIs operativos, eficiencia |

### 2. Sistema de Filtros Dinámicos

**Filtros Colapsables en Sidebar:**
- 📅 Rango de fechas personalizado
- 🌍 Geografía (países, regiones, ciudades)
- 📦 Productos (categorías traducidas)
- 👥 Segmentos de clientes
- 💳 Canales y métodos de pago
- 📱 Tipos de dispositivo
- 💰 Rango de precios
- 🤖 Activación de predicciones ML

### 3. Visualizaciones Profesionales

**Correcciones v3.1 para Cliente/Directivos:**
- ✅ Mapa mundial con códigos ISO-3 (renderizado correcto)
- ✅ Treemap simplificado (País → Categoría, sin city)
- ✅ Gráfico evolución con eje secundario (sin pico anormal)
- ✅ Prophet con estacionalidad multiplicativa (precisión mejorada)
- ✅ Churn con distribución variada (41% muy bajo, 32% bajo)
- ✅ Etiquetas de dispositivos limpias (sin "device=")
- ✅ Sankey con colores diferenciados (sin "source"/"target")
- ✅ Firma CMSR92 visible y profesional

### 4. Machine Learning Integrado

**Modelos Implementados:**
- **Prophet Forecasting**: 90 días con intervalo confianza 80%/95%
- **K-Means Clustering**: 4 segmentos RFM (Champions, Loyal, At Risk, Lost)
- **Isolation Forest**: Detección de anomalías en transacciones
- **XGBoost**: Predicción de churn y recomendaciones
- **Market Basket**: Análisis de productos relacionados

**Métricas de Evaluación:**
- MAPE, RMSE, R² para forecasting
- Silhouette Score para clustering
- Precision/Recall para clasificación

### 5. Internacionalización Completa

**Sistema de Traducciones Automáticas:**
- Categorías: Home→Hogar, Electronics→Electrónica
- Países: EIRE→Irlanda, United Kingdom→Reino Unido
- Tráfico: Organic→Orgánico, Paid Ads→Anuncios Pagados
- Dispositivos: Mobile→Móvil, Desktop→Escritorio
- Segmentos: New→Nuevo, VIP→VIP, Regular→Regular
- Métodos de pago traducidos
- Días de semana en español

---

## 🚀 Instalación y Ejecución

### Requisitos Previos

```bash
Python 3.11+
```

### Instalación

```bash
# Clonar el repositorio
git clone <tu-repositorio>
cd analytics-ecommerce-global

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución Local

```bash
# Dashboard Streamlit
streamlit run app.py

# Acceder a: http://localhost:8501
```

### Deploy en Streamlit Cloud

1. Sube el proyecto a GitHub
2. Conecta tu repositorio en [share.streamlit.io](https://share.streamlit.io)
3. Selecciona `app.py` como archivo principal
4. ¡Listo! Tu dashboard estará en línea

---

## 📁 Estructura del Proyecto

```
analytics-ecommerce-global/
├── app.py                          # ⭐ Dashboard principal
├── requirements.txt                # Dependencias Python
├── .gitignore                      # Archivos ignorados
├── README.md                       # Esta documentación
├── replit.md                       # Memoria técnica del proyecto
│
├── api/                            # API RESTful
│   ├── __init__.py
│   ├── main.py                     # Endpoints principales
│   └── ml_endpoints.py             # Endpoints ML/IA
│
├── data/                           # Datasets optimizados (Parquet)
│   ├── transactions_unified.parquet # 472K transacciones
│   ├── customers_unified.parquet    # 4.3K clientes
│   └── products_unified.parquet     # 29K productos
│
├── database/                       # Base de datos (opcional)
│   ├── __init__.py
│   ├── schema.py                   # Modelos SQLAlchemy
│   └── migration_unified.py        # Migraciones
│
└── utils/                          # Utilidades
    ├── data_loader_pg.py           # Cargador con traducciones
    ├── traducciones.py             # Sistema i18n (ES)
    ├── ui_components.py            # Componentes UI (KPIs, firma)
    ├── filtros.py                  # Sistema de filtros
    ├── export_utils.py             # Exportación Excel/PDF
    ├── visualizaciones_avanzadas.py # Gráficos especializados
    ├── data_generator.py           # Generador sintético
    └── unified_data_integration.py # Integración de datos
```

---

## 📊 API Endpoints

### Datos Básicos
```
GET /api/kpis                      # KPIs principales
GET /api/transactions              # Transacciones
GET /api/customers                 # Clientes
GET /api/products                  # Productos
```

### Analytics Agregados
```
GET /api/aggregated/by_country     # Agregación por país
GET /api/aggregated/by_category    # Agregación por categoría
GET /api/aggregated/time_series    # Series temporales
```

### Machine Learning
```
POST /api/ml/forecast              # Forecasting Prophet
POST /api/ml/cluster_customers     # Clustering K-Means
GET  /api/ml/churn_risk           # Predicción de churn
GET  /api/ml/recommendations      # Recomendaciones
POST /api/ml/anomaly_detection    # Detección de anomalías
```

### Exportación
```
GET /api/export/excel             # Reporte Excel (8 hojas)
GET /api/export/pdf               # Reporte PDF profesional
```

**Documentación interactiva:** `http://localhost:8000/docs`

---

## 🎯 Casos de Uso

1. **Análisis Ejecutivo**: KPIs, tendencias, insights accionables
2. **Segmentación de Clientes**: RFM, clustering, predicción de churn
3. **Forecasting de Ventas**: Predicciones Prophet a 90 días
4. **Análisis Geográfico**: Rendimiento por país y región
5. **Optimización de Marketing**: Canales, dispositivos, conversión
6. **Análisis Financiero**: P&L, márgenes, ROI
7. **Detección de Anomalías**: Transacciones sospechosas
8. **Análisis de Productos**: BCG Matrix, top performers

---

## 📈 Versiones

### v3.1 - Correcciones Finales para Cliente (Oct 26, 2025)
- ✅ Mapa mundial corregido (ISO-3 codes)
- ✅ Treemap simplificado (sin city)
- ✅ Gráfico evolución optimizado (eje secundario)
- ✅ Prophet mejorado (estacionalidad multiplicativa)
- ✅ Churn variado (distribución realista)
- ✅ Etiquetas limpias (sin prefijos técnicos)
- ✅ Sankey profesional (colores + sin labels técnicos)
- ✅ Firma CMSR92 implementada

### v3.0 - Regeneración de Datos Globales (Oct 26, 2025)
- 472K transacciones con distribuciones globales realistas
- Estados Unidos como mercado principal (19.13%)
- Electrónica como categoría mayor (14.25%)
- Sistema de traducción extendido
- RFM y churn mejorados

---

## 🔒 Seguridad

- ✅ Variables de entorno para credenciales
- ✅ Consultas parametrizadas (anti SQL injection)
- ✅ Validación de inputs en API
- ✅ CORS configurado
- ✅ Gestión segura de secretos

---

## 👨‍💻 Autor

**CMSR92**  
*Data Scientist | ML Engineer | BI Specialist*

---

## 📄 Licencia

Proyecto de código abierto bajo licencia MIT.

---

## 🙏 Agradecimientos

- UCI Machine Learning Repository (Online Retail Dataset)
- Prophet by Meta (forecasting framework)
- Plotly (interactive visualizations)
- Streamlit (dashboard framework)
- Comunidad open source

---

**✨ Desarrollado por CMSR92 ✨**

*Dashboard profesional de Business Intelligence para ecommerce global*
