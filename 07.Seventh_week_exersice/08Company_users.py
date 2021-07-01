from collections import defaultdict

companies = defaultdict(list)

while True:

    command = input()
    if command == "End":
        break

    company, employee = command.split(" -> ")

    if employee not in companies[company]:
        companies[company].append(employee)


for k, v in sorted(companies.items()):
    print(f"{k}")
    for i in v:
        print(f"-- {i}")
