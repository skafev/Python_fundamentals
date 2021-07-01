def loading_bar(number):
    divided = number // 10
    counter = 0

    for i in range(1, divided + 1):
        counter += 1

    second_counter = 10 - counter

    return f"{number}% [{counter * '%'}{second_counter * '.'}]"


number = int(input())
if number == 100:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
else:
    print(loading_bar(number))
    print("Still loading...")