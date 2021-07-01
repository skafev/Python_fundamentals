import re

lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)

text = '\n'.join(lines)

pattern = re.compile(r'(\d+)')

matches = re.findall(pattern, text)

print(' '.join(matches), end="")
