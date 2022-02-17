# Python scripts for beancount

I'm a beginner. I have no idea of what I'm doing. It works for me. It may work for you. I don't take any responsibility.

## price.py

Fetch market prices from yahoo finance. Edit price_config file to your liking.

price_config:
| Symbol used to search yahoo | currency used in beancount-file | units used in beancount-file |
| - | - | - |
| BTC-USD | USD | BTC |

Usage:
`python3 price.py NAME_OF_BEANCOUNT_FILE`
