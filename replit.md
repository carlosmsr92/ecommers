# Global Ecommerce Analytics Platform

## Overview
This project delivers a professional Business Intelligence dashboard for global e-commerce analytics. It processes over 770,000 transactions over 16 years, combining real and synthetic data to provide advanced KPIs, multidimensional analysis, and predictive insights. The platform features an interactive Streamlit dashboard, a FastAPI RESTful API with ML endpoints, and robust data management with PostgreSQL and Parquet. Its core purpose is to enable data-driven decision-making for e-commerce businesses through comprehensive analytics, forecasting, customer segmentation, and product performance evaluation. The platform is designed for scalability and production readiness, aiming to unlock significant market potential by providing deep insights into sales, customer behavior, and operational efficiency. The entire platform is internationalized for Spanish-speaking users, including all UI elements, data translations, and insights.

## User Preferences
I prefer detailed explanations. Do not make changes to the folder Z. Do not make changes to the file Y.

## System Architecture
The system employs a multi-tiered architecture focusing on modularity and scalability.

**UI/UX Decisions:**
The dashboard is built with Streamlit and features a professional, responsive design with automatic dark/light mode detection. It utilizes a corporate color palette and presents all content in professional Spanish, including contextual descriptions, KPI explanations, and actionable recommendations. Key elements include interactive visualizations with Plotly, professional tab navigation, and executive insights generation based on real-time data.

**Technical Implementations & Feature Specifications:**

*   **Interactive Dashboard (Streamlit):** Features 9 functional navigation tabs for comprehensive analysis: General Summary, Geography, Performance & Temporal Analysis, Products, Customers, Channel, ML & AI, Finance, and Operations. Includes 8 core KPIs, geo-spatial analysis with Folium, statistical performance analysis with moving averages and growth indicators, BCG matrix for product analysis, RFM customer segmentation with K-Means clustering, Sankey diagrams, Isolation Forest for anomaly detection, and waterfall charts for financial P&L. All data, filters, labels, and insights are fully translated into Spanish.
*   **API RESTful (FastAPI):** Provides data and machine learning endpoints for KPIs, transactions, customers, products, aggregated analytics, forecasting, clustering, churn prediction, product recommendations, and anomaly detection. Includes endpoints for generating comprehensive Excel and PDF reports.
*   **Database Design (Unified Parquet + PostgreSQL):** Primary data source is optimized Parquet files (774,434 transactions from 2010-2025), supplemented by PostgreSQL for development and backup. Data includes 541,909 real and 232,525 synthetically generated transactions, ensuring continuous time series and realistic distributions. Optimized indexing supports rapid query performance.
*   **Internationalization System:** Comprehensive translation architecture ensures a 100% Spanish interface across all UI elements, data, charts, tooltips, and insights, applied automatically at data load time.
*   **Advanced Filtering System:** Dynamic, collapsible sidebar filters allow data segmentation by date, geography, product, customer segment, payment method, device type, traffic source, and price range, all with Spanish placeholders.

**System Design Choices:**
The project emphasizes modularity and scalability using Streamlit for rapid dashboard development and FastAPI for a high-performance, well-documented API. PostgreSQL provides robustness, with Parquet files optimizing large dataset processing. Machine learning models are integrated as API endpoints for easy consumption. Security is managed through environment variables, CORS configuration, parameterized queries, and input validation.

## Recent Changes

**Dashboard v4.0 - Prophet Removal & Performance Analytics (October 26, 2025):**

