# Global Ecommerce Analytics Platform

## Overview
This project delivers a professional Business Intelligence dashboard for global e-commerce analytics. It processes over 760,000 transactions spanning 16 years, combining real and synthetic data to provide advanced KPIs, multidimensional analysis, and predictive insights. The platform features an interactive Streamlit dashboard, a FastAPI RESTful API with ML endpoints, and robust data management with PostgreSQL and Parquet. Its core purpose is to enable data-driven decision-making for e-commerce businesses through comprehensive analytics, forecasting, customer segmentation, and product performance evaluation. The platform is designed for scalability and production readiness, aiming to unlock significant market potential by providing deep insights into sales, customer behavior, and operational efficiency.

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