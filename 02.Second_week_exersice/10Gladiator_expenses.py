fights_lost_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_brake = 0
total_cost = 0

for n in range(1, fights_lost_count + 1):

    if n % 2 == 0:
        total_cost += helmet_price

    if n % 3 == 0:
        total_cost += sword_price

        if n % 2 == 0:
            total_cost += shield_price
            shield_brake += 1

            if shield_brake % 2 == 0:
                total_cost += armor_price

print(f"Gladiator expenses: {total_cost:.2f} aureus")