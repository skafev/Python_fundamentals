import re

while True:
    text = input()

    if text == "":
        break

    pattern = re.compile(r'([w]{3}\.[A-Za-z0-9\-]+\.[a-z]+(\.[a-z]+)*)')
    matches = re.finditer(pattern, text)

    for match in matches:
        print(match.group(0))
