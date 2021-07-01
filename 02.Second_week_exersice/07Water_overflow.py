number = int(input())
capacity = 255
in_tank = 0

for n in range(1, number + 1):
    water_in_tank = int(input())
    if water_in_tank > capacity:
        print("Insufficient capacity!")
        continue
    capacity -= water_in_tank
    in_tank += water_in_tank
print(in_tank)