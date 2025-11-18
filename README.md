# Project Overview

```
ecommerce-sales-analysis-prediction/
│
├── data/
│   ├── raw/
│   │   └── Online_Retail.xlsx          # Original dataset
│   │   └── OnlineRetail.csv          
│   ├── processed/
│   │   ├── ecommerce_cleaned.csv       # Cleaned dataset
│   │   ├── customers.csv               # Customer table
│   │   ├── products.csv                # Product table
│   │   ├── invoices.csv                # Invoice table
│   │   └── invoice_items.csv           # Invoice items table
│   └── models/                         # TODO: Trained models output
│
├── src/
│   ├── data_preprocessing.py           # Data cleaning script
│   ├── model_training.py               # TODO: ML training script
│   └── utils.py                        # TODO: Helper functions
│
├── tableau/
│   ├── ecommerce_dashboard.twbx        # Tableau workbook
│   └── dashboard_screenshots/          # Dashboard images
│
├── streamlit/                          # TODO: Streamlit application
│
├── results/
│   └── ER Diagram.png                    # Entity relationship diagram
│
├── docs/
│   ├── report_ecommerce_preprocessing.md # Data cleansing summary
│   └── report_tableau_dashboard.md       # Tableau dashboard report
│ 
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
└── .gitignore                          # Git ignore file
```