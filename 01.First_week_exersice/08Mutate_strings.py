first_string = input ( )
second_string = input ( )

length = len(first_string)

for index in range(length):
    if first_string[index] != second_string[index]:
        for i in range(0, index+1):
            print(second_string[i], end="")
        for j in range(index + 1, length):
            print(first_string[j], end="")
        print()