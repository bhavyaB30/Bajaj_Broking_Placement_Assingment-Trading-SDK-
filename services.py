import uuid
from storage import orders, trades, portfolio, instruments


def place_order(order_request):
    """
    Validates and places a new order.
    MARKET orders are executed immediately.
    LIMIT orders are kept in PLACED state.
    """

    # Basic validations
    if order_request.quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if order_request.type == "LIMIT" and order_request.price is None:
        raise ValueError("Price is mandatory for LIMIT orders")

    order_id = str(uuid.uuid4())

    # Determine initial order status
    if order_request.type == "MARKET":
        status = "EXECUTED"
    else:
        status = "PLACED"

    orders[order_id] = {
        "orderId": order_id,
        "status": status,
        "request": order_request
    }

    # Execute trade immediately for MARKET orders
    if status == "EXECUTED":
        execute_trade(order_id, order_request)

    return orders[order_id]


def execute_trade(order_id, order_request):
    """
    Creates a trade for an executed order
    and updates the portfolio.
    """

    # Determine execution price
    if order_request.type == "MARKET":
        price = next(
            inst["lastTradedPrice"]
            for inst in instruments
            if inst["symbol"] == order_request.symbol
        )
    else:
        price = order_request.price

    trade = {
        "tradeId": str(uuid.uuid4()),
        "orderId": order_id,
        "symbol": order_request.symbol,
        "quantity": order_request.quantity,
        "price": price
    }

    trades.append(trade)
    update_portfolio(trade, order_request.side)


def update_portfolio(trade, side):
    """
    Updates portfolio holdings after trade execution.
    """

    symbol = trade["symbol"]
    quantity = trade["quantity"]
    trade_value = trade["price"] * quantity

    holding = portfolio.get(symbol, {
        "quantity": 0,
        "averagePrice": 0.0
    })

    if side == "BUY":
        total_value = holding["quantity"] * holding["averagePrice"] + trade_value
        total_quantity = holding["quantity"] + quantity

        holding["averagePrice"] = total_value / total_quantity
        holding["quantity"] = total_quantity

    elif side == "SELL":
        holding["quantity"] -= quantity

    portfolio[symbol] = holding
