numbers = input().split(" ")
new_text = []
for number in numbers:
    current_number = int(number)
    new_text.append(current_number * -1)
print(new_text)