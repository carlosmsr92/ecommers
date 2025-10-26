# Global Ecommerce Analytics Platform

## Overview
This project delivers a professional Business Intelligence dashboard for global e-commerce analytics. It processes over 760,000 transactions spanning 16 years, combining real and synthetic data to provide advanced KPIs, multidimensional analysis, and predictive insights. The platform features an interactive Streamlit dashboard, a FastAPI RESTful API with ML endpoints, and robust data management with PostgreSQL and Parquet. Its core purpose is to enable data-driven decision-making for e-commerce businesses through comprehensive analytics, forecasting, customer segmentation, and product performance evaluation. The platform is designed for scalability and production readiness, aiming to unlock significant market potential by providing deep insights into sales, customer behavior, and operational efficiency.

## Recent Changes (October 26, 2025)
**Dashboard v2.0 - Complete Implementation:**
- ✅ Implemented all 9 navigation tabs with full functionality (Resumen General, Geografía, Forecasting, Productos, Clientes, Canal, ML & IA, Finanzas, Operacional)
- ✅ Created modular architecture: utils/ui_components.py, utils/filtros.py, utils/visualizaciones_avanzadas.py
- ✅ Implemented collapsible filter system in sidebar without overlapping
- ✅ Applied corporate color palette (#667eea, #f093fb, #10B981, #F59E0B, #EF4444, #3B82F6)
- ✅ All content translated to professional Spanish
- ✅ Added cmsr92 signature in footer
- ✅ Prophet forecasting with 90-day predictions and confidence intervals
- ✅ BCG matrix for product analysis (4 quadrants)
- ✅ RFM customer segmentation with K-Means clustering
- ✅ Sankey diagram for conversion flow analysis
- ✅ Isolation Forest for anomaly detection
- ✅ Waterfall chart for financial P&L analysis
- ✅ Operational metrics with rotation analysis
- ✅ Corrected MAPE calculation for historical data only
- ✅ Added ML clustering validation for required columns
- ✅ E2E testing completed successfully on all tabs
- ✅ README v2.0 created in Spanish with complete documentation

**Dashboard v2.1 - Enterprise UX/UI Enhancements (October 26, 2025):**
- ✅ **Automatic Theme Detection:** CSS `prefers-color-scheme` media queries for automatic light/dark mode based on browser settings (no manual toggle)
- ✅ **Professional Tab Navigation:** Flex-wrap layout displaying all 9 tabs visibly without horizontal scrolling, responsive design for mobile/tablet
- ✅ **Contextual Descriptions:** Professional section descriptions at the start of all 9 tabs explaining purpose and interpretation for non-technical users
- ✅ **Executive Insights System:** Automated insight generation with 4 conditional scenarios (growth, concentration, category leader, efficiency) based on real-time data
- ✅ **KPI Explanations:** Collapsible expander with clear definitions of all 8 KPIs in accessible Spanish for business stakeholders
- ✅ **Actionable Recommendations:** 5 cross-referenced recommendations linking tabs for comprehensive analysis (Geography, Forecasting, Segmentation, ML, Financial)
- ✅ **Enhanced Churn Analysis:** Risk categorization (High >70%, Medium 40-70%, Low <40%) with specific insights and 5 tiered recommendations
- ✅ **Enhanced Clustering:** 4 visual segment cards (Premium, Active, At Risk, Inactive) with characteristics, profiles, and prioritized strategies
- ✅ **Robust Error Handling:** Zero-division protection, null-data handling with clear messaging, coherent insights in all edge cases
- ✅ **Visual Consistency:** Standardized color palette, professional labels, clear legends, formatted numbers across all visualizations
- ✅ **E2E Testing Completed:** Full Playwright validation of all 9 tabs, insights system, KPI explanations, churn/clustering enhancements, and professional UX elements

**Dashboard v2.2 - Complete Spanish Internationalization (October 26, 2025):**
- ✅ **Category Translation System:** Created utils/traducciones.py with comprehensive CATEGORIAS_ES dictionary (20+ mappings: Electronics→Electrónica, Books→Libros, Clothing→Ropa, etc.)
- ✅ **Automatic Data Translation:** Categories and subcategories automatically translated at data load time via aplicar_traducciones_df() in utils/data_loader_pg.py
- ✅ **Spanish Filters:** Sidebar filters display all categories in professional Spanish (Electrónica, Libros, Deportes, Juguetes, Belleza, etc.)
- ✅ **Professional Chart Labels:** Centralized LABELS_PROFESIONALES dictionary with 50+ mappings eliminating technical field names from all visualizations
- ✅ **Professional Hovertemplates:** All 20+ charts updated with formatted tooltips: "Categoría: Electrónica, Ingresos: $7,258,482" instead of "category=electronics, total_amount_usd=7258482"
- ✅ **Spanish Insights:** Executive insights automatically use translated categories ("Categoría Líder: Electrónica domina el portafolio con 45.2%")
- ✅ **Number Formatting:** Consistent professional formatting throughout: $1,234,567 (thousand separators), 12.3% (percentages)
- ✅ **Zero Mix Languages:** 100% Spanish interface with no English category names or technical column names visible in any chart, tooltip, or filter
- ✅ **Translation Architecture:** Single-pass translation at data load ensures consistency across all tabs, filters, and visualizations without performance impact
- ✅ **Case-Insensitive Matching:** Robust traducir_categoria() function handles capitalization variations (electronics/Electronics/ELECTRONICS → Electrónica)

**Dashboard v2.3 - Complete Geographic & Temporal Internationalization (October 26, 2025):**
- ✅ **Country Translation System:** Extended PAISES_TRADUCCION dictionary in utils/traducciones.py with 100+ country mappings (United States→Estados Unidos, United Kingdom→Reino Unido, etc.)
- ✅ **Weekday Translation System:** Added DIAS_SEMANA_ES dictionary mapping English weekdays to Spanish (Monday→Lunes, Tuesday→Martes, etc.)
- ✅ **Automatic Geographic Translation:** Countries translated at data load time via aplicar_traducciones_paises_df() ensuring all geographic visualizations display Spanish names
- ✅ **All Charts Updated:** 25+ charts now have professional Spanish hovertemplates with formatted currency ($1,234,567), percentages (12.3%), and thousands separators
- ✅ **Enhanced Chart Tooltips:** Every visualization updated with custom hovertemplate for consistent professional presentation:
  - Geographic charts: "País: Estados Unidos, Ingresos: $12,345,678"
  - Product charts: "Producto: Widget ABC, Ventas: 1,234 unidades"
  - Temporal charts: "Fecha: 2024-01, Beneficio: $567,890"
  - Customer charts: "Segmento: Campeones, Clientes: 2,345 (23.5%)"
- ✅ **Weekday Charts in Spanish:** Operational tab now displays weekdays in Spanish (Lunes, Martes, Miércoles, etc.) with proper ordering
- ✅ **Data Quality Issue Identified:** Documented 9-month gap in dataset (Jan-Sep 2023) caused by synthetic data generation failure - requires data regeneration script update
- ✅ **Translation Functions:** Centralized traducir_pais() and traducir_dia_semana() functions with case-insensitive matching and fallback to original value

## User Preferences
I prefer detailed explanations. Do not make changes to the folder Z. Do not make changes to the file Y.

## System Architecture
The system employs a multi-tiered architecture. The **Frontend** is an interactive dashboard built with Streamlit, utilizing Plotly for advanced visualizations and Folium for geospatial mapping. The **Backend** is a FastAPI RESTful API, providing data and machine learning endpoints, with PostgreSQL as the primary database and SQLAlchemy for ORM. For **Machine Learning**, Prophet is used for time-series forecasting, Scikit-learn for clustering and anomaly detection, and XGBoost for advanced predictions. ReportLab handles PDF generation, and OpenPyXL manages Excel exports.

**UI/UX Decisions:**
The dashboard focuses on clear, interactive visualizations. It presents key performance indicators (KPIs) via digestible cards, choropleth maps for geographical analysis, hierarchical treemaps for detailed breakdowns, and time-series plots with forecasting. Advanced filtering via a dynamic sidebar allows users to slice data by period, geography, product, customer segment, and more.

**Technical Implementations & Feature Specifications:**

*   **Interactive Dashboard (Streamlit):**
    *   **KPIs:** 8 main KPIs including Total Revenue, Orders, AOV, Profit, Customers, Conversion Rate, LTV, and Churn Rate with comparative metrics.
    *   **Geo-spatial Analysis:** World choropleth maps, top 15 country rankings, and hierarchical treemaps (Country → City → Category).
    *   **Forecasting & Trends:** Time-series plots with Prophet 90-day forecasting, confidence bands, and model metrics (MAPE, RMSE, R²).
    *   **Product Analysis:** BCG matrix, top 20 products, revenue/profit by category.
    *   **Customer Segmentation:** RFM analysis (11 segments), LTV distribution, cohort analysis, and churn prediction.
    *   **ML Insights:** K-Means customer clustering, Isolation Forest anomaly detection, and channel performance analysis.
    *   **Detailed Tables:** Interactive DataTable with pagination and CSV download.
*   **API RESTful (FastAPI):**
    *   **Data Endpoints:** For KPIs, transactions, customers, products, and aggregated analytics by country, category, and time-series.
    *   **Machine Learning Endpoints:** For Prophet forecasting, K-Means customer clustering, churn risk identification, product recommendations (Market Basket Analysis), product demand forecasting, and anomaly detection.
    *   **Export Endpoints:** For generating comprehensive Excel reports (8 sheets) and professional PDF reports.
*   **Database Design (Unified Parquet + PostgreSQL):**
    *   **Unified Dataset (Parquet files):** Primary data source with `transactions` (763,884 records), `customers` (47,580 records), `products` (4,161 records).
    *   **PostgreSQL:** Available for backup/development with 100K sample records.
    *   **Data Loader:** Automatically uses Parquet files for optimal performance with large datasets.
    *   Optimized indexing on `transaction_id`, `customer_id`, `product_id`, `date`, `country`, and `category` for rapid queries.
    *   **Data Composition:** 541,909 real transactions (Online Retail dataset UK, 2010-2011) + 221,975 synthetically generated transactions (gap-fill 2012-2022 + extension 2023-2025), covering 16 years across 47,580 customers and 4,161 products in 37 countries, ensuring realistic seasonal patterns and growth.
*   **Advanced Filtering System:** Dynamic sidebar filters for date ranges, geographical locations, product categories, customer segments, payment methods, device types, traffic sources, and price ranges.
*   **Report Export System:** Comprehensive Excel reports with 8 distinct sheets and professional PDF reports including key KPIs, top rankings, and category analyses.

**System Design Choices:**
The project prioritizes modularity and scalability. Streamlit provides rapid dashboard development, while FastAPI ensures a high-performance, well-documented API. PostgreSQL is chosen for its robustness and ACID compliance, with Parquet used for optimized data processing and backup. Machine learning models are integrated as API endpoints for easy consumption. Security is addressed through environment variables, CORS configuration, parameterized queries to prevent SQL injection, and input validation.

## External Dependencies
*   **Streamlit:** For interactive dashboard development.
*   **FastAPI:** For building the RESTful API.
*   **PostgreSQL:** Primary relational database.
*   **Plotly:** For advanced and interactive data visualizations.
*   **Folium:** For geo-spatial data visualization.
*   **SQLAlchemy:** ORM for database interactions.
*   **Prophet (Meta):** For time-series forecasting.
*   **Scikit-learn:** For machine learning algorithms (K-Means, Isolation Forest).
*   **XGBoost:** For advanced predictive modeling.
*   **ReportLab:** For generating professional PDF reports.
*   **OpenPyXL:** For exporting data to Excel files.
*   **Pandas & NumPy:** For data manipulation and numerical operations.