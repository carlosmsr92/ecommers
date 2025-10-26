# Global Ecommerce Analytics Platform

## Overview
This project delivers a professional Business Intelligence dashboard for global e-commerce analytics. It processes over 770,000 transactions spanning 16 years, combining real and synthetic data to provide advanced KPIs, multidimensional analysis, and predictive insights. The platform features an interactive Streamlit dashboard, a FastAPI RESTful API with ML endpoints, and robust data management with PostgreSQL and Parquet. Its core purpose is to enable data-driven decision-making for e-commerce businesses through comprehensive analytics, forecasting, customer segmentation, and product performance evaluation. The platform is designed for scalability and production readiness, aiming to unlock significant market potential by providing deep insights into sales, customer behavior, and operational efficiency. The entire platform is internationalized for Spanish-speaking users, including all UI elements, data translations, and insights.

## User Preferences
I prefer detailed explanations. Do not make changes to the folder Z. Do not make changes to the file Y.

## System Architecture
The system employs a multi-tiered architecture focusing on modularity and scalability.

**UI/UX Decisions:**
The dashboard is built with Streamlit and features a professional, responsive design with automatic dark/light mode detection. It utilizes a corporate color palette and presents all content in professional Spanish, including contextual descriptions, KPI explanations, and actionable recommendations. Key elements include interactive visualizations with Plotly, professional tab navigation, and executive insights generation based on real-time data. Visual consistency is maintained through standardized formatting and clear labels.

**Technical Implementations & Feature Specifications:**

*   **Interactive Dashboard (Streamlit):** Features 9 functional navigation tabs for comprehensive analysis: General Summary, Geography, Forecasting, Products, Customers, Channel, ML & AI, Finance, and Operations. Includes 8 core KPIs, geo-spatial analysis with Folium, Prophet-based 90-day forecasting, BCG matrix for product analysis, RFM customer segmentation with K-Means clustering, Sankey diagrams, Isolation Forest for anomaly detection, and waterfall charts for financial P&L. All data, filters, labels, and insights are fully translated into Spanish.
*   **API RESTful (FastAPI):** Provides data and machine learning endpoints for KPIs, transactions, customers, products, aggregated analytics, forecasting, clustering, churn prediction, product recommendations, and anomaly detection. Includes endpoints for generating comprehensive Excel (8 sheets) and PDF reports.
*   **Database Design (Unified Parquet + PostgreSQL):** Primary data source is optimized Parquet files (774,434 transactions from 2010-2025), supplemented by PostgreSQL for development and backup. Data includes 541,909 real and 232,525 synthetically generated transactions, ensuring continuous time series and realistic distributions. Optimized indexing supports rapid query performance.
*   **Internationalization System:** Comprehensive translation architecture (categories, countries, weekdays, RFM segments, devices, payment methods) ensures a 100% Spanish interface across all UI elements, data, charts, tooltips, and insights, applied automatically at data load time.
*   **Advanced Filtering System:** Dynamic, collapsible sidebar filters allow data segmentation by date, geography, product, customer segment, payment method, device type, traffic source, and price range, all with Spanish placeholders.

**System Design Choices:**
The project emphasizes modularity and scalability using Streamlit for rapid dashboard development and FastAPI for a high-performance, well-documented API. PostgreSQL provides robustness, with Parquet files optimizing large dataset processing. Machine learning models are integrated as API endpoints for easy consumption. Security is managed through environment variables, CORS configuration, parameterized queries, and input validation.

## External Dependencies
*   **Streamlit:** Interactive dashboard development.
*   **FastAPI:** RESTful API.
*   **PostgreSQL:** Relational database.
*   **Plotly:** Interactive data visualizations.
*   **Folium:** Geo-spatial visualization.
*   **SQLAlchemy:** ORM for database interactions.
*   **Prophet (Meta):** Time-series forecasting.
*   **Scikit-learn:** Machine learning algorithms (K-Means, Isolation Forest).
*   **XGBoost:** Advanced predictive modeling.
*   **ReportLab:** PDF report generation.
*   **OpenPyXL:** Excel file export.
*   **Pandas & NumPy:** Data manipulation and numerical operations.

## Version History

**Dashboard v3.0 - Data Regeneration & Global Realistic Distributions (October 26, 2025):**
- ✅ **Complete Data Regeneration with Realistic Global Distributions:**
  - Applied stratified sampling to real UK data (reduced from 354k to 53k transactions for balance)
  - Generated 375,500 new synthetic transactions with globally realistic distributions
  - **Final dataset: 472,211 transactions** (down from 773,384 to achieve better quality over quantity)
  - **Country Distribution (Realistic Global E-commerce):**
    - United States: 19.13% (previously 0% - now appears as major market!) ✅
    - United Kingdom: 24.00% (previously 89% - now balanced) ✅
    - Germany: 9.81%, France: 7.30%, China: 7.13%
    - Top 10 countries now represent diverse global markets
  - **Category Distribution (Balanced & Varied):**
    - Home (Hogar): 34.13% (previously 73% - now balanced) ✅
    - Electronics (Electrónica): 14.25% (previously 0.89% - major increase!) ✅
    - Fashion (Moda): 14.89%
    - Groceries (Comestibles): 11.09%
    - Books (Libros): 8.72%, Toys (Juguetes): 7.02%
  - **Traffic Sources:** Evenly distributed (Direct 20%, Organic 20%, Paid Ads 20%, Social Media 13%, Email 13%, Referral 13%)
  - **Customer Segments:** Uniformly distributed (VIP 33%, New 33%, Regular 33%)

