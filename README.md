# Financial Data Pipeline & Interactive Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-orange)
![PowerBI](https://img.shields.io/badge/Power_BI-Desktop-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## **Dashboard Preview**
![Dashboard Screenshot](screenshots/financial_dashboard.png)

## 📊 Project Overview

This project creates an end-to-end financial data solution that:

1. **Collects** financial data from multiple sources (CSV, Excel, Yahoo Finance API)
2. **Processes** the data (cleaning, calculating KPIs like ROI and EBITDA)
3. **Stores** everything in a PostgreSQL database
4. **Visualizes** insights through an interactive Power BI dashboard

The result? Automated financial reporting that improves audit efficiency, compliance tracking, and financial forecasting.

## ✨ Key Features

- **Automated Data Pipeline**
  - Extracts data from diverse sources
  - Cleans and transforms data
  - Calculates important financial metrics
  - Loads everything into a centralized database

- **Interactive Dashboard**
  - Dynamic Profit & Loss statements
  - Budget vs. Actual comparisons
  - Revenue forecasting using Facebook Prophet
  - Visual KPI tracking

- **Business Benefits**
  - Reduces manual reporting work
  - Improves data accuracy
  - Provides real-time financial insights
  - Supports data-driven decision making

## 🛠️ Tech Stack

- **Python 3.9+**: Core programming language
- **Pandas & SQLAlchemy**: Data manipulation and database interaction
- **PostgreSQL**: Relational database 
- **Power BI**: Interactive data visualization
- **Facebook Prophet**: Time series forecasting
- **Git/GitHub**: Version control

## 📋 Installation Guide

### Prerequisites
1. Install [Python 3.9+](https://www.python.org/downloads/)
2. Install [PostgreSQL](https://www.postgresql.org/download/)
3. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/financial-data-pipeline.git
   cd financial-data-pipeline
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL database**
   - Create a database named `financial_db`
   - Update the connection string in `scripts/etl_pipeline.py`:
     ```python
     engine = create_engine('postgresql://username:password@localhost:5432/financial_db')
     ```

4. **Download sample data**
   - Get `mock_sales_data.csv` and `mock_budget_data.xlsx` from the `data/` folder

## 🚀 Usage

### Running the ETL Pipeline

1. Execute the main pipeline script:
   ```bash
   python scripts/etl_pipeline.py
   ```
   
2. This will:
   - Extract data from files and APIs
   - Transform the data (clean and calculate KPIs)
   - Load data into PostgreSQL

### Exploring the Dashboard

1. Open Power BI Desktop
2. Load the `dashboard/financial_dashboard.pbix` file
3. Connect to your PostgreSQL database
4. Explore financial insights:
   - View P&L statements
   - Compare budgets to actuals
   - Analyze revenue forecasts

## 📁 Project Structure

```
financial-data-pipeline/
├── data/                   # Sample data files
├── scripts/                # Python ETL code
│   ├── etl_pipeline.py     # Main pipeline script
│   ├── forecasting.py      # Prophet forecasting model
├── sql/                    # Database scripts
│   ├── schema.sql          # Database schema
├── dashboard/              # Power BI files
│   ├── financial_dashboard.pbix
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgements

- Yahoo Finance API for financial data
- Facebook Prophet for time series forecasting
- EY for inspiring this project

---

Let's build a better working world! 🚀
