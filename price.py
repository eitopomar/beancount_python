#!/opt/homebrew/bin/python3
from datetime import datetime
import yfinance as yf
import argparse
from decimal import *

# create parser
parser = argparse.ArgumentParser()
# add an argument
parser.add_argument('filename', type=str, help='Append filename')
# parse argument
args = parser.parse_args()
items = []
result = []

# get date of today and format for beancount
now = datetime.now()
today = now.strftime("%Y-%m-%d")

# iterate throug config file
with open('price_config') as f:
    for line in f:
        # save lines to list
        items = line.split()
        # get stock info
        stock_info = yf.Ticker(items[0]).info
        # save regularMarketPrice to variable
        market_price = stock_info['regularMarketPrice']
        # print(type(market_price))
        # skip if no stock info -> type = None
        if type(market_price) is not float:
            continue
        # convert float to string
        m_price = str(market_price)
        # create entry for beancount file (convert m_price to Decimal, helps with exponential numbers)   
        price = "{0} price {3} {1} {2}".format(today, Decimal(m_price), items[1], items[2])
        # append price line to result list
        result.append(price)

# append results to file
with open(args.filename, 'a') as file_object:
    file_object.write('\n\n; automatic prices from: ' + today + '\n')
    for i in result:
        file_object.write(i + "\n")
    file_object.write('; end automatic prices\n\n')