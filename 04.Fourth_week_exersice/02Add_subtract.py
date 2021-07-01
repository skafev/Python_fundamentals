def sum_numbers(a, b):
    return a + b


def subtract(a, b, c):
    return (a + b) - c


def add_and_subtract(a, b, c):
    return subtract(a, b, c)


a = int(input())
b = int(input())
c = int(input())
print(add_and_subtract(a, b, c))