Stock Trading Bot 
A stock trading bot built in Python using `yfinance`, `rich`, and ChatGPT integration for AI-based order validation.

Features
- Market & Limit Orders
- AI advice for limit trades
- Logging
- Rich CLI Interface

Usage

bash
python src/main.py market AAPL buy 10
python src/main.py limit AAPL sell 3 --limit_price 105.5

Requirements

pip install yfinance rich openai pandas python-dotenv


<img width="300"  alt="limit_order" src="https://github.com/user-attachments/assets/da14eeaf-161b-474f-b5ae-c07320af1cca" />


<img width="300" height="768" alt="market_order" src="https://github.com/user-attachments/assets/b8f1bdfa-8286-483f-a044-0982da397034" />


