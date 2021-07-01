number = int(input())

for i in range(0, number):
    for x in range(0, number):
        for j in range(0, number):
            print(f"{chr(97 + i)}{chr(97 + x)}{chr(97 + j)}")