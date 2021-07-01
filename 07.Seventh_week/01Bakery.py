line = input().split()
bakery = {}
for i in range(0, len(line)):
    if i % 2 == 0 or i == 0:
        product = line[i]
        quantity = line[i + 1]
        bakery[product] = int(quantity)

print(bakery)