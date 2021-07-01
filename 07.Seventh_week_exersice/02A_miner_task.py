from collections import defaultdict

my_dict = defaultdict(int)

command = input()
while command != "stop":
    key = command
    value = int(input())
    my_dict[key] += value
    command = input()

for k, v in my_dict.items():
    print(f"{k} -> {v}")