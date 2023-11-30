# Install the forex-python library using: pip install forex-python
from forex_python.converter import CurrencyRates
import sys

def get_exchange_rate(from_currency, to_currency):
    currency_rates = CurrencyRates()
    exchange_rate = currency_rates.get_rate(from_currency, to_currency)
    return exchange_rate

def convert_currency(from_currency, to_currency, amount):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    if len(sys.argv) != 4:
        print("Usage: python exchange_rate_calculator.py <from_currency> <to_currency> <amount>")
        sys.exit(1)

    from_currency = sys.argv[1].upper()
    to_currency = sys.argv[2].upper()

    try:
        amount = float(sys.argv[3])
    except ValueError:
        print("Error: Invalid amount. Please enter a numeric value.")
        sys.exit(1)

    exchange_rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = convert_currency(from_currency, to_currency, amount)

    print(f"Exchange Rate ({from_currency} to {to_currency}): {exchange_rate}")
    print(f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
