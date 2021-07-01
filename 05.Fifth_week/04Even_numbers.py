numbers = input().split(", ")
even = []
index = 0

for num in numbers:

    if int(num) % 2 == 0:
        even.append(index)
    index += 1

print(even)