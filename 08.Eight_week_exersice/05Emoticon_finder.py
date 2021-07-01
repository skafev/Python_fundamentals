text = input()

for a, b in zip(text, text[1:]):
    if a == ":":
        print(a + b)
