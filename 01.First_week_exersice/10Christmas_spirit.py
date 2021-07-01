quantity = int(input())
days = int(input())

ornament_set = 0
tree_skirt = 0
tree_garlands = 0
tree_lights = 0

christmas_spirit = 0

for day in range(1, days + 1):

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        ornament_set += quantity * 2
        christmas_spirit += 5

    if day % 3 == 0:
        tree_skirt += quantity * 5
        tree_garlands += quantity * 3
        christmas_spirit += 13

    if day % 5 == 0:
        tree_lights += quantity * 15
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        tree_skirt += 5
        tree_garlands += 3
        tree_lights += 15

if days % 10 == 0:
    christmas_spirit -= 30

total_cost = ornament_set + tree_skirt + tree_garlands + tree_lights
print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
