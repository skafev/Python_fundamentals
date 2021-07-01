text = input()
current_strength = 0

i = 0
while i < len(text):
    ch = text[i]

    if ch == ">":
        current_strength += int(text[i + 1])
    else:
        if current_strength > 0:
            text = text[:i] + text[i + 1:]
            current_strength -= 1
            i -= 1
    i += 1

print(text)