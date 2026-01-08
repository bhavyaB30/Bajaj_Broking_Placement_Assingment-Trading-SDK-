# Trading SDK – Demo UI

A robust **Trading SDK Demo** built with a modern stack: **FastAPI** for the backend, **SQLAlchemy** for database orchestration, and **Streamlit** for a responsive frontend. This project simulates a professional trading environment including order execution, portfolio management, and persistent data storage.

[Image of a system architecture diagram showing a FastAPI backend connecting to a SQLite database and a Streamlit frontend]

---

## 🚀 Features

* **Instrument Management**: Dynamically view 50+ instruments with real-time price simulations.
* **Order Execution**: Place `BUY`/`SELL` orders with `MARKET` and `LIMIT` logic.
* **Trade Auditing**: A complete history of every executed trade with price and time metadata.
* **Portfolio Tracking**: Automated calculation of holdings, quantities, and average buy prices.

---

## 🛠️ Tech Stack

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (High-performance Python API)
* **Frontend:** [Streamlit](https://streamlit.io/) (Data-centric UI)
* **Database:** [SQLAlchemy](https://www.sqlalchemy.org/) with SQLite (Easy to port to PostgreSQL)
* **Validation:** [Pydantic](https://docs.pydantic.dev/) (Data schemas)

---

## 📁 Project Structure

```text
trading-sdk-demo/
├── backend/
│   ├── main.py          # FastAPI application & API routes
│   ├── models.py        # SQLAlchemy database models
│   ├── database.py      # SQLite connection & session setup
│   ├── crud.py          # Database operations (Create, Read, Update)
│   └── requirements.txt # Backend dependencies
└── frontend/
    ├── app.py           # Streamlit UI dashboard
    └── requirements.txt # Frontend dependencies