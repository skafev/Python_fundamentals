number = int(input())
index = 1
res = []

while number > 0:
    formula = 2 * index ** 2

    if number < formula:
        res.append(number)
    else:
        res.append(formula)

    number -= formula
    index += 1

print(res)
