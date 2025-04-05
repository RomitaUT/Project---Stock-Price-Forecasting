# 📈 Stock Price Forecasting App

A sleek, interactive Streamlit web app that forecasts stock prices using Facebook's Prophet time series model. The app allows users to select a stock, choose a prediction horizon, and visualize the future trend with confidence intervals.

![App Preview](visuals/forecast_ui_screenshot.png)

---

## 🚀 Features

- 🔍 Select stock tickers from a dropdown (AAPL, TSLA, GOOGL, etc.)
- 📆 Choose forecast horizon (1 to 5 years)
- 📊 Interactive Plotly chart with historical data, predictions, and confidence intervals
- 📄 Forecasted data table
- 🌙 Clean dark theme with stylish UI elements

---

## 📸 UI Snapshot

![Forecast Chart](visuals/forecast_chart_screenshot.png)

---

## ⚙️ How It Works

1. **Data Collection**: Pulls historical stock price data using `yfinance`.
2. **Data Preparation**: Transforms the data for compatibility with `Prophet`.
3. **Modeling**: Fits a time series model and generates forecasts.
4. **Visualization**: Displays the results with interactive Plotly charts in Streamlit.

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Data**: yFinance
- **Forecasting**: Facebook Prophet
- **Visualization**: Plotly

---

## 🧑‍💻 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/stock-price-forecasting-app.git
   cd stock-price-forecasting-app

2. **Create and Activate a Virtual Environment (Recommended)**
    conda create -n stockforecast python=3.10
    conda activate stockforecast

3. **Install All Required Dependencies**
    pip install -r requirements.txt
    
    **If Prophet throws errors:**
    pip install prophet
    
4. **Run the App**
    streamlit run app.py

**Then open your browser and go to:**
http://localhost:8501

## 📂 Project Structure

stock-price-forecasting/
├── app.py                  # Streamlit app
├── README.md               # Project documentation
├── requirements.txt        # All dependencies
└── visuals/                # Optional: saved chart images

## 🧪 Possible Improvements

    Export forecast data as downloadable CSV

    Add ARIMA model comparison

    Let users upload their own ticker list

    Deploy app via Streamlit Cloud


## 🙌 Acknowledgements
    Streamlit

    Facebook Prophet

    Yahoo Finance via yfinance