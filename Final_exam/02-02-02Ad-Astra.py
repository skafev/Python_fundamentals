import re

nutrition = 0
daily_calories = 2000

text = input()
pattern = re.compile(r"(\||#)([A-Za-z]+\s?[A-Za-z]+)\1"
                     r"((3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/([0-9]{2}))\1"
                     r"(\d{1,5})\1")
matches = re.findall(pattern, text)
foods = []
for match in matches:
    food = match[1]
    expiration_date = match[2]
    calories = match[6]
    foods.append(food)
    foods.append(expiration_date)
    foods.append(int(calories))
    nutrition += int(calories)

days = nutrition // daily_calories
print(f"You have food to last you for: {days} days!")
for i in range(0, len(foods), 3):
    print(f"Item: {foods[i]}, Best before: {foods[i + 1]}, Nutrition: {foods[i + 2]}")
