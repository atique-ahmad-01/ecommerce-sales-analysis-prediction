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
│   └── models/
│
├── src/
│   ├── data_preprocessing.py           # Data cleaning script
│   ├── model_training.py               # ML training script
│   └── utils.py                        # Helper functions
│
├── streamlit/
│   └── app.py                          # Streamlit application
│
├── results/
│
├── docs/
│
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
└── .gitignore                          # Git ignore file
```