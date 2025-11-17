# E-commerce Data Cleaning & Preprocessing Report

**Dataset:** Online Retail (UCI Machine Learning Repository)  
**Source File:** `data/raw/OnlineRetail.csv`  
**Processed Files:** `data/processed/ecommerce_cleaned.csv`, `customers.csv`, `products.csv`, `invoices.csv`, `invoice_items.csv`

**Author:** Atique Ahmad | MSDS25030  
**Date:** 17-Nov-2025  

---

## 1. Project Overview

The goal of this preprocessing script is to **clean, structure, and enhance** the Online Retail dataset for further analysis, visualization, and predictive modeling.  

Key objectives:

- Remove invalid or missing data  
- Create new features for analysis (e.g., revenue, date-time components)  
- Organize data into **ER-diagram based tables**: Customer, Product, Invoice, InvoiceItem  
- Save processed datasets for **ML modeling and visualization**

---

## 2. Dataset Overview

- **Original Dataset Shape:** `(541,909 rows × 8 columns)`  
- **Columns:**

| Column      | Description |
|------------|-------------|
| InvoiceNo   | Invoice identifier |
| StockCode   | Product code |
| Description | Product description |
| Quantity    | Quantity purchased |
| InvoiceDate | Invoice date and time |
| UnitPrice   | Price per unit |
| CustomerID  | Customer identifier |
| Country     | Customer's country |

- **Missing Values:**
  - `CustomerID`: 135,080 missing entries  
  - `Description`: 1,454 missing entries  
- **Negative or zero values:** Present in `Quantity` and `UnitPrice`

---

## 3. Data Cleaning

Steps performed:

1. Removed rows with **missing CustomerID**.  
2. Removed rows with **negative or zero Quantity and UnitPrice**.  
3. Removed **duplicate records**.  
4. Converted `InvoiceDate` to **datetime format**.  
5. Converted `CustomerID` to **integer type**.

**Cleaned Dataset Shape:** `(392,692 rows × 8 columns)`

---

## 4. Feature Engineering

New features created:

| Feature        | Description |
|----------------|-------------|
| TotalPrice     | Revenue per row (`Quantity × UnitPrice`) |
| Year           | Invoice year |
| Month          | Invoice month |
| Day            | Invoice day |
| Hour           | Invoice hour |
| DayOfWeek      | Day of the week (0=Monday) |
| Quarter        | Fiscal quarter |

These features will support **sales analysis**, **trend visualization**, and **predictive modeling**.

---

## 5. ER-Diagram Based Tables

The cleaned dataset was transformed into the following tables:

### 5.1 Customer Table

| Column            | Description |
|------------------|-------------|
| CustomerID        | Unique customer identifier |
| Country           | Customer country |
| FirstPurchaseDate | Date of first purchase |
| TotalSpent        | Total revenue by customer |

**Total Customers:** 4,338

---

### 5.2 Product Table

| Column      | Description |
|------------|-------------|
| StockCode  | Product code |
| Description| Product description |
| UnitPrice  | Average unit price |
| TotalSold  | Total quantity sold |

**Total Products:** 3,665

---

### 5.3 Invoice Table

| Column      | Description |
|------------|-------------|
| InvoiceNo   | Invoice identifier |
| CustomerID  | Customer identifier |
| InvoiceDate | Invoice date |
| TotalPrice  | Total revenue for invoice |

**Total Invoices:** 18,532

---

### 5.4 InvoiceItem Table

| Column      | Description |
|------------|-------------|
| InvoiceNo   | Invoice identifier |
| StockCode   | Product code |
| Description | Product description |
| Quantity    | Quantity purchased |
| UnitPrice   | Price per unit |
| TotalPrice  | Revenue per item |

**Total Records:** 392,692

---

## 6. Data Quality Summary

| Metric               | Value |
|----------------------|-------|
| Total Records        | 392,692 |
| Unique Customers     | 4,338 |
| Unique Products      | 3,665 |
| Unique Invoices      | 18,532 |
| Total Revenue        | £8,887,208.89 |

- No missing values remain after cleaning  
- All numeric and date fields are in proper formats  

---

## 7. Output Files

The following files were saved in `data/processed/`:

| File                     | Description |
|--------------------------|-------------|
| ecommerce_cleaned.csv     | Full cleaned dataset with engineered features |
| customers.csv             | Customer table |
| products.csv              | Product table |
| invoices.csv              | Invoice table |
| invoice_items.csv         | InvoiceItem table |

---
