from currency_converter import CurrencyConverter

async def currencies() -> dict:
    c = CurrencyConverter()
    return c.currencies


class Convertation:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        self.c = CurrencyConverter()
    
    def __call__(self):
        return self.c.convert(self.amount, self.currency)


e = Convertation('EUR', 1)
print(e())