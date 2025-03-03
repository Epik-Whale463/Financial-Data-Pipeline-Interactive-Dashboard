from prophet import Prophet
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def generate_forecast():
    """Generate 6-month revenue forecast and save to CSV"""
    try:
        engine = create_engine(
            f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
            f"{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        )
        
        df = pd.read_sql_table('financial_reports', engine)
        
        prophet_df = df[['Date', 'Revenue']].rename(columns={'Date': 'ds', 'Revenue': 'y'})
        
        model = Prophet(seasonality_mode='multiplicative')
        model.fit(prophet_df)
        
        future = model.make_future_dataframe(periods=180)
        forecast = model.predict(future)
        
        forecast[['ds', 'yhat']].to_csv('../data/forecast.csv', index=False)
        print("Successfully generated forecast.csv")
        
    except Exception as e:
        print(f"Forecasting Error: {str(e)}")

if __name__ == "__main__":
    generate_forecast()