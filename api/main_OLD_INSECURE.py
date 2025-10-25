from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from datetime import datetime, timedelta
import pandas as pd
from database.schema import get_engine
from pydantic import BaseModel
from sqlalchemy import text
from api.ml_endpoints import router as ml_router

app = FastAPI(
    title="Global Ecommerce Analytics API",
    description="API REST para análisis de ecommerce con Machine Learning",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include ML router
app.include_router(ml_router)

# Models
class KPIResponse(BaseModel):
    total_revenue: float
    total_orders: int
    avg_order_value: float
    gross_profit: float
    total_customers: int
    conversion_rate: float
    period_start: str
    period_end: str

class TransactionResponse(BaseModel):
    transaction_id: str
    date: datetime
    customer_id: str
    country: str
    product_name: str
    category: str
    total_amount_usd: float
    payment_method: str

class CustomerResponse(BaseModel):
    customer_id: str
    country: str
    lifetime_value: float
    total_orders: int
    rfm_segment: str
    churn_probability: float

class ProductResponse(BaseModel):
    product_id: str
    product_name: str
    category: str
    base_price: float
    margin_percentage: float
    rating: float

# Helper function
def get_db_engine():
    return get_engine()

@app.get("/")
def read_root():
    return {
        "message": "Global Ecommerce Analytics API",
        "version": "1.0.0",
        "endpoints": {
            "kpis": "/api/kpis",
            "transactions": "/api/transactions",
            "customers": "/api/customers",
            "products": "/api/products",
            "countries": "/api/analytics/countries",
            "categories": "/api/analytics/categories"
        }
    }

@app.get("/api/kpis", response_model=KPIResponse)
def get_kpis(
    start_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)"),
    country: Optional[str] = Query(None, description="Filter by country"),
    category: Optional[str] = Query(None, description="Filter by category")
):
    """
    Obtiene KPIs principales del ecommerce
    """
    engine = get_db_engine()
    
    # Fechas por defecto
    if not end_date:
        end_date = datetime.now().strftime('%Y-%m-%d')
    if not start_date:
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    # Query base
    query = f"""
    SELECT 
        COUNT(*) as total_orders,
        SUM(total_amount_usd) as total_revenue,
        AVG(total_amount_usd) as avg_order_value,
        SUM(profit) as gross_profit,
        COUNT(DISTINCT customer_id) as total_customers
    FROM transactions
    WHERE date >= '{start_date}' AND date <= '{end_date}'
    """
    
    # Filtros opcionales
    if country:
        query += f" AND country = '{country}'"
    if category:
        query += f" AND category = '{category}'"
    
    try:
        result = pd.read_sql_query(query, engine)
        data = result.iloc[0]
        
        total_customers = float(data['total_customers']) if data['total_customers'] else 1
        total_orders = float(data['total_orders']) if data['total_orders'] else 0
        
        return KPIResponse(
            total_revenue=float(data['total_revenue'] or 0),
            total_orders=int(data['total_orders'] or 0),
            avg_order_value=float(data['avg_order_value'] or 0),
            gross_profit=float(data['gross_profit'] or 0),
            total_customers=int(total_customers),
            conversion_rate=round((total_orders / total_customers) * 100, 2) if total_customers > 0 else 0,
            period_start=start_date,
            period_end=end_date
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/transactions")
def get_transactions(
    limit: int = Query(100, le=1000),
    offset: int = Query(0),
    country: Optional[str] = None,
    category: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    """
    Obtiene transacciones con paginación y filtros
    """
    engine = get_db_engine()
    
    query = "SELECT * FROM transactions WHERE 1=1"
    
    if start_date:
        query += f" AND date >= '{start_date}'"
    if end_date:
        query += f" AND date <= '{end_date}'"
    if country:
        query += f" AND country = '{country}'"
    if category:
        query += f" AND category = '{category}'"
    
    query += f" ORDER BY date DESC LIMIT {limit} OFFSET {offset}"
    
    try:
        df = pd.read_sql_query(query, engine)
        return {
            "total": len(df),
            "limit": limit,
            "offset": offset,
            "data": df.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/customers")
def get_customers(
    limit: int = Query(100, le=1000),
    offset: int = Query(0),
    country: Optional[str] = None,
    rfm_segment: Optional[str] = None,
    min_ltv: Optional[float] = None
):
    """
    Obtiene clientes con filtros
    """
    engine = get_db_engine()
    
    query = "SELECT * FROM customers WHERE 1=1"
    
    if country:
        query += f" AND country = '{country}'"
    if rfm_segment:
        query += f" AND rfm_segment = '{rfm_segment}'"
    if min_ltv:
        query += f" AND lifetime_value >= {min_ltv}"
    
    query += f" ORDER BY lifetime_value DESC LIMIT {limit} OFFSET {offset}"
    
    try:
        df = pd.read_sql_query(query, engine)
        return {
            "total": len(df),
            "limit": limit,
            "offset": offset,
            "data": df.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/products")
def get_products(
    limit: int = Query(100, le=500),
    offset: int = Query(0),
    category: Optional[str] = None,
    min_rating: Optional[float] = None
):
    """
    Obtiene productos con filtros
    """
    engine = get_db_engine()
    
    query = "SELECT * FROM products WHERE 1=1"
    
    if category:
        query += f" AND category = '{category}'"
    if min_rating:
        query += f" AND rating >= {min_rating}"
    
    query += f" ORDER BY rating DESC LIMIT {limit} OFFSET {offset}"
    
    try:
        df = pd.read_sql_query(query, engine)
        return {
            "total": len(df),
            "limit": limit,
            "offset": offset,
            "data": df.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/analytics/countries")
def get_country_analytics(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    """
    Análisis de revenue por país
    """
    engine = get_db_engine()
    
    query = """
    SELECT 
        country,
        COUNT(*) as orders,
        SUM(total_amount_usd) as revenue,
        AVG(total_amount_usd) as aov,
        COUNT(DISTINCT customer_id) as customers
    FROM transactions
    """
    
    if start_date or end_date:
        query += " WHERE 1=1"
        if start_date:
            query += f" AND date >= '{start_date}'"
        if end_date:
            query += f" AND date <= '{end_date}'"
    
    query += " GROUP BY country ORDER BY revenue DESC"
    
    try:
        df = pd.read_sql_query(query, engine)
        return {
            "data": df.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/analytics/categories")
def get_category_analytics(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    """
    Análisis de revenue por categoría
    """
    engine = get_db_engine()
    
    query = """
    SELECT 
        category,
        COUNT(*) as orders,
        SUM(total_amount_usd) as revenue,
        SUM(profit) as profit,
        AVG(margin_percentage) as avg_margin
    FROM transactions t
    """
    
    if start_date or end_date:
        query += " WHERE 1=1"
        if start_date:
            query += f" AND date >= '{start_date}'"
        if end_date:
            query += f" AND date <= '{end_date}'"
    
    query += " GROUP BY category ORDER BY revenue DESC"
    
    try:
        df = pd.read_sql_query(query, engine)
        return {
            "data": df.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/analytics/time-series")
def get_time_series(
    granularity: str = Query("day", description="day, week, or month"),
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    """
    Serie temporal de revenue y orders
    """
    engine = get_db_engine()
    
    # Determinar formato de fecha según granularidad
    date_format = {
        'day': "DATE(date)",
        'week': "DATE_TRUNC('week', date)",
        'month': "DATE_TRUNC('month', date)"
    }.get(granularity, "DATE(date)")
    
    query = f"""
    SELECT 
        {date_format} as period,
        COUNT(*) as orders,
        SUM(total_amount_usd) as revenue,
        SUM(profit) as profit
    FROM transactions
    """
    
    if start_date or end_date:
        query += " WHERE 1=1"
        if start_date:
            query += f" AND date >= '{start_date}'"
        if end_date:
            query += f" AND date <= '{end_date}'"
    
    query += f" GROUP BY {date_format} ORDER BY period"
    
    try:
        df = pd.read_sql_query(query, engine)
        df['period'] = df['period'].astype(str)
        return {
            "granularity": granularity,
            "data": df.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/analytics/top-products")
def get_top_products(
    limit: int = Query(20, le=100),
    metric: str = Query("revenue", description="revenue, orders, or margin")
):
    """
    Top productos por métrica seleccionada
    """
    engine = get_db_engine()
    
    metric_map = {
        'revenue': 'SUM(total_amount_usd)',
        'orders': 'COUNT(*)',
        'margin': 'AVG(profit / total_amount_usd * 100)'
    }
    
    metric_sql = metric_map.get(metric, metric_map['revenue'])
    
    query = f"""
    SELECT 
        product_id,
        product_name,
        category,
        COUNT(*) as orders,
        SUM(total_amount_usd) as revenue,
        SUM(profit) as profit,
        SUM(quantity) as units_sold
    FROM transactions
    GROUP BY product_id, product_name, category
    ORDER BY {metric_sql} DESC
    LIMIT {limit}
    """
    
    try:
        df = pd.read_sql_query(query, engine)
        return {
            "metric": metric,
            "data": df.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/export/excel")
def export_excel(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    country: Optional[str] = None,
    category: Optional[str] = None
):
    """
    Exporta datos a Excel con análisis completo
    """
    from fastapi.responses import StreamingResponse
    from utils.export_utils import create_excel_report
    
    try:
        engine = get_db_engine()
        
        # Cargar datos
        transactions_query = "SELECT * FROM transactions WHERE 1=1"
        if start_date:
            transactions_query += f" AND date >= '{start_date}'"
        if end_date:
            transactions_query += f" AND date <= '{end_date}'"
        if country:
            transactions_query += f" AND country = '{country}'"
        if category:
            transactions_query += f" AND category = '{category}'"
        
        transactions_df = pd.read_sql_query(transactions_query, engine)
        customers_df = pd.read_sql_table('customers', engine)
        products_df = pd.read_sql_table('products', engine)
        
        # Generar Excel
        excel_buffer = create_excel_report(transactions_df, customers_df, products_df, {})
        
        return StreamingResponse(
            excel_buffer,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={
                'Content-Disposition': f'attachment; filename=ecommerce_report_{datetime.now().strftime("%Y%m%d")}.xlsx'
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generando Excel: {str(e)}")

@app.get("/api/export/pdf")
def export_pdf(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    country: Optional[str] = None,
    category: Optional[str] = None
):
    """
    Exporta reporte en PDF profesional
    """
    from fastapi.responses import StreamingResponse
    from utils.export_utils import create_pdf_report
    
    try:
        engine = get_db_engine()
        
        # Cargar datos
        transactions_query = "SELECT * FROM transactions WHERE 1=1"
        if start_date:
            transactions_query += f" AND date >= '{start_date}'"
        if end_date:
            transactions_query += f" AND date <= '{end_date}'"
        if country:
            transactions_query += f" AND country = '{country}'"
        if category:
            transactions_query += f" AND category = '{category}'"
        
        transactions_df = pd.read_sql_query(transactions_query, engine)
        customers_df = pd.read_sql_table('customers', engine)
        products_df = pd.read_sql_table('products', engine)
        
        # Generar PDF
        pdf_buffer = create_pdf_report(transactions_df, customers_df, products_df, {})
        
        return StreamingResponse(
            pdf_buffer,
            media_type='application/pdf',
            headers={
                'Content-Disposition': f'attachment; filename=ecommerce_report_{datetime.now().strftime("%Y%m%d")}.pdf'
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generando PDF: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
