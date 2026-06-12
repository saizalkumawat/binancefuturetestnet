from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=  os.getenv("API_KEY")
API_SECRET= os.getenv("API_SECRET")


# Client create
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# User Input
symbol = input("Enter Symbol (BTCUSDT): ").upper()
side = input("Enter Side (BUY/SELL): ").upper()
order_type = input("Enter Order Type (MARKET/LIMIT): ").upper()
quantity = float(input("Enter Quantity: "))

try:
    if order_type == "MARKET":

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    elif order_type == "LIMIT":

        price = input("Enter Price: ")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

    else:
        print("Invalid Order Type")
        exit()

    print("\nOrder Placed Successfully!")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])

except Exception as e:
    print("Error:", e)

