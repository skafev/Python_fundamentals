def add_number(my_list, command, wagons):
    index = wagons - 1
    number = int(command[1])
    my_list[index] += number

    return my_list


def insert_number(my_list, command):
    index = int(command[1])
    number = int(command[2])
    my_list[index] += number

    return my_list


def leave_wagon(my_list, command):
    index = int(command[1])
    number = int(command[2])
    my_list[index] -= number

    return my_list


wagons = int(input())
command = input()
my_list = [0 for n in range(wagons)]

while command != "End":
    command = command.split()

    if command[0] == "add":
        my_list = add_number(my_list, command, wagons)

    elif command[0] == "insert":
        my_list = insert_number(my_list, command)

    elif command[0] == "leave":
        my_list = leave_wagon(my_list, command)

    command = input()
print(my_list)