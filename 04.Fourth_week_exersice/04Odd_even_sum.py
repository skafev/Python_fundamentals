def odd_even_sum(number):
    odd = 0
    even = 0
    my_list = []
    for i in number:
        my_list.append(i)

    for num in my_list:
        if int(num) % 2 == 0:
            even += int(num)
        else:
            odd += int(num)

    return f"Odd sum = {odd}, Even sum = {even}"

number = input()
print(odd_even_sum(number))