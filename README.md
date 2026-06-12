# binancefuturetestnet

Binance Futures Testnet Trading Bot

Overview

This project is a Python CLI application that places BUY and SELL orders on Binance Futures Testnet (USDT-M). The application supports both Market and Limit orders, validates user inputs, logs order activity, and handles errors gracefully.

Features

- Place Market Orders
- Place Limit Orders
- BUY and SELL support
- Command Line Interface (CLI)
- Input Validation
- Logging of requests and responses
- Exception Handling

Requirements

- Python 3.x
- Binance Futures Testnet Account
- API Key and Secret Key

Installation

1. Clone the repository:

git clone <repository-link>
cd binance-futures-bot

2. Install dependencies:

pip install -r requirements.txt

3. Create a .env file in the project root:

API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key

Running the Application

Market Order

python app.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

Limit Order

python app.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 120000

Example Output

Order Request:

- Symbol: BTCUSDT
- Side: BUY
- Order Type: MARKET
- Quantity: 0.001

Order Response:

- Order ID
- Status
- Executed Quantity

Logging

All API requests, responses, and errors are stored in the log file located inside the logs directory.

Example:

2026-06-12 22:30:15 INFO Request: Symbol=BTCUSDT Side=BUY Type=MARKET
2026-06-12 22:30:16 INFO Response: OrderID=123456789 Status=FILLED

Assumptions

- Valid Binance Futures Testnet API credentials are provided.
- Sufficient test funds are available in the account.
- The application is intended for Binance Futures Testnet only.
- Only Market and Limit orders are implemented.

Project Structure

binance-futures-bot/

- main.py
- requirements.txt
- README.md
- .env.example
- .gitignore
- orders.log

Author

Saizal Kumawat
