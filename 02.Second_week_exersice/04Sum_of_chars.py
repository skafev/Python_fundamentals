number = int(input())
total_sum = 0

while number > 0:
    n_ascii = input()
    total_sum += ord(n_ascii)
    number -= 1
print(f"The sum equals: {total_sum}")
