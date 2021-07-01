numbers = input().split()
text = input()
secret_word = ""

while len(numbers) > 0:
    i = 0
    sum_digits = 0

    for num in numbers[0]:
        sum_digits += int(num)

    while i < sum_digits:

        for x in enumerate(list(text)):
            i += 1

            if i == sum_digits + 1:
                secret_word += str(x[1])
                text = text[0:int(x[0]):] + text[int(x[0]) + 1::]
                del numbers[0]
                break

print(secret_word)