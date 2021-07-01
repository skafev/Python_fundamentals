import sys


def exchange(my_list, intcommand):
    my_list = my_list[intcommand + 1:] + my_list[:1 + intcommand]

    return my_list


def max_even_index(my_list):
    max_num = -sys.maxsize
    index = -1

    for i in range(len(my_list)):
        num = my_list[i]
        if num >= max_num and num % 2 == 0:
            max_num = num
            index = i

    return index


def max_odd_index(my_list):
    max_num = -sys.maxsize
    index = -1

    for i in range(len(my_list)):
        num = my_list[i]
        if num >= max_num and num % 2 != 0:
            max_num = num
            index = i

    return index


def min_even_index(my_list):
    max_num = sys.maxsize
    index = -1

    for i in range(len(my_list)):
        num = my_list[i]
        if num <= max_num and num % 2 == 0:
            max_num = num
            index = i

    return index


def min_odd_index(my_list):
    max_num = sys.maxsize
    index = -1

    for i in range(len(my_list)):
        num = my_list[i]
        if num <= max_num and num % 2 != 0:
            max_num = num
            index = i

    return index


def first_even(my_list, count):
    temp_list = []
    counter = 0

    for num in my_list:
        if counter == count:
            break
        if num % 2 == 0:
            temp_list.append(num)
            counter += 1

    return temp_list


def first_odd(my_list, count):
    temp_list = []
    counter = 0

    for num in my_list:
        if counter == count:
            break
        if num % 2 != 0:
            temp_list.append(num)
            counter += 1

    return temp_list


def last_even(my_list, count):
    temp_list = []
    counter = 0

    for i in range(len(my_list) - 1, - 1, - 1):
        num = my_list[i]
        if counter == count:
            break
        if num % 2 == 0:
            temp_list.append(num)
            counter += 1

    temp_list.reverse()
    return temp_list


def last_odd(my_list, count):
    temp_list = []
    counter = 0

    for i in range(len(my_list) - 1, - 1, - 1):
        num = my_list[i]
        if counter == count:
            break
        if num % 2 != 0:
            temp_list.append(num)
            counter += 1

    temp_list.reverse()
    return temp_list

text = input().split()
command = input().split()
my_list = []

for i in text:
    my_list.append(int(i))

while command[0] != "end":

    if command[0] == "exchange":
        intcommand = int(command[1])
        if 0 > intcommand or intcommand > len(my_list):
            print("Invalid index")
            command = input().split()
            continue
        else:
            my_list = exchange(my_list, intcommand)

    elif command[0] == "max":
        index = -1
        if command[1] == "even":
            index = max_even_index(my_list)
        elif command[1] == "odd":
            index = max_odd_index(my_list)
        if index != -1:
            print(index)
        else:
            print("No matches")

    elif command[0] == "min":
        index = -1
        if command[1] == "even":
            index = min_even_index(my_list)
        if command[1] == "odd":
            index = max_odd_index(my_list)
        if index != -1:
            print(index)
        else:
            print("No matches")

    elif command[0] == "first":
        count = int(command[1])
        if count > len(my_list):
            print("Invalid count")
            command = input().split()
            continue

        res = []

        if command[2] == "even":
            res = first_even(my_list, count)
        elif command[2] == "odd":
            res = first_odd(my_list, count)

        print(res)

    elif command[0] == "last":
        count = int(command[1])
        if count > len(my_list):
            print("Invalid count")
            command = input().split()
            continue

        res = []
        if command[2] == "even":
            res = last_even(my_list, count)
        elif command[2] == "odd":
            res = last_odd(my_list, count)
        print(res)

    command = input().split()
print(my_list)