import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
import pandas as pd
from plotly import graph_objs as go

# ------------------------------------
# Streamlit App Config & Styling
# ------------------------------------
st.set_page_config(page_title="Stock Forecasting", layout="centered")
st.markdown("""
    <style>
        .main {
            background-color: #0f1117;
            color: #ffffff;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stSlider > div {
            color: #ffffff;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5rem 1.5rem;
        }
        .stButton > button:hover {
            background-color: #3e8e41;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📈 Stock Price Forecasting App")

# ------------------------------------
# Sidebar for Inputs
# ------------------------------------
with st.sidebar:
    st.header("🛠️ Settings")
    tickers = ["AAPL", "TSLA", "GOOGL", "MSFT", "AMZN", "META", "NFLX"]
    ticker = st.selectbox("Select stock ticker:", tickers)
    n_years = st.slider("Years of prediction:", 1, 5)
    period = n_years * 365

# ------------------------------------
# Forecast Button
# ------------------------------------
st.markdown("---")
if st.button("✨ Run Forecast"):
    try:
        # Load stock data
        data = yf.download(ticker, start="2018-01-01")
        data = data.reset_index()

        # Prepare data for Prophet
        df_prophet = pd.DataFrame()
        df_prophet["ds"] = pd.to_datetime(data["Date"])
        df_prophet["y"] = data["Close"]

        # Fit Prophet model
        model = Prophet(daily_seasonality=True)
        model.fit(df_prophet)

        # Make future predictions
        future = model.make_future_dataframe(periods=period)
        forecast = model.predict(future)

        # Custom Plotly chart
        st.subheader("📊 Forecast Plot")

        fig = go.Figure()

        # Historical data
        fig.add_trace(go.Scatter(x=df_prophet["ds"], y=df_prophet["y"],
                                 mode='lines', name='Actual',
                                 line=dict(color='lightblue', width=2)))

        # Forecasted data
        fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat"],
                                 mode='lines', name='Forecast',
                                 line=dict(color='orange', width=3)))

        # Confidence intervals
        fig.add_trace(go.Scatter(
            x=forecast["ds"], y=forecast["yhat_upper"],
            mode='lines', name='Upper Bound',
            line=dict(width=0), fill='tonexty', fillcolor='rgba(255, 165, 0, 0.2)',
            showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=forecast["ds"], y=forecast["yhat_lower"],
            mode='lines', name='Lower Bound',
            line=dict(width=0), fill='tonexty', fillcolor='rgba(255, 165, 0, 0.2)',
            showlegend=False
        ))

        fig.update_layout(
            title=f"{ticker} Stock Price Forecast",
            title_font=dict(size=24),
            xaxis_title="Date",
            yaxis_title="Price (USD)",
            template="plotly_dark",
            font=dict(family="Arial", size=14),
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)

        # Forecast Table
        st.subheader("📄 Forecast Data (Tail)")
        st.dataframe(forecast.tail(), use_container_width=True)

    except Exception as e:
        st.error(f"⚠️ Something went wrong:\n{e}")
