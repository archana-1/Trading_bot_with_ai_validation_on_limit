import argparse
from rich.console import Console
from market_orders import execute_market_order
from limit_orders import place_limit_order

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Rich CLI Stock Trading Bot")
    parser.add_argument("type", choices=["market", "limit"], help="Order type")
    parser.add_argument("ticker", help="Stock symbol (e.g., AAPL)")
    parser.add_argument("side", choices=["buy", "sell"], help="Order side")
    parser.add_argument("quantity", type=int, help="Order quantity")
    parser.add_argument("--limit_price", type=float, help="Limit price (for limit orders)")
    args = parser.parse_args()

    if args.type == "market":
        execute_market_order(args.ticker, args.quantity, args.side)
    elif args.type == "limit":
        if not args.limit_price:
            console.print("[red]Error: --limit_price is required for limit orders.[/red]")
            return
        place_limit_order(args.ticker, args.quantity, args.side, args.limit_price)

if __name__ == "__main__":
    main()
