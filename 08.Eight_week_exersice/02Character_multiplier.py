text = input().split()
word_one = text[0]
word_two = text[1]
total = 0

min_length = len(word_one)
if len(word_two) < len(word_one):
    min_length = len(word_two)

max_length = word_one
if len(word_two) > len(word_one):
    max_length = word_two

for i in range(min_length):
    total += ord(word_one[i]) * ord(word_two[i])

for j in range(min_length, len(max_length)):
    total += ord(max_length[j])

print(total)