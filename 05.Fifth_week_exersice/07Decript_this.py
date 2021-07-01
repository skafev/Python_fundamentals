def number_to_char(word):

    temp = ""
    other = ""

    for ch in word:
        if ch.isdigit():
            temp += "".join(ch)
        else:
            other += "".join(ch)

    new_word = chr(int(temp))
    newest_word = new_word + other

    return newest_word


def switched_letters(word):
    text = list(word)

    text[1], text[-1] = text[-1], text[1]

    return "".join(text)

def decript(word):
    res = number_to_char(word)
    res = switched_letters(res)

    return res


secret_message = input().split()

decriptet = [decript(x) for x in secret_message]
print(" ".join(decriptet))