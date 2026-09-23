import streamlit as st
import pandas as pd
import joblib

# Page Configuration

st.set_page_config(
    page_title="Superstore Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title

st.title("Superstore Sales & Forecasting Dashboard")
st.write(
    "Interactive dashboard for sales, profit, and business performance analysis."
)

# Load Cleaned Dataset

df = pd.read_csv("superstore_cleaned.csv")

# Sidebar Filters

st.sidebar.header("Filters")

selected_year = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

# Apply Filters

filtered_df = df[
    (df["Year"].isin(selected_year)) &
    (df["Region"].isin(selected_region)) &
    (df["Category"].isin(selected_category))
]

# KPI Calculations

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_quantity = filtered_df["Quantity"].sum()
total_orders = filtered_df["Order ID"].nunique()

# KPI Cards

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Total Quantity",
    f"{total_quantity:,}"
)

col4.metric(
    "Total Orders",
    f"{total_orders:,}"
)

# Monthly Sales Trend

st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    filtered_df.groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Date"] = pd.to_datetime(
    monthly_sales["Year"].astype(str)
    + "-"
    + monthly_sales["Month"].astype(str)
    + "-01"
)

monthly_sales = monthly_sales.sort_values("Date")

st.line_chart(
    monthly_sales.set_index("Date")["Sales"]
)

# Sales by Category

st.subheader("Sales by Category")

category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_sales)

# Sales by Region

st.subheader("Sales by Region")

region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(region_sales)

# Top 10 Products by Sales

st.subheader("Top 10 Products by Sales")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

st.bar_chart(top_products)

# Profit by Category

st.subheader("Profit by Category")

category_profit = (
    filtered_df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_profit)

# Sales Forecasting

st.subheader("Sales Forecasting")

# Load trained XGBoost model
model = joblib.load("sales_forecast_model.pkl")

# Prepare forecasting data using complete historical dataset
forecast_data = (
    df.groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
)

forecast_data["Date"] = pd.to_datetime(
    forecast_data["Year"].astype(str)
    + "-"
    + forecast_data["Month"].astype(str)
    + "-01"
)

forecast_data = forecast_data.sort_values("Date")

# Create lag features
forecast_data["Lag_1"] = forecast_data["Sales"].shift(1)
forecast_data["Lag_2"] = forecast_data["Sales"].shift(2)
forecast_data["Lag_3"] = forecast_data["Sales"].shift(3)

# Create rolling average
forecast_data["Rolling_3"] = (
    forecast_data["Sales"]
    .shift(1)
    .rolling(3)
    .mean()
)

# Remove rows with missing lag values
forecast_data = forecast_data.dropna()

# Select model features
X_forecast = forecast_data[
    [
        "Month",
        "Year",
        "Lag_1",
        "Lag_2",
        "Lag_3",
        "Rolling_3"
    ]
]

# Generate predictions
forecast_data["Predicted Sales"] = model.predict(X_forecast)

# Display actual vs predicted sales
st.line_chart(
    forecast_data.set_index("Date")[
        ["Sales", "Predicted Sales"]
    ]
)

# Footer

st.markdown("---")

st.caption(
    "Built using Python, Pandas, XGBoost, Joblib, and Streamlit."
)