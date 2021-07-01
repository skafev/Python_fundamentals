tasks = []

while True:
    command = input()

    if command == "End":
        break

    tokens = command.split("-")
    priority = int(tokens[0])
    task = tokens[1]
    tasks.append((priority, task))

final_tasks = [task for priority,task in sorted(tasks)]
print(final_tasks)