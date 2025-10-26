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