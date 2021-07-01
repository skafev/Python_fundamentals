import re

phone_number = input()
pattern = re.compile(r'(\+359-2-\d{3}-\d{4}|\+359 2 \d{3} \d{4})\b')

matches = re.findall(pattern, phone_number)
print(", ".join(matches))