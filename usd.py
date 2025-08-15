# Exchange to USD


rates_to_usd = {
    "MMK": 0.00048,   # Myanmar Kyat
    "EUR": 1.09,      # Euro
    "JPY": 0.0069,    # Japanese Yen
    "GBP": 1.27       # British Pound
}

currency = input('Which currency would you like to exchange to USD? ').upper()

if currency in rates_to_usd:

    amount = float(
        input(f'How much {currency} would you like to exwchange to USD?'))
    usd = amount * rates_to_usd[currency]
    print(f'{amount} {currency} = {round(usd, 2)} USD')
else:
    print("❌ Sorry, this currency is not supported.")
