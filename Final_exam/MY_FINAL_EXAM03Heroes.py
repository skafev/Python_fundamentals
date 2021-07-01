heroes = {}

while True:
    command = input().split()
    if command[0] == "End":
        break

    hero_name = command[1]

    if command[0] == "Enroll":
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []

    elif command[0] == "Learn":
        spell_name = command[2]

        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
            continue

        if spell_name not in heroes[hero_name]:
            heroes[hero_name].append(spell_name)
        else:
            print(f"{hero_name} has already learnt {spell_name}.")

    elif command[0] == "Unlearn":
        spell_name = command[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
            continue

        if spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)

heroes = sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0]))

print("Heroes:")
for k, v in heroes:
    print(f"== {k}: {', '.join(v)}")
