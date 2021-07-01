class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        self.species = species
        res = Zoo.__animals

        if type_of_animal == "mammal":
            return f"Mammals in {zoo_name}: {', '.join(zoo_park.mammals)}\n" \
                   f"Total animals: {res}"
        elif type_of_animal == "fish":
            return f"Fishes in {zoo_name}: {', '.join(zoo_park.fishes)}\n" \
                   f"Total animals: {res}"
        elif type_of_animal == "bird":
            return f"Birds in {zoo_name}: {', '.join(zoo_park.birds)}\n" \
                   f"Total animals: {res}"

zoo_name = input()
zoo_park = Zoo(zoo_name)
n = int(input())
for i in range(1, n + 1):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo_park.add_animal(species, name)

type_of_animal = input()
print(zoo_park.get_info(type_of_animal))
