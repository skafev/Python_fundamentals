num = int(input())
my_list = []

for n in range(1, num + 1):
    new_num = int(input())
    my_list.append(new_num)
command = input()
new_string = []
if command == "even":
    for m in range(len(my_list)):
        if my_list[m] % 2 == 0:
            new_string.append(my_list[m])
if command == "odd":
    for m in range(len(my_list)):
        if my_list[m] % 2 != 0:
            new_string.append(my_list[m])
if command == "negative":
    for m in range(len(my_list)):
        if my_list[m] < 0:
            new_string.append(my_list[m])
if command == "positive":
    for m in range(len(my_list)):
        if my_list[m] >= 0:
            new_string.append(my_list[m])
print(new_string)