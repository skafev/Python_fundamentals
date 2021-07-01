factor = int(input())
count = int(input())
my_list = []
for n in range(factor, (count * factor) + 1, factor):
    my_list.append(n)
print(my_list)