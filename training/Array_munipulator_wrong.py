text = input().split()
command = input().split()
my_list = []
max_odd = 0
max_even = 0
min_odd = 0
min_even = 10000000
first_count_even = []
last_count_even = []
first_count_odd = []
last_count_odd = []
for i in text:
    my_list.append(int(i))

while command[0] != "end":

    if command[0] == "exchange":
        intcommand = int(command[1])
        if 0 > intcommand or intcommand > len(my_list):
            print("Invalid index")

        else:
            my_list = my_list[intcommand + 1:] + my_list[:1 + intcommand]


    elif command[1] == "odd":

        if command[0] == "max":
            for n in my_list:
                if n % 2 != 0:
                    if n >= max_odd:
                        max_odd = n
            if max_odd != 0:
                    print(my_list.index(max_odd))
            else:
                print("No matches")

        if command[0] == "min":
            for n in my_list:
                if n % 2 != 0:
                    min_odd = n
                    if n <= min_odd:
                        min_odd = n
            if min_odd != 0:
                print(my_list.index(min_odd))
            else:
                print("No matches")

    elif command[1] == "even":

        if command[0] == "max":
            for m in my_list:
                if m % 2 == 0:
                    if m >= max_even:
                        max_even = m
            if max_even != 0:
                print(my_list.index(max_even))
            else:
                print("No matches")

        if command[0] == "min":
            for m in my_list:
                if m % 2 == 0:
                    if m <= min_even:
                        min_even = m

            if min_even != 10000000:
                print(my_list.index(min_even))
            else:
                min_even = 0
                print("No matches")

    elif command[0] == "first":
        count = int(command[1])

        if count > len(my_list):
            print("Invalid count")

        elif command[2] == "even":
            for j in my_list:
                if j % 2 == 0:
                    first_count_even.append(j)
                    count -= 1
                    if count == 0:
                        break
            print(first_count_even)

        elif command[2] == "odd":
            for k in my_list:
                if k % 2 != 0:
                    first_count_odd.append(k)
                    count -= 1
                    if count == 0:
                        break
            print(first_count_odd)

    elif command[0] == "last":
        count = int(command[1])

        if count > len(my_list):
            print("Invalid count")

        if command[2] == "even":
            for v in my_list:
                if v % 2 == 0:
                    last_count_even.append(v)
            while len(last_count_even) > count:
                del last_count_even[0]
            print(last_count_even)

        if command[2] == "odd":
            for t in my_list:
                if t % 2 != 0:
                    last_count_odd.append(t)
            while len(last_count_odd) > count:
                del last_count_odd[0]
            print(last_count_odd)

    command = input().split()
print(my_list)