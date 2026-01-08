import streamlit as st
import requests
from datetime import datetime

BASE_URL = "http://localhost:8000/api/v1"

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Trading SDK Demo",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("📈 Trading SDK – Demo UI")
#st.write("Demo interface to view instruments, place trades, and track portfolio.")

# ------------------ Load Instruments ------------------
st.header("📊 Available Instruments")
if st.button("Load Instruments"):
    try:
        response = requests.get(f"{BASE_URL}/instruments")
        response.raise_for_status()
        instruments = response.json()
        st.success(f"Loaded {len(instruments)} instruments")
        st.dataframe(instruments)
    except Exception as e:
        st.error(f"Failed to fetch instruments: {e}")

# ------------------ Place Order ------------------
st.header("📝 Place Order")


try:
    instruments_response = requests.get(f"{BASE_URL}/instruments")
    instruments_response.raise_for_status()
    instruments_data = instruments_response.json()
    symbols = [inst["symbol"] for inst in instruments_data]
except Exception:
    symbols = []
    st.warning("Could not load instruments for Place Order.")

with st.form("order_form"):
    col1, col2 = st.columns(2)
    with col1:
        symbol = st.selectbox("Symbol", symbols)
        side = st.selectbox("Side", ["BUY", "SELL"])
    with col2:
        order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
        quantity = st.number_input("Quantity", min_value=1, step=1)

        price = None
        if order_type == "LIMIT":
            price = st.number_input("Price", min_value=1.0)

    submitted = st.form_submit_button("Place Order")
    if submitted:
        payload = {
            "symbol": symbol,
            "side": side,
            "order_type": order_type,
            "quantity": quantity
        }
        if order_type == "LIMIT":
            payload["price"] = price

        try:
            response = requests.post(f"{BASE_URL}/orders", json=payload)
            response.raise_for_status()
            order = response.json()
            st.success(f"✅ Order placed successfully: ID {order.get('order_id')}")
            st.json(order)
        except Exception as e:
            st.error(f"❌ Failed to place order: {e}")

# ------------------ Executed Trades ------------------
st.header("📜 Executed Trades")
if st.button("Load Trades"):
    try:
        response = requests.get(f"{BASE_URL}/trades")
        response.raise_for_status()
        trades = response.json()
        if trades:
            for trade in trades:
                trade["executed_at"] = datetime.fromisoformat(trade["executed_at"]).strftime("%Y-%m-%d %H:%M:%S")
            st.dataframe(trades)
        else:
            st.info("No trades executed yet.")
    except Exception as e:
        st.error(f"Failed to fetch trades: {e}")

# ------------------ Portfolio ------------------
st.header("💼 Portfolio")
if st.button("Load Portfolio"):
    try:
        response = requests.get(f"{BASE_URL}/portfolio")
        response.raise_for_status()
        portfolio = response.json()
        if portfolio:
            st.dataframe(portfolio)
            
            total_symbols = len(portfolio)
            total_quantity = sum(item["quantity"] for item in portfolio)
            avg_price = round(sum(item["avg_price"] for item in portfolio) / total_symbols, 2)
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Symbols", total_symbols)
            col2.metric("Total Quantity", total_quantity)
            col3.metric("Avg. Price", avg_price)
        else:
            st.info("Portfolio is empty.")
    except Exception as e:
        st.error(f"Failed to fetch portfolio: {e}")
