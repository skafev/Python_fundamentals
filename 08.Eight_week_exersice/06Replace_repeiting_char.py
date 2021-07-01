text = input()
previous = ""

for a in text:
    if a != previous:
        print(a, end="")
    previous = a
