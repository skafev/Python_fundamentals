text = input().split()
numbers_to_remove = int(input())
numbers = []
the_biggest = 100000
for n in text:
    numbers.append(int(n))

for i in range(numbers_to_remove):

    for number in numbers:

        if number < the_biggest:
            the_biggest = number

    numbers.remove(the_biggest)
    the_biggest = 100000

print(numbers)