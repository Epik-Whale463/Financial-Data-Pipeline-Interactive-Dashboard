import os
import pandas as pd
import requests
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = 'financial_db'

def extract_local_data(file_path: str) -> pd.DataFrame:
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {str(e)}")
        return pd.DataFrame()

def extract_api_data(symbol: str) -> pd.DataFrame:
    try:
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}'
        params = {'interval': '1d', 'range': '1y'}
        response = requests.get(url, params=params)
        data = response.json()['chart']['result'][0]
        return pd.DataFrame({
            'Date': pd.to_datetime(data['timestamp'], unit='s'),
            'Close': data['indicators']['quote'][0]['close']
        })
    except Exception as e:
        print(f"API Error: {str(e)}")
        return pd.DataFrame()

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['Revenue', 'Expenses'])
    
    df['Profit'] = df['Revenue'] - df['Expenses']
    df['ROI'] = (df['Profit'] / df['Expenses']) * 100
    df['EBITDA'] = df['Profit'] + df.get('Depreciation', 0)
    
    df = df[df['Revenue'] > 0]
    return df

def load_to_db(df: pd.DataFrame) -> None:
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
    try:
        df.to_sql('financial_reports', engine, if_exists='replace', index=False)
        print("Data successfully loaded to PostgreSQL")
    except Exception as e:
        print(f"Database Error: {str(e)}")

if __name__ == "__main__":
    sales_data = extract_local_data('../data/mock_sales_data.csv')
    stock_data = extract_api_data('AAPL')
    
    cleaned_data = transform_data(sales_data)
    
    load_to_db(cleaned_data)