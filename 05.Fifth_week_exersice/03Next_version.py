text = input()

number = []
for num in text.split("."):
    number.append(int(num))
number[2] += 1

if number[2] == 10:
    number[2] = 0
    number[1] += 1

if number[1] == 10:
    number[1] = 0
    number[0] += 1

res = ".".join([str(x) for x in number])
print(res)