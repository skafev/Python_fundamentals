text = input().split()
res = ""

for i in text:
    res += i * len(i)

print(res)