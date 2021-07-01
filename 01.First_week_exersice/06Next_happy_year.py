number = int(input())

while True:
    number += 1
    year = str(number)
    year_to_set = set(year)
    if len(year) == len(year_to_set):
        print(year)
        break