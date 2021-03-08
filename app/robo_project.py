# app/robo_advisor.py file 
#Inspired by Prof. Rossetti's screencast

import csv
import json 
import os

from datetime import datetime 
from dotenv import load_dotenv 
import requests

load_dotenv()

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

# Formatting prices to USD dollars 
def to_usd(my_price):
    return"${0:,.2f}".format(my_price)

# Compiling request URLs
url_lookup = ""
def compile_url(ticker_input):
    url_lookup = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker_input}&apikey={api_key}"
    return url_lookup

#Issuing API Requests 
def get_response(ticker):
    this_url = compile_url(ticker)
    response = requests.get(this_url)
    parsed_response = json.loads(response.text)
    return parsed_response

# INFO OUTPUTS
#



symbol = "IBM" # accept user input 

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

# breakpoint()


csv_file_path = os.path.join(os.path.dirname(__file__),"..","data","prices.csv")

csv_headers = ["timestamp", "open", "high", "low","close", "volume"]

with open(csv_file_path,"w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")