- ✅ **Extended Translation System:**
  - **Categories:** Home→Hogar, Electronics→Electrónica, Fashion→Moda, Groceries→Comestibles ✅
  - **Traffic Sources:** Direct→Directo, Organic→Orgánico, Paid Ads→Anuncios Pagados, Social Media→Redes Sociales, Email→Correo Electrónico, Referral→Referencia ✅
  - **Customer Segments:** New→Nuevo, Regular→Regular, VIP→VIP ✅
  - **Countries:** EIRE→Irlanda added to dictionary ✅
  - All translations applied automatically via utils/data_loader_pg.py at data load time

- ✅ **Enhanced Customer Dataset:**
  - 4,338 unique customers
  - Added RFM segmentation (9 segments: Champions, Loyal Customers, Recent Customers, Promising, At Risk, Hibernating, Lost, Potential Loyalists, Customers Needing Attention)
  - Calculated lifetime_value (LTV) metric (average: $9,071.32)
  - Calculated churn_probability using RFM-based model (average: 42.84%, distributed: 58% low risk, 31% medium risk, 10% high risk)
  - Complete customer profiles with recency, frequency, monetary values

- ✅ **Updated Products Dataset:**
  - 29,120 unique products
  - Linked to new transaction patterns
  - Maintains subcategories in sync with main categories

- ✅ **Technical Quality:**
  - Dashboard runs without critical errors
  - Only minor pre-existing Plotly warning (country names library update notice) - does not affect functionality
  - All data files properly formatted and optimized (Parquet format)
  - Consistent data relationships across transactions, customers, and products

- ✅ **User Request Compliance:**
  - Estados Unidos (United States) now appears as major market ✅
  - Electrónica (Electronics) is now a major category ✅
  - Hogar (Home) balanced with other categories ✅
  - Greater variety of countries across continents ✅
  - EIRE correctly translates to Irlanda ✅
  - All filters and UI elements in Spanish ✅

**Dashboard v3.1 - Final Corrections for Client/Executive Delivery (October 26, 2025):**
- ✅ **World Map Visualization Fixed:**
  - Implemented ISO-3 country code mapping for accurate rendering
  - 40+ countries mapped (United Kingdom→GBR, United States→USA, etc.)
  - Professional 'natural earth' projection
  - Filtered invalid country codes

- ✅ **Geographic Treemap Simplified:**
  - Changed from path=['country', 'city', 'category'] to path=['country', 'category']
  - Eliminated confusing 'city' level
  - Clear hierarchy: Country → Category

- ✅ **Evolution Chart Enhanced:**
  - Replaced separated subplots with dual-axis chart
  - Monthly aggregation (smoother than daily)
  - Eliminated visual spike between lines and bars
  - Transparent bars with border for professional appearance

- ✅ **Prophet Forecasting Precision Improved:**
  - Added seasonality_mode='multiplicative'
  - changepoint_prior_scale=0.05 for better change detection
  - Additional monthly seasonality (period=30.5, fourier_order=5)
  - LBFGS algorithm for faster convergence

- ✅ **Churn Data Distribution Varied:**
  - Realistic distribution: 41% very low, 32% low, 9% medium, 1% high, 0.05% very high
  - Mean: 18.4% (previously 42.8%)
  - Standard deviation: 15.5
  - Based on RFM scores with random noise for variability

- ✅ **Device Distribution Labels Cleaned:**
  - Removed technical prefixes (no more "device=Mobile")
  - Professional hover templates
  - Clean label display

- ✅ **Sankey Flow Chart Professionalized:**
  - Differentiated colors by node type (traffic sources, devices, payment methods)
  - Removed technical labels 'source'/'target' from hovers
  - Transparent links for visual clarity

- ✅ **CMSR92 Signature Added:**
  - Professional footer: "✨ Desarrollado por CMSR92 ✨"
  - Corporate color styling (#667eea)
  - Visible and elegant placement

- ✅ **Technical Quality:**
  - All hovertemplate warnings resolved
  - Dashboard running without critical errors
  - Only pre-existing Plotly country names library notice (non-blocking)
  - Prophet training successful (cmdstanpy logs clean)
  - Client/executive delivery ready