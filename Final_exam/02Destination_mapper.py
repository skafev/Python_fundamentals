import re
res = []
length = 0

text = input()
pattern = re.compile(r'(=|\/)([A-Z][A-Za-z]{2,})\1')
matches = re.finditer(pattern, text)

for match in matches:
    res.append(match[2])
    length += len(match[2])

print(f"Destinations: {', '.join(res)}")
print(f"Travel Points: {length}")
