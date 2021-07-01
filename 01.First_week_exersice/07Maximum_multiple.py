divisor = int(input())
bound = int(input())
largest = 0

for i in range(divisor, bound + 1):
    if i % divisor == 0:
        largest = i
print(largest)