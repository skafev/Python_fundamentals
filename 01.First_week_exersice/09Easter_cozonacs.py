budget = float(input())
flour = float(input())

pack_of_eggs = flour * 0.75
milk = (flour + (flour * 0.25)) / 4
one_cozonac = pack_of_eggs + flour + milk
cozonac_count = 0
money_left = 0
colored_eggs = 0
while budget > one_cozonac:
    budget -= one_cozonac
    cozonac_count += 1
    colored_eggs += 3

    if cozonac_count % 3 == 0:
        colored_eggs -= cozonac_count - 2

print(f"You made {cozonac_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")



