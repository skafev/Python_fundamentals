def perfect_number(number):
    half = number // 2
    perfect = 0

    for i in range(1, half + 1):
        if number % i == 0:
            perfect += i

    if perfect == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))