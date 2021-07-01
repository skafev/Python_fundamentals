text = input().split(", ")
beggars = int(input())
new_list = []
index = 0
beggars_count = []

for i in range(beggars):
    beggars_count.append(0)

for number in text:
    beggars_count[index] += int(number)
    index += 1
    if index == beggars:
        index = 0
print(beggars_count)