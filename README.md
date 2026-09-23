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

The dataset used in this project is the Sample Superstore dataset obtained from Kaggle.

Dataset Source: https://www.kaggle.com/datasets/binib1997/superstore


### Dataset Details

- Records: 9,994
- Columns: 21
- Data Type: Structured tabular data
- Domain: Retail Sales and Business Analytics

The dataset contains information about orders, customers, products, sales, profit, regions, categories, and shipping details.

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

## Project Structure Sample
  Sample - Superstore.csv/
│
├── Anusha superstore.ipynb
├── Sample - Superstore.csv
├── superstore_cleaned.csv
├── sales_forecast_model.pkl
├── app.py
├── requirements.txt
├── Anusha_ProjectReport.docx
└── README.md

## How to Run the Project

## 1. Open the project folder
    Open Command Prompt or Terminal and navigate to the project folder:

```bash
cd "C:\Users\beera\OneDrive\Desktop\sales forecasting\Sample - Superstore.csv"
 
 ## Dashboard

The Streamlit dashboard provides interactive analysis of sales, profit, quantity, and orders.

Users can filter the dashboard by:

- Year
- Region
- Category

The KPI values and charts update dynamically based on the selected filters.

The dashboard includes:

- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Top 10 Products by Sales
- Profit by Category
- Actual vs Predicted Sales Forecast

## Project Outcome

This project demonstrates practical skills in:

- Data cleaning and preprocessing
- Exploratory Data Analysis
- Business KPI analysis
- Data visualization
- Feature engineering
- Machine learning
- Time-based sales forecasting
- Model evaluation
- Interactive dashboard development
- Python-based data analytics
  
 ## Author

Anusha Beeram

B.Tech Computer Science and Engineering  
Specialization: Artificial Intelligence and Machine Learning  
Chaitanya Deemed to be University  
Graduation Year: 2027 