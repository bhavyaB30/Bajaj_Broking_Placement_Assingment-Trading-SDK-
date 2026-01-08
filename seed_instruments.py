from database import SessionLocal
from models import Instrument

db = SessionLocal()

instruments = [
    # IT
    ("TCS", "NSE", "EQUITY", 3850.5),
    ("INFY", "NSE", "EQUITY", 1600.0),
    ("WIPRO", "NSE", "EQUITY", 485.0),
    ("HCLTECH", "NSE", "EQUITY", 1450.0),
    ("TECHM", "NSE", "EQUITY", 1320.0),

    # Banking
    ("HDFCBANK", "NSE", "EQUITY", 1550.0),
    ("ICICIBANK", "NSE", "EQUITY", 1020.0),
    ("SBIN", "NSE", "EQUITY", 640.0),
    ("AXISBANK", "NSE", "EQUITY", 1120.0),
    ("KOTAKBANK", "NSE", "EQUITY", 1750.0),

    # FMCG
    ("HINDUNILVR", "NSE", "EQUITY", 2450.0),
    ("ITC", "NSE", "EQUITY", 460.0),
    ("NESTLEIND", "NSE", "EQUITY", 25500.0),
    ("DABUR", "NSE", "EQUITY", 540.0),
    ("BRITANNIA", "NSE", "EQUITY", 5050.0),

    # Energy
    ("RELIANCE", "NSE", "EQUITY", 2850.0),
    ("ONGC", "NSE", "EQUITY", 245.0),
    ("BPCL", "NSE", "EQUITY", 465.0),
    ("IOC", "NSE", "EQUITY", 165.0),
    ("POWERGRID", "NSE", "EQUITY", 295.0),

    # Auto
    ("TATAMOTORS", "NSE", "EQUITY", 980.0),
    ("MARUTI", "NSE", "EQUITY", 11200.0),
    ("M&M", "NSE", "EQUITY", 1780.0),
    ("BAJAJ-AUTO", "NSE", "EQUITY", 8650.0),
    ("EICHERMOT", "NSE", "EQUITY", 3950.0),

    # Pharma
    ("SUNPHARMA", "NSE", "EQUITY", 1320.0),
    ("DRREDDY", "NSE", "EQUITY", 5650.0),
    ("CIPLA", "NSE", "EQUITY", 1240.0),
    ("DIVISLAB", "NSE", "EQUITY", 3950.0),
    ("LUPIN", "NSE", "EQUITY", 1450.0),

    # Metals
    ("TATASTEEL", "NSE", "EQUITY", 145.0),
    ("JSWSTEEL", "NSE", "EQUITY", 890.0),
    ("HINDALCO", "NSE", "EQUITY", 620.0),
    ("COALINDIA", "NSE", "EQUITY", 450.0),
    ("VEDL", "NSE", "EQUITY", 285.0),

    # Others
    ("LT", "NSE", "EQUITY", 3650.0),
    ("ULTRACEMCO", "NSE", "EQUITY", 9950.0),
    ("ADANIENT", "NSE", "EQUITY", 3150.0),
    ("ADANIPORTS", "NSE", "EQUITY", 1180.0),
    ("DMART", "NSE", "EQUITY", 3950.0),
    ("IRCTC", "NSE", "EQUITY", 930.0),
]

for symbol, exchange, inst_type, price in instruments:
    if not db.query(Instrument).filter(Instrument.symbol == symbol).first():
        db.add(Instrument(
            symbol=symbol,
            exchange=exchange,
            instrument_type=inst_type,
            last_traded_price=price
        ))

db.commit()
db.close()
print("50+ instruments inserted successfully")
