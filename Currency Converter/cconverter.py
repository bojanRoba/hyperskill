import requests

# 01. Take the first input – the currency that you have. It is default for all the calculations.
currency = input().lower()

# 02. Retrieve the data from FloatRates as before.
currency_url = f"http://www.floatrates.com/daily/{currency}.json"
currency_data = requests.get(currency_url).json()

# 03. Save the exchange rates for USD and EUR (these are the most popular ones, so it's good to have rates for them in advance).
currency_rate = {}

if 'usd' in currency_data:
    currency_rate['usd'] = currency_data['usd']['rate']

if 'eur' in currency_data:
    currency_rate['eur'] = currency_data['eur']['rate']

# 04. Take the second input – the currency code that you want to exchange money for, and the third input – amount of money you have.
while True:
    second_currency = input().lower()
    if len(second_currency) == 0:
        break
    else:
        amount_money = float(input())

        # 05. Check the cache. Maybe you already have what you need?
        print("Checking the cache...")

        # 06. If you have the currency in your cache, calculate the result.
        if second_currency in currency_rate:
            print("Oh! It is in the cache!")

        else:
            print("Sorry, but it is not in the cache!")
            # 07. If not, get it from the site, and calculate the result.
            # second_currency_url = f"http://www.floatrates.com/daily/{second_currency}.json"
            # second_currency_data = requests.get(currency_url).json()
            currency_rate[second_currency] = currency_data[second_currency]['rate']

    # 08. Save the rate to your cache.
        conversion = round(currency_rate[second_currency] * amount_money, 2)

    # 09. Print the result.
        print(f"You received {conversion} {second_currency.upper()}.")

    # 10.Repeat steps 4-9 until there is no currency left to process.
