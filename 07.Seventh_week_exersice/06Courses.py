from collections import defaultdict

courses = defaultdict(list)

while True:
    command = input()
    if command == "end":
        break

    course, name = command.split(" : ")
    courses[course].append(name)

for k, v in sorted(courses.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{k}: {len(v)}")
    for i in sorted(v):
        print(f"-- {''.join(i)}")
