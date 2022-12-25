# def discounter(price, discount: float = 0.12):
#     return str(float(price) / discount)
def discount(price, discount: float = 3.00) -> str:
    if price > 25.00:
        return f'{price - discount}'