- ✅ **Prophet Forecasting Replaced with Statistical Performance Analysis:**
  - **DECISION:** Eliminated Prophet (Meta's forecasting library) due to persistent Timestamp errors across granularities
  - **ROOT CAUSE:** Prophet incompatible with Pandas' deprecated Timestamp arithmetic, causing "Addition/subtraction of integers with Timestamp not supported" errors
  - **SOLUTION:** Replaced with robust statistical analysis approach using standard pandas/numpy operations
  
- ✅ **New "Rendimiento & Análisis Temporal" Tab:**
  - **Renamed from:** "Forecasting & Tendencias" → "Rendimiento & Análisis Temporal"
  - **Updated description:** Removed all references to prediction/forecasting, focused on historical performance analysis
  - **Maintained visualizations:** Evolution chart, weekday distribution, hourly distribution (all working perfectly)
  
- ✅ **New Performance Analysis Features:**
  - **Growth Indicators:** Period-over-period comparison, daily growth rate, momentum detection (accelerated/decelerated/stable)
  - **Moving Average Analysis:** Configurable windows (7/30 days, 4/12 weeks, 3/6 months) with trend detection
  - **Automatic Insights:** Smart trend analysis comparing short-term vs long-term averages
  - **Professional KPIs:** Revenue variation, order growth, daily growth rate, momentum status
  
- ✅ **Technical Quality:**
  - Zero dependency on Prophet - eliminates entire class of Timestamp errors
  - Faster execution - no ML training required
  - More robust - pure pandas/numpy operations
  - Equally valuable - executive-focused growth metrics
  
- ✅ **ML Capabilities Retained:**
  - Isolation Forest (anomaly detection) - functional ✅
  - K-Means clustering (customer segmentation) - functional ✅
  - Correlation analysis - functional ✅
  - Product recommendations - functional ✅
  - Dashboard still ML-powered with 4 robust models

- ✅ **Production Status:**
  - Dashboard 100% stable without Prophet
  - All 9 tabs functional
  - Zero Timestamp errors
  - Client-ready for international delivery

**Dashboard v4.0 - UX Refinement & Production Polish (October 26, 2025):**

- ✅ **Automatic Alerts Completely Removed:**
  - **REASON:** High data volatility across 16 years of historical data makes automatic threshold-based alerts unreliable
  - **REMOVED:** "⚠️ **Alerta de Desaceleración:**" replaced with neutral "📊 **Análisis de Variación:**"
  - **UPDATED:** "⚠️ Clientes En Riesgo" changed to "🔍 Clientes En Riesgo" (RFM segment title)
  - **RESULT:** Clean, professional dashboard without automatic warning banners

- ✅ **Custom Date Selector Implemented:**
  - **NEW FEATURE:** "Personalizado" option with interactive calendar pickers (st.date_input)
  - **DATE RANGE:** Min: 29/10/2015, Max: 26/10/2025 (full historical data range)
  - **VALIDATION:** Prevents None-type errors with graceful fallback to defaults
  - **UX:** Side-by-side date inputs (Desde/Hasta) with clear labels and help text

- ✅ **Robust Date Handling:**
  - **FIX:** Added None checks before datetime.combine() to prevent TypeError exceptions
  - **VALIDATION:** Fecha inicio must be < fecha fin with user-friendly error messages
  - **FALLBACK:** Automatic default dates if user interaction is incomplete
  - **STABILITY:** Zero TypeError exceptions in server logs confirmed by e2e testing

- ✅ **Production Environment:**
  - **CLEANED:** Removed prophet dependency from requirements.txt
  - **GITIGNORE:** Updated to exclude attached_assets/, temp files, cache
  - **README:** Comprehensive v4.0 documentation with Streamlit Cloud deployment instructions
  - **AUTHOR:** Signature "CMSR92" present throughout platform

- ✅ **End-to-End Testing:**
  - **VALIDATED:** Custom date selector functionality with calendar interaction
  - **CONFIRMED:** Zero automatic alerts ("Alerta" or "⚠️") in dashboard insights
  - **TESTED:** All 9 tabs functional, filters apply correctly, no server exceptions
  - **STATUS:** 100% production-ready, client/executive-ready deliverable

## External Dependencies
*   **Streamlit:** Interactive dashboard development.
*   **FastAPI:** RESTful API.
*   **PostgreSQL:** Relational database.
*   **Plotly:** Interactive data visualizations.
*   **Folium:** Geo-spatial visualization.
*   **SQLAlchemy:** ORM for database interactions.
*   **Scikit-learn:** Machine learning algorithms (K-Means, Isolation Forest).
*   **XGBoost:** Advanced predictive modeling.
*   **ReportLab:** PDF report generation.
*   **OpenPyXL:** Excel file export.
*   **Pandas & NumPy:** Data manipulation and numerical operations.

**Note:** Prophet (Meta) was removed in v4.0 due to compatibility issues. Replaced with statistical performance analysis.