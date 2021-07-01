line = input().split()
products_to_search = input().split()
bakery = {}

for i in range(0, len(line), 2):
    if i % 2 == 0 or i == 0:
        product = line[i]
        quantity = line[i + 1]
        bakery[product] = int(quantity)

for p in products_to_search:
    if bakery.get(p):
        print(f"We have {bakery[p]} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")