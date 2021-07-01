def orders(product, quantity):
    price = None
    if product == "coffee":
        price = 1.5
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2

    if price is not None:
        return price * quantity




product = input()
quantity = int(input())
print(f"{orders(product,quantity):.2f}")