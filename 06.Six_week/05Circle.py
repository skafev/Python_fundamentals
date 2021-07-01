class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter /2

    def calculate_circumference(self):
        res = self.__pi * self.diameter
        return res

    def calculate_area(self):
        res = (self.calculate_circumference() ** 2) / (4 * self.__pi)
        return res

    def calculate_area_of_sector(self, angle):
        self.angle = angle
        return (angle/360) * self.__pi * self.radius * self.radius

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")