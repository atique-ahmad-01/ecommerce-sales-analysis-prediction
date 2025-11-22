# Project Overview

```
ecommerce-sales-analysis-prediction/
│
├── .gitignore
├── LICENSE
├── README.md
├── data/
│   ├── raw/
│   │   ├── Online Retail.xlsx
│   │   └── OnlineRetail.csv
│   └── processed/
│       ├── ecommerce_cleaned.csv
│       ├── customers.csv
│       ├── products.csv
│       ├── invoices.csv
│       ├── invoice_items.csv
│       └── regression/
│           └── output/
│               ├── best_regression_model.pkl
│               ├── stock_encoder.pkl
│               ├── country_encoder.pkl
│               ├── customer_encoder.pkl
│               └── predictions.csv
│
├── notebooks/
│   └── regression_model.ipynb
│
├── src/
│   └── data_preprocessing.py
│
├── streamlit/
│   └── app.py
│
├── tableau/
│   ├── ecommerce_dashboard.twbx
│   ├── annie_dashboard/
│   │   └── Customer Spend Analysis Dashboard.png
│   └── dashboard_screenshots/
│       ├── Dashboard_preview.png
│       ├── Top Customer Spending.png
│       ├── Sales Overview.png
│       ├── Dashboard_1.png
│       ├── Dashboard_2.png
│       ├── Revenue by Hour.png
│       ├── KPI: Total Revenue.png
│       ├── Dashboard_containers.png
│       ├── top products.png
│       ├── combine tables.png
│       └── Dashboard.png
│
├── results/
│   ├── predicted_vs_actual.png
│   ├── feature_importance.png
│   ├── ER Diagram.png
│   ├── model_r2_comparison.png
│   └── residuals_distribution.png
│
├── docs/
│   ├── report_ecommerce_preprocessing.md
│   ├── report_regression_pipeline.md
│   └── report_tableau_dashboard.md
│
└── requirements.txt

```