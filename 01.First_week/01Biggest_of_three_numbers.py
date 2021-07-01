number_one = int(input())
number_two = int(input())
number_three = int(input())
biggest = -10000000

if number_one > biggest:
    biggest = number_one
if number_two > biggest:
    biggest = number_two
if number_three > biggest:
    biggest = number_three

print(biggest)

