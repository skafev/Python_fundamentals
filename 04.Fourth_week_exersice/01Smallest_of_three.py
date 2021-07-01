def smallest_number(a, b, c):
    smallest = 10000
    if a < smallest:
        smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    return smallest


a = int(input())
b = int(input())
c = int(input())
print(smallest_number(a, b, c))