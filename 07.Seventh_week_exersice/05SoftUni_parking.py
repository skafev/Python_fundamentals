num = int(input())
registered_cards = {}
for n in range(1, num + 1):
    command = input().split()
    reg = command[0]

    if reg == "register":
        name = command[1]
        plate = command[2]
        if not name in registered_cards:
            registered_cards[name] = plate
            print(f"{name} registered {registered_cards[name]} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_cards[name]}")

    elif reg == "unregister":
        name = command[1]
        if not name in registered_cards:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del registered_cards[name]

for k, v in registered_cards.items():
    print(f"{k} => {v}")