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

# Issuing API Requests 
def get_response(ticker):
    this_url = compile_url(ticker)
    response = requests.get(this_url)
    parsed_response = json.loads(response.text)
    return parsed_response

# Processing API Responses 
def transform_response(parsed_response):
    tsd = parsed_response["Time Series (Daily)"]
    rows = []

    for date, daily_prices in tsd.items():
        row = {
            "timestamp" : date,
            "open": float(daily_prices["1. open"]),
            "high": float(daily_prices["2. high"]),
            "low": float(daily_prices["3. low"]),
            "close": float(daily_prices["4. close"]),
            "volume": int(daily_prices["5. volume"])
        }
        rows.append(row)
    return rows

# Writing to CSV
def write_to_csv(rows, csv_file_path):
    csv_headers = ["timestamp", "open", "high", "low", "close", "volume" ]
    with open(csv_file_path, "w") as csv_file: 
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return True

if __name__ == "__main__":
    #Validations(Prelim)
    while True:
        ticker_symbol = input("Please enter a valid ticker symbol of the stock you wish to evaluate (e.g. IBM): ")
        if not ticker_symbol.isalpha() and len(ticker_symbol) <= 5:
            print("That doesn't seem a valid stock symbol. Please check the formatting and try again. ")
        else:
            get_response(ticker_symbol)
        if "error" in get_response(ticker_symbol):
            print("Oh no! I couldn't find any trading data for that stock symbol.Please restart the program and try another one if you'd like.")
        else:
            break
    while True:
        acceptable_risk = input("How much risk are you willing to accept? Please enter a number between 1 and 10, with 1 being very low risk and 10 being very high risk. ")
        if 1<= float(acceptable_risk) <= 10 :
            break 
        else:
            print("Sorry, that level of risk is not a valid! Please try again.") 

#
# Information Output 
#

#Latest day & Latest Close 
parsed_response = get_response(ticker_symbol)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
row = transform_response(parsed_response)
latest_close = row[0]["close"]

# 
#
#


symbol = "IBM" # accept user input 

dates = list(tsd.keys())

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


print("-------------------------")
print("Stock: XYZ")
print("-------------------------")
print("Fetching stock market Data...")
print("Requested at: 2018-02-20 02:00pm")
print("-------------------------")
print(f"Latest Data from: {last_refreshed}")
print(f"Latest closing price: {to_usd(float(latest_close))}")
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