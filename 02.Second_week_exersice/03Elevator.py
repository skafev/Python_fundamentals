number_of_people = int(input())
capacity = int(input())
courses = 0

while capacity > 0:
    number_of_people -= capacity
    courses += 1
    if number_of_people <= 0:
        break
print(courses)