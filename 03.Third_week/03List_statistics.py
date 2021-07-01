list_positive = []
list_negative = []
num = int(input())

for n in range(1, num + 1):
    n1 = int(input())
    if n1 >= 0:
        list_positive.append(n1)
    else:
        list_negative.append(n1)
print(list_positive)
print(list_negative)
print(f"Count of positive {len(list_positive)}, count of negative {sum(list_negative)}")