import re

name = input()
pattern = re.compile(r'(\b[A-Z][a-z]+ [A-Z][a-z]+)\b')
match = re.findall(pattern, name)

print(" ".join(match))