text = input().split(" ")
number = int(input())
length = len(text) // 2

for n in range(1, number + 1):
    my_list = []

    for index in range(length):

        first_card = text[index]
        second_card = text[index + length]
        my_list.append(first_card)
        my_list.append(second_card)
    text = my_list
print(text)