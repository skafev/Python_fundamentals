numbers = input().split(", ")
numbers.sort(key="0".__eq__)
my_list = []
for number in numbers:
    my_list.append(int(number))
print(my_list)