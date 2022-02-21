# Python scripts for beancount

I couldn't get the beancount price fetcher to work. So I wrote this script to fetch prices from yahoo finance with the easy to use yfinance.

## price.py

Fetch market prices from yahoo finance. Edit price_config file to your liking.

price_config:
| Symbol/ISIN used to search yahoo | currency used in beancount-file | units used in beancount-file |
| - | - | - |
| BTC-USD | USD | BTC |

Usage:
`python3 price.py NAME_OF_BEANCOUNT_FILE`
