number = int(input())


for n in range(1, number+1):

    if n == 5:
        print(f"{n} -> True")
        continue

    if n == 7:
        print(f"{n} -> True")
        continue

    if n > 10:
        digits = [int(x) for x in str(n)]
        if digits[0] + digits[1] == 5 or digits[0] + digits[1] == 7 or digits[0] + digits[1] == 11:
            print(f"{n} -> True")
        else:
            print(f"{n} -> False")
    else:
        print(f"{n} -> False")

