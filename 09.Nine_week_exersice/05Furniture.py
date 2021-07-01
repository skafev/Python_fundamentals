import re
furniture_total = ""
total = 0
while True:
    text = input()

    if text == "Purchase":
        break

    pattern = re.compile(r'(>>\w+<<)([0-9]+\.?[0-9]+?)!([0-9]+)')
    matches = re.finditer(pattern, text)

    for match in matches:
        furniture = match.group(1)
        price = match.group(2)
        quantity = match.group(3)
        total += int(quantity) * float(price)
        furniture_total += furniture

pattern_two = re.compile(r'([A-Za-z]+)')
matches_two = re.findall(pattern_two, furniture_total)
print(f"Bought furniture:")
for m in matches_two:
    print(m)
print(f'Total money spend: {total:.2f}')
