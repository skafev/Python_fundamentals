import re

text = input()


pattern = re.compile(r'( |^)[A-Za-z0-9]+((\.|\-|\_)[A-Za-z0-9]+)'
                     r'*@([A-Za-z0-9])+(-[A-Za-z0-9]+)*\.[A-Za-z0-9]+((\.|\-|\_)[A-Za-z0-9]+)*')

matches = re.finditer(pattern, text)

for match in matches:
    print(match[0])
