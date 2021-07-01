class Plant:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.ratings = []

    def rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0


n = int(input())
plants = {}
for i in range(n):
    text = input().split("<->")
    plant_name, plant_rarity = text
    plants[plant_name] = Plant(plant_name, int(plant_rarity))

while True:
    command = input().split(": ")

    if command[0] == "Exhibition":
        break

    elif command[0] == "Rate":
        plant_name, rating = command[1].split(" - ")
        if plant_name in plants:
            plants[plant_name].ratings.append(int(rating))
        else:
            print("error")

    elif command[0] == "Update":
        plant_name, new_rarity = command[1].split(" - ")
        if plant_name in plants:
            plants[plant_name].rarity = int(new_rarity)
        else:
            print("error")

    elif command[0] == "Reset":
        plant_name = command[1]
        if plant_name not in plants:
            print("error")
        plants[plant_name].ratings.clear()

    else:
        print("error")

sorted_plants = sorted(plants.values(), key=lambda x: (x.rarity, x.rating()), reverse=True)
print("Plants for the exhibition:")
for plant in sorted_plants:
    print(f"- {plant.name}; Rarity: {plant.rarity}; Rating: {plant.rating():.2f}")
