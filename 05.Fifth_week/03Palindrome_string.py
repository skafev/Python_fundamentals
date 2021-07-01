def is_palindrome(text):
    new_text = []

    for word in text:
        length = len(word) // 2
        palidrome = True

        for index in range(length):
            if word[index] != word[(len(word) - 1 - index)]:
                palidrome = False

        if palidrome == True:
            new_text.append(word)
    text = new_text
    return print(text)

def search_in_text(text, search_word):
    count = 0
    for word in text:
        if word == search_word:
            count += 1

    return print(f"Found palindrome {count} times")


text = input().split()
search_word = input()

is_palindrome(text)
search_in_text(text, search_word)

# string = input().split()
# searched_word = input()
# palidroms = []
#
# for word in string:
#     if word == "".join(reversed(word)):
#         palidroms.append(word)
#
# print(palidroms)