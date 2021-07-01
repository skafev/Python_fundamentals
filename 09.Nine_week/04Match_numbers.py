import re

numbers = input()
pattern = re.compile(r'(^|(?<=\s))(-*)(\d+)((\.\d+)*)($|(?=\s))')

matches = re.finditer(pattern, numbers)

for match in matches:
    print(match.group(0), end=" ")
