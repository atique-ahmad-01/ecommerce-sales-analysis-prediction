import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os

# ---------------------------
# Paths
# ---------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "data", "processed", "regression", "output")
PRED_CSV = os.path.join(MODEL_DIR, "predictions.csv")

MODEL_FILE = os.path.join(MODEL_DIR, "best_regression_model.pkl")
LE_STOCK_FILE = os.path.join(MODEL_DIR, "stock_encoder.pkl")
LE_COUNTRY_FILE = os.path.join(MODEL_DIR, "country_encoder.pkl")
LE_CUSTOMER_FILE = os.path.join(MODEL_DIR, "customer_encoder.pkl")

# ---------------------------
# Load model and encoders
# ---------------------------
model = joblib.load(MODEL_FILE)
le_stock = joblib.load(LE_STOCK_FILE)
le_country = joblib.load(LE_COUNTRY_FILE)
le_customer = joblib.load(LE_CUSTOMER_FILE)

# ---------------------------
# App title
# ---------------------------
st.title("E-commerce Sales Prediction")
st.write("Predict the Total Price of an invoice/item based on product, customer, and quantity details.")

# ---------------------------
# Sidebar inputs
# ---------------------------
st.sidebar.header("Input Features")
stock = st.sidebar.selectbox("Stock Code", le_stock.classes_)
customer_id = st.sidebar.selectbox("Customer ID", le_customer.classes_)
country = st.sidebar.selectbox("Country", le_country.classes_)
quantity = st.sidebar.number_input("Quantity", min_value=1, value=1)
unit_price = st.sidebar.number_input("Unit Price", min_value=0.0, value=10.0)
year = st.sidebar.number_input("Year", min_value=2010, max_value=2025, value=2011)
month = st.sidebar.number_input("Month", min_value=1, max_value=12, value=12)
day = st.sidebar.number_input("Day", min_value=1, max_value=31, value=1)
hour = st.sidebar.number_input("Hour", min_value=0, max_value=23, value=12)
day_of_week = st.sidebar.number_input("Day of Week", min_value=0, max_value=6, value=2)
quarter = st.sidebar.number_input("Quarter", min_value=1, max_value=4, value=4)

# ---------------------------
# Encode categorical inputs
# ---------------------------
stock_enc = le_stock.transform([stock])[0]
country_enc = le_country.transform([country])[0]
customer_enc = le_customer.transform([int(customer_id)])[0]

# ---------------------------
# Load previous predictions
# ---------------------------
df_pred = pd.read_csv(PRED_CSV)  # columns: ['y_true', 'y_pred']

# ---------------------------
# Predict button and visualization
# ---------------------------
if st.button("Predict Total Price"):
    # Create input dataframe
    X_input = pd.DataFrame([[
        stock_enc, customer_enc, country_enc, quantity, unit_price,
        year, month, day, hour, day_of_week, quarter
    ]], columns=[
        'StockCode_enc', 'CustomerID_enc', 'Country_enc', 'Quantity', 'UnitPrice',
        'Year', 'Month', 'Day', 'Hour', 'DayOfWeek', 'Quarter'
    ])
    
    # Predict
    new_pred = model.predict(X_input)[0]
    st.success(f"Predicted Total Price: £{new_pred:.2f}")
    
    # ---------------------------
    # Update visualization with new point
    # ---------------------------
    st.subheader("Predicted vs Actual (Scatter) with New Prediction")
    
    # Sort by actual values
    df_sorted = df_pred.sort_values(by='y_true').reset_index(drop=True)
    
    plt.figure(figsize=(8,6))
    plt.scatter(df_sorted['y_true'], df_sorted['y_pred'], alpha=0.3, label="Previous Predictions")
    
    # Plot new prediction as black
    plt.scatter(0, new_pred, color='black', s=100, label="New Prediction")
    
    plt.xlabel("Actual TotalPrice")
    plt.ylabel("Predicted TotalPrice")
    plt.title("Predicted vs Actual Scatter")
    plt.legend()
    st.pyplot(plt)
