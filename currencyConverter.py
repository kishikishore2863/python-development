class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            print("Invalid currency")
            return None
        else:
            conversion_rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
            converted_amount = amount * conversion_rate
            return converted_amount


# Sample exchange rates (as of the current knowledge cutoff date)
exchange_rates = {
    'USD': 1.0,  # Base currency
    'EUR': 0.85,  # Exchange rate for 1 USD to EUR
    'GBP': 0.73,  # Exchange rate for 1 USD to GBP
}

# Create a CurrencyConverter instance
converter = CurrencyConverter(exchange_rates)

# Get user input for conversion
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()

# Perform the conversion and display the result
converted_amount = converter.convert(amount, from_currency, to_currency)

if converted_amount is not None:
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")



