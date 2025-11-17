"""
E-commerce Data Cleaning & Preprocessing
Dataset: Online Retail (UCI ML Repository)
Location: data/raw/OnlineRetail.csv

This script loads the dataset, cleans it, creates new useful features,
and finally produces separate tables based on the ER diagram:

- Customer
- Product
- Invoice
- InvoiceItem
"""

import os
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ================================================================
# STEP 1 — Load Dataset
# ================================================================
print("\n   Loading Online Retail Dataset...")
df = pd.read_csv("data/raw/OnlineRetail.csv", encoding='latin1')

print("  Dataset loaded successfully!")
print("Shape:", df.shape)
print("Columns:", list(df.columns))

# ================================================================
# STEP 2 — Quick Overview
# ================================================================
print("\n   Preview of Data:")
print(df.head())

print("\n   Dataset Info:")
df.info()

print("\n   Summary Statistics:")
print(df.describe())

# ================================================================
# STEP 3 — Data Cleaning
# ================================================================
print("\n   Cleaning Data...")

# Remove rows with missing CustomerID
df_clean = df.dropna(subset=['CustomerID'])

# Remove negative quantities and prices
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]

# Remove duplicates
df_clean = df_clean.drop_duplicates()

# Fix datatypes
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
df_clean['CustomerID'] = df_clean['CustomerID'].astype(int)

print("  Cleaning completed!")
print("Cleaned shape:", df_clean.shape)

# ================================================================
# STEP 4 — Feature Engineering
# ================================================================
print("\n   Creating new features...")

# Total revenue for each row
df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['UnitPrice']

# Date-based features
df_clean['Year'] = df_clean['InvoiceDate'].dt.year
df_clean['Month'] = df_clean['InvoiceDate'].dt.month
df_clean['Day'] = df_clean['InvoiceDate'].dt.day
df_clean['Hour'] = df_clean['InvoiceDate'].dt.hour
df_clean['DayOfWeek'] = df_clean['InvoiceDate'].dt.dayofweek
df_clean['Quarter'] = df_clean['InvoiceDate'].dt.quarter

print("  Feature engineering completed!")

# ================================================================
# STEP 5 — ER-Diagram Based Tables
# ================================================================
print("\n   Creating ER-diagram tables...")

# Customer Table
customers = df_clean.groupby('CustomerID').agg({
    'Country': 'first',
    'InvoiceDate': 'min',
    'TotalPrice': 'sum'
}).rename(columns={
    'InvoiceDate': 'FirstPurchaseDate',
    'TotalPrice': 'TotalSpent'
}).reset_index()

# Product Table
products = df_clean.groupby('StockCode').agg({
    'Description': 'first',
    'UnitPrice': 'mean',
    'Quantity': 'sum'
}).rename(columns={
    'Quantity': 'TotalSold'
}).reset_index()

# Invoice Table
invoices = df_clean.groupby('InvoiceNo').agg({
    'CustomerID': 'first',
    'InvoiceDate': 'first',
    'TotalPrice': 'sum'
}).reset_index()

# Invoice Items
invoice_items = df_clean[['InvoiceNo', 'StockCode', 'Description',
                          'Quantity', 'UnitPrice', 'TotalPrice']]

print("  ER tables created!")

# ================================================================
# STEP 6 — Save Outputs
# ================================================================

os.makedirs("data/processed", exist_ok=True)
print("\n   Saving cleaned files...")

customers.to_csv("data/processed/customers.csv", index=False)
products.to_csv("data/processed/products.csv", index=False)
invoices.to_csv("data/processed/invoices.csv", index=False)
invoice_items.to_csv("data/processed/invoice_items.csv", index=False)
df_clean.to_csv("data/processed/ecommerce_cleaned.csv", index=False)

print("  All files saved in data/processed/")

# ================================================================
# STEP 7 — Data Quality Summary
# ================================================================
print("\n   Data Quality Summary")
print("Total Records:", len(df_clean))
print("Unique Customers:", df_clean['CustomerID'].nunique())
print("Unique Products:", df_clean['StockCode'].nunique())
print("Unique Invoices:", df_clean['InvoiceNo'].nunique())
print("Total Revenue: £", df_clean['TotalPrice'].sum())

print("\n Preprocessing completed successfully!")

