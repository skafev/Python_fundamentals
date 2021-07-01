import re

year = input()
pattern = re.compile(r'(\d{2})([/\.-])([A-z][a-z]+)\2(\d{4})')

matches = re.findall(pattern, year)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")