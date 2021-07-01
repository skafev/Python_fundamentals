num = int(input())
key_word = input()
new_list = []
for n in range(1, num + 1):
    word = input()
    new_list.append(word)
print(new_list)
for n in range(0, len(new_list) - 1):
    if key_word not in new_list[n]:
        new_list.remove(new_list[n])
print(new_list)