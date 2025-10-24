from rich.console import Console
from data_handler import fetch_stock_data
from utils import setup_logger

logger = setup_logger()
console = Console()

def execute_market_order(ticker: str, quantity: int, side: str):
    """
    Execute a simulated market order at the latest price.
    """
    data = fetch_stock_data(ticker)
    # fix the ticker level to access data like data['close']
    data = data.xs(ticker, axis= 1, level= "Ticker")
    price = data['Close'].iloc[-1]
    cost = quantity * price

    logger.info(f"Market Order | {side.upper()} | {quantity} {ticker} @ {price:.2f}")
    console.print(f"[bold green]Market {side.upper()} Order Executed[/bold green] for {quantity} {ticker} @ ${price:.2f}")
    return {"ticker": ticker, "side": side, "price": price, "quantity": quantity, "total": cost}
