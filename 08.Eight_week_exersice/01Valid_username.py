text = input().split(", ")
usernames = []
current_word = ""

for word in text:
    if 3 <= len(word) <= 16:
        for char in word:

            if char.isdigit() or char.isalpha() or char == "-" or char == "_":
                current_word += char
            if len(current_word) == len(word):
                usernames.append(word)

        current_word = ""

for i in usernames:
    print("".join(i))
