import sys


def exchange(numbers, index):
    temp_number = numbers[index + 1:]
    temp_number += numbers[1:index + 1]

    return temp_number


def max_even_index(numbers):
    max_num = -sys.maxsize
    index = -1

    for i in range(len(numbers)):
        num = numbers[i]

        if num >= max_num and num % 2 == 0:
            max_num = num
            index = i

    return index


def max_odd_index(numbers):
    max_num = -sys.maxsize
    index = -1

    for i in range(len(numbers)):
        num = numbers[i]

        if num > max_num and num % 2 != 0:
            max_num = num
            index = i

    return index


def min_even_index(numbers):
    max_num = sys.maxsize
    index = -1

    for i in range(len(numbers)):
        num = numbers[i]

        if num < max_num and num % 2 == 0:
            max_num = num
            index = i

    return index


def min_odd_index(numbers):
    max_num = sys.maxsize
    index = -1

    for i in range(len(numbers)):
        num = numbers[i]

        if num < max_num and num % 2 != 0:
            max_num = num
            index = i

    return index


def first_even(numbers, count):
    temp_list = []
    counter = 0

    for num in numbers:
        if counter == count:
            break
        if num % 2 == 0:
            temp_list.append(num)
            counter += 1

    return temp_list


def first_odd(numbers, count):
    temp_list = []
    counter = 0

    for num in numbers:
        if counter == count:
            break
        if num % 2 != 0:
            temp_list.append(num)
            counter += 1

    return temp_list


def last_even(numbers, count):
    temp_list = []
    counter = 0

    for i in range(len(numbers) - 1, - 1, - 1):
        num = numbers[i]

        if counter == count:
            break
        if num % 2 == 0:
            temp_list.append(num)
            counter += 1

    temp_list.reverse()
    return temp_list


def last_odd(numbers, count):
    temp_list = []
    counter = 0

    for i in range(len(numbers) - 1, - 1, - 1):
        num = numbers[i]

        if counter == count:
            break

        if num % 2 != 0:
            temp_list.append(num)
            counter += 1

    temp_list.reverse()
    return temp_list


items = input().split()
command_input = input()
numbers = []

for item in items:
    numbers.append(int(item))

while command_input != "end":
    tokens = command_input.split()
    command = tokens[0]

    if command == "exchange":
        index = int(tokens[1])

        if index < 0 or index >= len(numbers):
            print("Invalid index")
            command_input = input()
            continue

        numbers = exchange(numbers, index)

    elif command == "max":
        index = -1

        if tokens[1] == "even":
            index = max_even_index(numbers)

        elif tokens[1] == "odd":
            index = max_odd_index(numbers)

        if index != -1:
            print(index)
        else:
            print("No matches")

    elif command == "min":
        index = -1

        if tokens[1] == "even":
            index = min_even_index(numbers)

        if tokens[1] == "odd":
            index = max_odd_index(numbers)

        if index != -1:
            print(index)
        else:
            print("No matches")

    elif command == "first":
        count = int(tokens[1])

        if count > len(numbers):
            print("Invalid count")
            command_input = input()
            continue

        res = []

        if tokens[2] == "even":
            res = first_even(numbers, count)

        elif tokens[2] == "odd":
            res = first_odd(numbers, count)

        print(res)

    elif command == "last":
        count = int(tokens[1])

        if count > len(numbers):
            print("Invalid count")
            command_input = input()
            continue

        res = []

        if tokens[2] == "even":
            res = last_even(numbers, count)

        elif tokens[2] == "odd":
            res = last_odd(numbers, count)

        print(res)

    command_input = input()
print(numbers)
