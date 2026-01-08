from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Instrument, Order, Trade, Portfolio

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/v1/instruments")
def get_instruments(db: Session = Depends(get_db)):
    return db.query(Instrument).all()

@app.post("/api/v1/orders")
def create_order(data: dict, db: Session = Depends(get_db)):
    instrument = db.query(Instrument).filter(
        Instrument.symbol == data["symbol"]
    ).first()

    if not instrument:
        raise HTTPException(status_code=404, detail="Instrument not found")

    order = Order(
        symbol=data["symbol"],
        side=data["side"],
        order_type=data["order_type"],
        quantity=data["quantity"],
        price=instrument.last_traded_price,
        status="FILLED"
    )
    db.add(order)
    db.commit()
    db.refresh(order)

    trade = Trade(
        order_id=order.id,
        symbol=order.symbol,
        side=order.side,
        quantity=order.quantity,
        price=order.price
    )
    db.add(trade)

    portfolio = db.query(Portfolio).filter(
        Portfolio.symbol == order.symbol
    ).first()

    if portfolio:
        total_qty = portfolio.quantity + order.quantity
        portfolio.avg_price = (
            (portfolio.avg_price * portfolio.quantity) +
            (order.price * order.quantity)
        ) / total_qty
        portfolio.quantity = total_qty
    else:
        portfolio = Portfolio(
            symbol=order.symbol,
            quantity=order.quantity,
            avg_price=order.price
        )
        db.add(portfolio)

    db.commit()
    return {"order_id": order.id, "status": "FILLED"}

@app.get("/api/v1/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/api/v1/trades")
def get_trades(db: Session = Depends(get_db)):
    return db.query(Trade).all()

@app.get("/api/v1/portfolio")
def get_portfolio(db: Session = Depends(get_db)):
    return db.query(Portfolio).all()
