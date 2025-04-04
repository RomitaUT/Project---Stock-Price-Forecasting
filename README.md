** 📈 Stock Price Forecasting with Prophet & ARIMA

Forecasting future stock prices using time series models can provide powerful insights for analysts, traders, and financial planners. This project demonstrates two popular techniques for time series forecasting using Python:

Facebook Prophet (trend + seasonality based)

ARIMA (classic statistical model)

All forecasts are generated for Apple Inc. (AAPL) with data ranging from 2018 to 2024, using Yahoo Finance.

** 🔍 Project Overview

This project explores and compares two powerful forecasting techniques:

📊 Visualizes historical closing prices

🔮 Forecasts stock prices for the next 180 days using Prophet

🔁 Forecasts the same period using ARIMA

📉 Calculates and compares model accuracy using Mean Absolute Error (MAE)

📈 Compares both models' forecasts side-by-side with actual data

** 🧰 Tech Stack

Python 3.10+

yfinance – to pull stock data

Prophet – forecasting model by Meta

statsmodels – ARIMA modeling

Matplotlib / Pandas for visualizations & data manipulation

** 📂 Project Structure

Stock-Price-Forecasting/
├── data/                      # (optional)
├── notebooks/
│   └── 01_forecasting_aapl.ipynb
├── requirements.txt
├── README.md

** 📉 Forecasting Outputs

Prophet Forecast:

Captures overall trend and seasonality

Automatically adjusts for holidays and irregularities

ARIMA Forecast:

Relies on autocorrelation, moving averages, and differencing

Assumes consistent time series behavior

Model Accuracy:

MAE (Mean Absolute Error) was calculated to compare Prophet predictions with actuals

** 📌 How to Run This Project

Clone the repository

Install required packages:

pip install -r requirements.txt

Open the notebook and run:

jupyter notebook notebooks/01_forecasting_aapl.ipynb

** 🌟 Possible Improvements

Add interactive Streamlit app to accept custom tickers

Export results to PDF/HTML for sharing

Add more models (SARIMA, LSTM, XGBoost)

** 👤 Author

Romita Thally
Financial Analyst & Data Enthusiast