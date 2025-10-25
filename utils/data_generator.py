import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from faker import Faker
import random
import warnings
warnings.filterwarnings('ignore')

fake = Faker()

# Configuración de datos
COUNTRIES = {
    'USA': {'region_prob': 0.35, 'cities': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'], 'currency': 'USD', 'exchange_rate': 1.0},
    'UK': {'region_prob': 0.12, 'cities': ['London', 'Manchester', 'Birmingham', 'Liverpool', 'Leeds'], 'currency': 'GBP', 'exchange_rate': 0.79},
    'Germany': {'region_prob': 0.10, 'cities': ['Berlin', 'Munich', 'Hamburg', 'Frankfurt', 'Cologne'], 'currency': 'EUR', 'exchange_rate': 0.92},
    'France': {'region_prob': 0.08, 'cities': ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice'], 'currency': 'EUR', 'exchange_rate': 0.92},
    'Canada': {'region_prob': 0.07, 'cities': ['Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Ottawa'], 'currency': 'CAD', 'exchange_rate': 1.35},
    'Australia': {'region_prob': 0.06, 'cities': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide'], 'currency': 'AUD', 'exchange_rate': 1.52},
    'Spain': {'region_prob': 0.05, 'cities': ['Madrid', 'Barcelona', 'Valencia', 'Seville', 'Zaragoza'], 'currency': 'EUR', 'exchange_rate': 0.92},
    'Italy': {'region_prob': 0.04, 'cities': ['Rome', 'Milan', 'Naples', 'Turin', 'Florence'], 'currency': 'EUR', 'exchange_rate': 0.92},
    'Brazil': {'region_prob': 0.04, 'cities': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Fortaleza'], 'currency': 'BRL', 'exchange_rate': 5.02},
    'Mexico': {'region_prob': 0.03, 'cities': ['Mexico City', 'Guadalajara', 'Monterrey', 'Puebla', 'Tijuana'], 'currency': 'MXN', 'exchange_rate': 17.15},
    'Japan': {'region_prob': 0.02, 'cities': ['Tokyo', 'Osaka', 'Yokohama', 'Nagoya', 'Sapporo'], 'currency': 'JPY', 'exchange_rate': 149.50},
    'Netherlands': {'region_prob': 0.015, 'cities': ['Amsterdam', 'Rotterdam', 'The Hague', 'Utrecht', 'Eindhoven'], 'currency': 'EUR', 'exchange_rate': 0.92},
    'Sweden': {'region_prob': 0.01, 'cities': ['Stockholm', 'Gothenburg', 'Malmö', 'Uppsala', 'Västerås'], 'currency': 'SEK', 'exchange_rate': 10.50},
}

CATEGORIES = {
    'Electronics': {
        'subcategories': ['Smartphones', 'Laptops', 'Tablets', 'Headphones', 'Cameras'],
        'price_range': (50, 2000),
        'margin': (0.15, 0.35),
        'brands': ['Apple', 'Samsung', 'Sony', 'Dell', 'HP', 'Lenovo', 'Bose']
    },
    'Fashion': {
        'subcategories': ['Mens Clothing', 'Womens Clothing', 'Shoes', 'Accessories', 'Jewelry'],
        'price_range': (20, 500),
        'margin': (0.40, 0.65),
        'brands': ['Nike', 'Adidas', 'Zara', 'H&M', 'Gucci', 'Prada', 'Levis']
    },
    'Home': {
        'subcategories': ['Furniture', 'Kitchen', 'Decor', 'Bedding', 'Storage'],
        'price_range': (15, 800),
        'margin': (0.35, 0.55),
        'brands': ['IKEA', 'Wayfair', 'West Elm', 'Crate & Barrel', 'HomeGoods']
    },
    'Sports': {
        'subcategories': ['Fitness Equipment', 'Outdoor Gear', 'Team Sports', 'Cycling', 'Yoga'],
        'price_range': (10, 600),
        'margin': (0.30, 0.50),
        'brands': ['Under Armour', 'Reebok', 'Columbia', 'The North Face', 'Patagonia']
    },
    'Books': {
        'subcategories': ['Fiction', 'Non-Fiction', 'Educational', 'Comics', 'Magazines'],
        'price_range': (5, 60),
        'margin': (0.25, 0.45),
        'brands': ['Penguin', 'Harper Collins', 'Random House', 'Scholastic', 'Marvel']
    },
    'Beauty': {
        'subcategories': ['Skincare', 'Makeup', 'Haircare', 'Fragrance', 'Tools'],
        'price_range': (10, 200),
        'margin': (0.50, 0.70),
        'brands': ['LOreal', 'Estée Lauder', 'MAC', 'Sephora', 'Clinique']
    },
    'Toys': {
        'subcategories': ['Action Figures', 'Board Games', 'Educational', 'Outdoor Toys', 'Puzzles'],
        'price_range': (5, 150),
        'margin': (0.40, 0.60),
        'brands': ['LEGO', 'Mattel', 'Hasbro', 'Fisher-Price', 'Melissa & Doug']
    },
    'Groceries': {
        'subcategories': ['Snacks', 'Beverages', 'Organic', 'Frozen', 'Canned Goods'],
        'price_range': (2, 50),
        'margin': (0.20, 0.35),
        'brands': ['Nestle', 'Coca-Cola', 'Pepsi', 'Kraft', 'General Mills']
    }
}

PAYMENT_METHODS = ['Credit Card', 'PayPal', 'Apple Pay', 'Google Pay', 'Bank Transfer']
DEVICE_TYPES = ['Desktop', 'Mobile', 'Tablet']
TRAFFIC_SOURCES = ['Organic', 'Paid', 'Social', 'Email', 'Direct']

def generate_products(n_products=500):
    """Genera productos realistas"""
    products = []
    product_id = 1
    
    for category, details in CATEGORIES.items():
        subcategories = details['subcategories']
        brands = details['brands']
        price_min, price_max = details['price_range']
        margin_min, margin_max = details['margin']
        
        products_per_category = n_products // len(CATEGORIES)
        
        for i in range(products_per_category):
            subcategory = random.choice(subcategories)
            brand = random.choice(brands)
            
            base_price = round(random.uniform(price_min, price_max), 2)
            margin = random.uniform(margin_min, margin_max)
            cost_price = round(base_price * (1 - margin), 2)
            
            product = {
                'product_id': f'P{product_id:05d}',
                'product_name': f'{brand} {subcategory} {fake.word().capitalize()}',
                'category': category,
                'subcategory': subcategory,
                'brand': brand,
                'base_price': base_price,
                'cost_price': cost_price,
                'margin_percentage': round(margin * 100, 2),
                'stock_quantity': random.randint(50, 1000),
                'supplier_country': random.choice(list(COUNTRIES.keys())),
                'weight': round(random.uniform(0.1, 10.0), 2),
                'rating': round(random.uniform(3.5, 5.0), 1),
                'reviews_count': random.randint(10, 5000),
                'launch_date': fake.date_between(start_date='-3y', end_date='today')
            }
            products.append(product)
            product_id += 1
    
    return pd.DataFrame(products)

def generate_customers(n_customers=50000):
    """Genera clientes realistas"""
    customers = []
    
    # Distribución de países (normalizar para que sumen 1)
    country_probs = np.array([v['region_prob'] for v in COUNTRIES.values()])
    country_probs = country_probs / country_probs.sum()
    countries_list = list(COUNTRIES.keys())
    
    for i in range(n_customers):
        country = np.random.choice(countries_list, p=country_probs)
        registration_date = fake.date_between(start_date='-5y', end_date='today')
        
        # RFM scores
        recency_score = random.randint(1, 365)
        frequency_score = random.randint(1, 50)
        monetary_score = round(random.uniform(50, 5000), 2)
        
        # Calcular segmento RFM
        rfm_segment = calculate_rfm_segment(recency_score, frequency_score, monetary_score)
        
        # Churn probability (basado en recency principalmente)
        churn_prob = min(0.95, recency_score / 365.0)
        
        customer = {
            'customer_id': f'C{i+1:06d}',
            'registration_date': registration_date,
            'country': country,
            'age': random.randint(18, 80),
            'gender': random.choice(['Male', 'Female', 'Other']),
            'lifetime_value': monetary_score,
            'total_orders': frequency_score,
            'avg_order_value': round(monetary_score / max(frequency_score, 1), 2),
            'last_purchase_date': datetime.now() - timedelta(days=recency_score),
            'recency_score': recency_score,
            'frequency_score': frequency_score,
            'monetary_score': monetary_score,
            'rfm_segment': rfm_segment,
            'churn_probability': round(churn_prob, 3),
            'preferred_category': random.choice(list(CATEGORIES.keys()))
        }
        customers.append(customer)
    
    return pd.DataFrame(customers)

def calculate_rfm_segment(recency, frequency, monetary):
    """Calcula segmento RFM"""
    if recency <= 30 and frequency >= 10 and monetary >= 1000:
        return 'Champions'
    elif recency <= 60 and frequency >= 8:
        return 'Loyal Customers'
    elif recency <= 90 and frequency >= 5:
        return 'Potential Loyalists'
    elif recency <= 60 and frequency <= 3:
        return 'Recent Customers'
    elif recency <= 90 and frequency <= 5 and monetary >= 500:
        return 'Promising'
    elif recency <= 120 and frequency >= 3:
        return 'Customers Needing Attention'
    elif recency <= 180 and frequency >= 2:
        return 'About to Sleep'
    elif recency <= 240 and monetary >= 800:
        return 'At Risk'
    elif recency <= 300 and monetary >= 1000:
        return "Can't Lose Them"
    elif recency <= 365 and frequency <= 2:
        return 'Hibernating'
    else:
        return 'Lost'

def generate_transactions(n_transactions=100000, customers_df=None, products_df=None):
    """Genera transacciones realistas con estacionalidad"""
    transactions = []
    
    # Fechas: últimos 24 meses
    end_date = datetime.now()
    start_date = end_date - timedelta(days=730)
    
    # Distribución de países (normalizar para que sumen 1)
    country_probs = np.array([v['region_prob'] for v in COUNTRIES.values()])
    country_probs = country_probs / country_probs.sum()
    countries_list = list(COUNTRIES.keys())
    
    for i in range(n_transactions):
        # Fecha con estacionalidad (más ventas en Nov-Dec)
        days_back = random.randint(0, 730)
        transaction_date = end_date - timedelta(days=days_back)
        
        # Boost para Black Friday / Navidad
        month = transaction_date.month
        if month in [11, 12]:
            if random.random() > 0.3:  # 70% más probabilidad
                pass
        
        country = np.random.choice(countries_list, p=country_probs)
        country_info = COUNTRIES[country]
        city = random.choice(country_info['cities'])
        
        # Seleccionar producto
        if products_df is not None and len(products_df) > 0:
            product = products_df.sample(1).iloc[0]
            product_id = product['product_id']
            product_name = product['product_name']
            category = product['category']
            subcategory = product['subcategory']
            unit_price = product['base_price']
            cost_price = product['cost_price']
        else:
            category = random.choice(list(CATEGORIES.keys()))
            subcategory = random.choice(CATEGORIES[category]['subcategories'])
            product_id = f'P{random.randint(1, 500):05d}'
            product_name = f'{category} Product'
            price_range = CATEGORIES[category]['price_range']
            unit_price = round(random.uniform(*price_range), 2)
            cost_price = unit_price * 0.6
        
        # Seleccionar cliente
        if customers_df is not None and len(customers_df) > 0:
            customer = customers_df.sample(1).iloc[0]
            customer_id = customer['customer_id']
            customer_segment = customer['rfm_segment']
        else:
            customer_id = f'C{random.randint(1, 50000):06d}'
            customer_segment = random.choice(['VIP', 'Regular', 'New', 'Churned'])
        
        quantity = random.randint(1, 10)
        discount = round(random.choice([0, 0, 0, 0.05, 0.10, 0.15, 0.20, 0.30]), 2)
        
        total_amount = round(quantity * unit_price * (1 - discount), 2)
        shipping_cost = round(random.uniform(5, 30), 2)
        
        transaction = {
            'transaction_id': f'T{i+1:08d}',
            'date': transaction_date,
            'customer_id': customer_id,
            'country': country,
            'region': fake.state() if country == 'USA' else city,
            'city': city,
            'product_id': product_id,
            'product_name': product_name,
            'category': category,
            'subcategory': subcategory,
            'quantity': quantity,
            'unit_price': unit_price,
            'total_amount': total_amount,
            'discount_applied': discount,
            'payment_method': random.choice(PAYMENT_METHODS),
            'shipping_cost': shipping_cost,
            'delivery_time': random.randint(5, 30),
            'customer_segment': customer_segment,
            'device_type': np.random.choice(DEVICE_TYPES, p=[0.45, 0.45, 0.10]),
            'traffic_source': np.random.choice(TRAFFIC_SOURCES, p=[0.30, 0.25, 0.20, 0.15, 0.10]),
            'currency': country_info['currency'],
            'exchange_rate': country_info['exchange_rate'],
            'total_amount_usd': round(total_amount / country_info['exchange_rate'], 2),
            'cost_price': cost_price,
            'profit': round(total_amount - (cost_price * quantity), 2)
        }
        transactions.append(transaction)
    
    return pd.DataFrame(transactions)

def generate_all_data(n_transactions=100000, n_customers=50000, n_products=500):
    """Genera todos los datos"""
    print("Generando productos...")
    products_df = generate_products(n_products)
    
    print("Generando clientes...")
    customers_df = generate_customers(n_customers)
    
    print("Generando transacciones...")
    transactions_df = generate_transactions(n_transactions, customers_df, products_df)
    
    print("¡Datos generados exitosamente!")
    return transactions_df, customers_df, products_df

if __name__ == "__main__":
    # Test
    transactions, customers, products = generate_all_data(1000, 500, 100)
    print("\nTransactions shape:", transactions.shape)
    print("Customers shape:", customers.shape)
    print("Products shape:", products.shape)
