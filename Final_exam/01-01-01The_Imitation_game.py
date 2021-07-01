message_to_decode = input()

while True:
    text = input().split("|")

    if text[0] == "Decode":
        break

    elif text[0] == "Move":
        number_of_letters = text[1]
        letter = ""
        for i in range(int(number_of_letters)):
            letter += message_to_decode[i]
        message_to_decode = message_to_decode.replace(letter, "") + letter

    elif text[0] == "Insert":
        index = text[1]
        value = text[2]
        if 0 <= int(index) <= len(message_to_decode):
            message_to_decode = message_to_decode[:int(index)] + value + message_to_decode[int(index):]

    elif text[0] == "ChangeAll":
        substring = text[1]
        replacement = text[2]
        if substring in message_to_decode:
            message_to_decode = message_to_decode.replace(substring, replacement, len(message_to_decode))

print(f"The decrypted message is: {message_to_decode}")
