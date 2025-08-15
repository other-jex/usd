# Exchange to USD


rates_to_usd = {
    "MMK": 0.00048,   # Myanmar Kyat
    "EUR": 1.09,      # Euro
    "JPY": 0.0069,    # Japanese Yen
    "GBP": 1.27       # British Pound
}

# Loop until the user enters a valid currency
while True:
    currency = input(
        'Which currency would you like to exchange to USD? ').upper()
    if currency in rates_to_usd:
        break  # exit the loop if the currency is valid
    else:
        print("❌ Sorry, this currency is not supported. Try again.")

# Now ask for the amount
amount = float(
    input(f'How much {currency} would you like to exchange to USD? '))
usd = amount * rates_to_usd[currency]
print(f'{amount} {currency} = {round(usd, 2)} USD')
