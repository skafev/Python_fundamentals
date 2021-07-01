tour = input()

while True:
    text = input().split(":")

    if text[0] == "Travel":
        break

    command = text[0]

    if command == "Add Stop":
        index = int(text[1])
        city = text[2]
        if len(tour) >= index:
            tour = tour[:index] + city + tour[index:]
        print(tour)

    elif command == "Remove Stop":
        start_index = int(text[1])
        stop_index = int(text[2])
        if start_index < len(tour) and stop_index < len(tour):
            tour = tour[0:start_index:] + tour[stop_index + 1::]
        print(tour)

    elif command == "Switch":
        old_string = text[1]
        new_string = text[2]
        if old_string in tour:
            tour = tour.replace(old_string, new_string)
            print(tour)

print(f"Ready for world tour! Planned stops: {tour}")