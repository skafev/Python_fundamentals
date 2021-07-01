t1 = input()
t2 = input()

while t1 in t2:
    t2 = t2.replace(t1, "", -1)

print(t2)