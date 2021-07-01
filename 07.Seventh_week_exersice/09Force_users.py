from collections import defaultdict

sides = defaultdict(list)

while True:

    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        if force_user not in sides[force_side]:
            sides[force_side].append(force_user)

    else:
        force_user, force_side = command.split(" -> ")
        for k, v in sides.items():
            if force_user in v:
                sides[k].remove(force_user)

        if force_user not in force_side:
            sides[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

for key, value in sorted(sides.items(), key=lambda x: (-len(x[1]), (x[0]))):
    if len(value) != 0:
        print(f"Side: {key}, Members: {len(value)}")
        for i in sorted(value):
            print(f"! {i}")