from collections import defaultdict

bar_price = defaultdict(int)
bar_quantity = defaultdict(int)
final_bar = defaultdict(int)

while True:
    command = input()
    if command == "buy":
        break

    product, price, quantity = command.split()
    bar_price[product] = float(price)
    bar_quantity[product] += int(quantity)

for product in bar_price:
    if product in bar_quantity:
        final_bar[product] = bar_price.get(product) * bar_quantity.get(product)


for k, v in final_bar.items():
    print(f"{k} -> {v:.2f}")