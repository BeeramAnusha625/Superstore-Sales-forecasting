# Superstore Sales & Forecasting System

## Project Overview

The Superstore Sales & Forecasting System is a data analytics and machine learning project built using the Sample Superstore dataset.

The project analyzes historical sales and profit performance and uses an XGBoost regression model to predict sales based on historical sales patterns. An interactive Streamlit dashboard is used to explore business performance through KPIs, charts, filters, and model predictions.

## Objectives

- Analyze historical sales and profit performance
- Identify sales trends across time, categories, and regions
- Analyze top-performing products
- Build a machine learning model for sales forecasting
- Evaluate model performance using MAE and RMSE
- Develop an interactive business intelligence dashboard

## Key Features

- Interactive Year, Region, and Category filters
- Total Sales KPI
- Total Profit KPI
- Total Quantity KPI
- Total Orders KPI
- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Top 10 Products by Sales
- Profit by Category
- XGBoost-based Sales Forecasting
- Actual vs Predicted Sales visualization

## Machine Learning

An XGBoost Regressor was used for sales forecasting.

### Features Used

- Month
- Year
- Lag 1 Sales
- Lag 2 Sales
- Lag 3 Sales
- 3-Month Rolling Average

### Model Evaluation

- MAE: 18,054.54
- RMSE: 22,707.00

The evaluation metrics are based on the chronological train-test split used in the project.

## Dataset

The project uses the Sample Superstore dataset containing approximately:

- 9,994 records
- 21 columns

The dataset contains information related to orders, customers, products, sales, profit, regions, and categories.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub