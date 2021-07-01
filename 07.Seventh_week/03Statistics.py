in_stock = {}
while True:
    command = input()
    if command == "statistics":
        break
    command = command.split()
    key = command[0]
    value = int(command[1])
    if in_stock.get(key):
        in_stock[key] += value
    else:
        in_stock[key] = value
sum_all_quantities = 0
count_all_products = 0
print(f"Products in stock:")
for k, v in in_stock.items():
    print(f"- {k} {v}")
    count_all_products += 1
    sum_all_quantities += v


print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")
