# 📊 Analytics Ecommerce Global - Dashboard v4.0

**Dashboard profesional de Business Intelligence con Machine Learning y Análisis Estadístico para E-commerce Global**

> Autor: **CMSR92**  
> Versión: **4.0** (Octubre 2025)  
> Plataforma: Streamlit + FastAPI + PostgreSQL

---

## 🎯 Descripción

Plataforma avanzada de Business Intelligence que analiza más de **774,000 transacciones** (2015-2025) con capacidades de:

- **9 Tabs de Análisis** interactivos y profesionales
- **4 Modelos de Machine Learning** (Isolation Forest, K-Means, Correlación, Recomendaciones)
- **Análisis Estadístico Robusto** con promedios móviles e indicadores de crecimiento
- **100% Internacionalizado** en español profesional
- **Filtros Avanzados** multi-dimensionales con selector personalizado de fechas

---

## 🚀 Deployment en Streamlit Cloud

### Paso 1: Preparar Repositorio Git

```bash
# Clonar o crear repositorio
git clone https://github.com/tu-usuario/analytics-ecommerce.git
cd analytics-ecommerce

# Agregar archivos
git add .
git commit -m "Dashboard v4.0 - Production Ready"
git push origin main
```

### Paso 2: Configurar en Streamlit Cloud

1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Conecta tu cuenta de GitHub
3. Click en "New app"
4. Selecciona:
   - **Repository:** `tu-usuario/analytics-ecommerce`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click en "Deploy"

### Paso 3: Configuración Avanzada (Opcional)

En "Advanced settings":
- **Python version:** 3.11
- **Requirements file:** `requirements.txt`

---

## 💻 Instalación Local

### Requisitos

- Python 3.11+
- PostgreSQL (opcional, usa Parquet por defecto)

### Instalación

```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/analytics-ecommerce.git
cd analytics-ecommerce

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar Dashboard
streamlit run app.py --server.port 5000

# 5. Ejecutar API (opcional, en otra terminal)
python -m uvicorn api.main:app --host 0.0.0.0 --port 8000
```

### Acceso

- **Dashboard:** http://localhost:5000
- **API Docs:** http://localhost:8000/docs

---

## 📦 Estructura del Proyecto

```
analytics-ecommerce/
├── app.py                          # Dashboard principal (Streamlit)
├── requirements.txt                # Dependencias Python
├── replit.md                       # Documentación técnica
│
├── api/
│   └── main.py                     # API RESTful (FastAPI)
│
├── data/                           # Datos (Parquet optimizado)
│   ├── transactions_unified.parquet
│   ├── customers_unified.parquet
│   └── products_unified.parquet
│
├── utils/                          # Módulos auxiliares
│   ├── data_loader_pg.py          # Carga de datos
│   ├── filtros.py                 # Sistema de filtros
│   ├── traducciones.py            # Internacionalización
│   └── ui_components.py           # Componentes UI
│
└── .streamlit/
    └── config.toml                # Configuración Streamlit
```

---

## 🎨 Features Principales

### 1. **Tabs de Análisis**

| Tab | Descripción |
|-----|-------------|
| 🏠 **Resumen General** | KPIs principales, insights ejecutivos, evolución temporal |
| 🌍 **Análisis Geográfico** | Mapas interactivos, distribución por país/región |
| 📈 **Rendimiento & Análisis Temporal** | Indicadores de crecimiento, promedios móviles, momentum |
| 📦 **Análisis de Productos** | BCG Matrix, categorías top, subcategorías |
| 👥 **Segmentación de Clientes** | RFM, K-Means clustering, análisis de cohortes |
| 📱 **Análisis de Canal** | Diagramas Sankey, conversión por dispositivo |
| 🤖 **ML & IA Insights** | Isolation Forest, anomalías, correlaciones |
| 💰 **Análisis Financiero** | P&L waterfall, márgenes, rentabilidad |
| ⚙️ **Métricas Operacionales** | Logística, cumplimiento, satisfacción |

### 2. **Machine Learning**

- **Isolation Forest:** Detección de anomalías en transacciones
- **K-Means:** Segmentación automática de clientes (RFM)
- **Análisis de Correlación:** Identificación de patrones ocultos
- **Sistema de Recomendaciones:** Productos relacionados

### 3. **Filtros Avanzados**

- **Selector Personalizado de Fechas** (29/10/2015 - 26/10/2025)
- Presets: 7 días, 30 días, 90 días, 1 año, histórico completo
- Filtros multidimensionales:
  - Geografía (países, regiones)
  - Productos (categorías, subcategorías)
  - Clientes (segmentos)
  - Canal (método pago, dispositivo, tráfico)
  - Rango de precios

---

## 🔧 Configuración

### Variables de Entorno (Opcional)

```bash
# PostgreSQL (si no usas Parquet)
DATABASE_URL=postgresql://user:password@host:port/database

# API
SESSION_SECRET=tu_secret_key_aqui
```

### Configuración de Streamlit

Archivo `.streamlit/config.toml`:

```toml
[server]
port = 5000
enableCORS = false
enableXsrfProtection = true

[theme]
base = "dark"
primaryColor = "#667eea"
```

---

## 📊 Datos

### Fuentes de Datos

- **Transactions:** 774,434 registros (541,909 reales + 232,525 sintéticos)
- **Customers:** 100,000 clientes únicos
- **Products:** 1,000 productos en 15 categorías

### Formato

- **Primario:** Parquet (optimizado para performance)
- **Backup:** PostgreSQL (opcional)

---

## 🛠️ Tecnologías

### Core
- **Streamlit** 1.31.0 - Dashboard interactivo
- **FastAPI** 0.109.0 - API RESTful
- **Pandas** 2.1.4 - Procesamiento de datos
- **NumPy** 1.26.3 - Operaciones numéricas

### Visualización
- **Plotly** 5.18.0 - Gráficos interactivos
- **Folium** 0.15.1 - Mapas geoespaciales
- **Matplotlib** 3.8.2 - Gráficos estáticos
- **Seaborn** 0.13.1 - Visualizaciones estadísticas

### Machine Learning
- **Scikit-learn** 1.3.2 - Modelos ML
- **XGBoost** 2.0.3 - Modelos avanzados

### Base de Datos
- **SQLAlchemy** 2.0.25 - ORM
- **psycopg2-binary** 2.9.9 - PostgreSQL driver

---

## 📝 Changelog

### v4.0 (Octubre 2025)
- ✅ Eliminado Prophet (Meta) por problemas de compatibilidad
- ✅ Nuevo sistema de análisis estadístico robusto
- ✅ Selector personalizado de fechas con calendarios
- ✅ Eliminadas alertas automáticas de desaceleración
- ✅ Mejoras de UX y performance
- ✅ Optimizado para Streamlit Cloud

### v3.1 (Anterior)
- Prophet forecasting (deprecado)
- 9 tabs de análisis
- ML capabilities básicas

---

## 🤝 Contribuciones

Este es un proyecto personal de **CMSR92**. Si encuentras bugs o tienes sugerencias, abre un issue.

---

## 📄 Licencia

Proyecto educativo y demostrativo. Uso permitido con atribución al autor.

---

## 👤 Autor

**CMSR92**  
Dashboard Avanzado de Analytics Ecommerce Global  
Version 4.0 - Octubre 2025

---

## 🔗 Links Útiles

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [FastAPI Documentation](https://fastapi.tiangolo.com)

---

**¿Preguntas?** Abre un issue en el repositorio.

**Desarrollado con ❤️ para la comunidad de Data Science y Business Intelligence**
