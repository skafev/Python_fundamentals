number_of_cars = int(input())
vehicles = {}

for n in range(number_of_cars):
    text = input().split("|")
    car_name, current_mileage, current_fuel = text
    vehicles[car_name] = {}
    vehicles[car_name]["mileage"] = int(current_mileage)
    vehicles[car_name]["fuel"] = int(current_fuel)
while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    car = command[1]

    if command[0] == "Drive":
        distance = command[2]
        fuel = command[3]
        if vehicles[car]["fuel"] < int(fuel):
            print("Not enough fuel to make that ride")
        else:
            vehicles[car]["mileage"] += int(distance)
            vehicles[car]["fuel"] -= int(fuel)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if vehicles[car]["mileage"] >= 100000:
            del vehicles[car]
            print(f"Time to sell the {car}!")

    elif command[0] == "Refuel":
        fuel = command[2]
        standard_tank = 75
        old_fuel = vehicles[car]["fuel"]
        vehicles[car]["fuel"] += int(fuel)
        if vehicles[car]["fuel"] >= standard_tank:
            added_fuel = standard_tank - old_fuel
            vehicles[car]["fuel"] = standard_tank
            print(f"{car} refueled with {added_fuel} liters")
        else:
            print(f"{car} refueled with {fuel} liters")

    elif command[0] == "Revert":
        kilometers = command[2]
        if vehicles[car]["mileage"] >= 10000:
            vehicles[car]["mileage"] -= int(kilometers)
            if vehicles[car]["mileage"] < 10000:
                vehicles[car]["mileage"] = 10000
                continue
        print(f"{car} mileage decreased by {kilometers} kilometers")
        if vehicles[car]["mileage"] < 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")

sorted_vehicles = sorted(vehicles.keys(), key=lambda x: (-vehicles[x]["mileage"], x))
for k in sorted_vehicles:
    print(f"{k} -> Mileage: {vehicles[k]['mileage']} kms, Fuel in the tank: {vehicles[k]['fuel']} lt.")
