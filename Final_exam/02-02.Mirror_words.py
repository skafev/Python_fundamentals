import re

text = input()
pattern = re.compile(r'((@[A-Za-z]{3,}@@[A-Za-z]{3,}@)|(#[A-Za-z]{3,}##[A-Za-z]{3,}#))')
matches = re.finditer(pattern, text)
hidden_word = ""

for match in matches:
    hidden_word += match[1]

mirror_words = []
pattern_fot_letters = re.compile(r"([A-Za-z]+)")
matches_for_letters = re.finditer(pattern_fot_letters, hidden_word)
valid_mirror_word = []

for m in matches_for_letters:
    mirror_words.append(m[1])
if hidden_word == "":
    print("No word pairs found!")
else:
    print(f"{len(mirror_words) // 2} word pairs found!")

index = 0
count = 0
for i in range(len(mirror_words) // 2):
    word_one = mirror_words[index]
    word_two = mirror_words[index + 1]
    index += 2

    word_two_to_check = word_two[::-1]
    if word_two_to_check == word_one:
        valid_mirror_word.extend((word_one, word_two))

if not valid_mirror_word:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    m = 0
    for k in range(len(valid_mirror_word) // 2):
        word_to_print = valid_mirror_word[m]
        second_word_to_print = valid_mirror_word[m + 1]
        m += 2
        if k + 1 == (len(valid_mirror_word) // 2):
            print(f"{word_to_print} <=> {second_word_to_print}", end="")
        else:
            print(f"{word_to_print} <=> {second_word_to_print}", end=", ")
