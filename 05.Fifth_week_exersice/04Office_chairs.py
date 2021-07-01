rooms = int(input())
free_chair = 0
have_chairs = True

for room in range(1, rooms + 1):
    chairs = input().split(" ")
    chairs_in_room = len((chairs[0]))
    people = int(chairs[1])

    if chairs_in_room >= people:
        free_chair += chairs_in_room - people
    else:
        have_chairs = False
        print(f"{people - chairs_in_room} more chairs needed in room {room}")

if have_chairs:
    print(f"Game On, {free_chair} free chairs left")
