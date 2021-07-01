from collections import defaultdict

num = int(input())
students = defaultdict(list)
filtered_students = defaultdict(float)
average_grade = 4.5
for n in range(1, num + 1):

    name = input()
    grade = float(input())
    students[name].append(grade)


for k, v in students.items():
    total_grade = sum(v) / len(v)
    if total_grade >= average_grade:
        filtered_students[k] = total_grade

for k, v in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{k} -> {v:.2f}")