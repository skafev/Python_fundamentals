gifts = input().split()
command = input()


while command != "No Money":
    command = command.split()

    if command[0] == "OutOfStock":
        if command[1] in gifts:
            while command[1] in gifts:
                gifts[gifts.index(command[1])] = "None"

    if command[0] == "Required":
        if 0 < int(command[2]) < len(gifts):
            del gifts[int(command[2])]
            gifts.insert(int(command[2]), command[1])

    if command[0] == "JustInCase":
        gifts.pop()
        gifts.append(command[1])
    command = input()

while "None" in gifts:
    gifts.remove("None")

print(" ".join(gifts), end=" ")