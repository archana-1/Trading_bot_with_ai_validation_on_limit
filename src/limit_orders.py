from rich.console import Console
from data_handler import fetch_stock_data
from utils import setup_logger
from openai import OpenAI
from dotenv import load_dotenv
import os


#load env
load_dotenv()

logger = setup_logger()
console = Console()

# You must export your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")


def ai_order_check(ticker, limit_price, side):
    """Use ChatGPT to validate the trade idea."""
    prompt = f"""
    You are a trading assistant. The user wants to place a {side.upper()} limit order
    for {ticker} at {limit_price}. Based on general stock trading principles,
    respond whether this order seems reasonable and provide a one-sentence justification.
    """
    client = OpenAI(api_key = api_key)
    response =client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )

    return response.choices[0].message.content
    # return prompt

def place_limit_order(ticker: str, quantity: int, side: str, limit_price: float):
    data = fetch_stock_data(ticker)
    # fix the ticker level to access data like data['close']
    data = data.xs(ticker, axis= 1, level= "Ticker")
    current_price = data['Close'].iloc[-1]

    ai_feedback = ai_order_check(ticker, limit_price, side)
    logger.info(f"AI Feedback: {ai_feedback}")

    console.print(f"[cyan]AI Suggestion:[/cyan] {ai_feedback}")

    if (side == 'buy' and limit_price >= current_price) or (side == 'sell' and limit_price <= current_price):
        console.print(f"[bold yellow]Limit order triggered immediately at market price![/bold yellow]")
        executed_price = current_price
    else:
        executed_price = limit_price
        console.print(f"[bold green]Limit order placed[/bold green] for {ticker} at ${limit_price:.2f}")

    logger.info(f"Limit Order | {side.upper()} | {quantity} {ticker} @ {executed_price:.2f}")
    return {"ticker": ticker, "side": side, "price": executed_price, "quantity": quantity}
