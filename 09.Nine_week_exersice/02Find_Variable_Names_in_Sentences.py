import re

text = input()
pattern = re.compile(r'(\b_)([A-Za-z0-9]+)\b')

matches = re.findall(pattern, text)
res = []
for match in matches:
    _, variable = match
    res.append(variable)
print(','.join(res))
