def characters(a, b):
    new_str = ""
    if ord(a) <= ord(b):
        for i in range(ord(a) + 1, ord(b)):
            new_str += chr(i) + " "
    else:
        for i in range(ord(b) + 1, ord(a)):
            new_str += chr(i) + " "

    return new_str

a = input()
b = input()
print(characters(a, b))