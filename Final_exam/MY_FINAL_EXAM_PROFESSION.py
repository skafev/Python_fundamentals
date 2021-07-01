import re

number = int(input())
for n in range(number):
    text = input()
    pattern = re.compile(r"\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#")
    matches = re.findall(pattern, text)

    for match in matches:
        name = match[0]
        profession = match[1]
        print(f"{name}, The {profession}")
        print(f">> Strength: {len(name)}")
        print(f">> Armour: {len(profession)}")

    if not matches:
        print("Access denied!")
