numbers = input().split(", ")
the_biggest = 0

for num in numbers:

    if int(num) > int(the_biggest):
        the_biggest = int(num)

lists = the_biggest // 10
if the_biggest % 10 != 0:
    lists += 1

for i in range(1, lists + 1):
    groups = []

    for nums in numbers[:]:

        if int(nums) <= (i * 10):
            groups.append(int(nums))
            numbers.remove(nums)

    print(f"Group of {i * 10}'s: {groups}")