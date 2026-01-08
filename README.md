# Trading SDK – BAJAJ BROKING

A robust **Trading SDK Demo** built with a modern stack: **FastAPI** for the backend, **SQLAlchemy** for database orchestration, and **Streamlit** for a responsive frontend. This project simulates a professional trading environment including order execution, portfolio management, and persistent data storage.



---

## 🚀 Features

* **Instrument Management**: Dynamically view 50+ instruments with real-time price simulations.
* **Order Execution**: Place `BUY`/`SELL` orders with `MARKET` and `LIMIT` logic.
* **Trade Auditing**: A complete history of every executed trade with price and time metadata.
* **Portfolio Tracking**: Automated calculation of holdings, quantities, and average buy prices.

---

## 🛠️ Tech Stack

* **Backend:** [FastAPI] (High-performance Python API)
* **Frontend:** [Streamlit] (Data-centric UI)
* **Database:** [SQLAlchemy]with SQLite (Easy to port to PostgreSQL)
* **Validation:** [Pydantic] (Data schemas)

---

## 📁 Project Structure

```text
trading-sdk-demo/
├── screenshots/
│   ├── backend_API         # FastAPI application & API routes
│   ├── frontend
    
├── backend/
│   ├── main.py          # FastAPI application & API routes
│   ├── seed_instruments.py
│   ├── services.py
│   ├── storage.py
│   ├── models.py        # SQLAlchemy database models
│   ├── database.py      # SQLite connection & session setup
│   ├── trading.db
│   ├── exceptions.py         
│   └── init_dp.py      # Backend dependencies
└── frontend/
    ├── app.py           # Streamlit UI dashboard
   
