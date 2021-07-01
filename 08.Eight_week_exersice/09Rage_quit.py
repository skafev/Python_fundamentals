text = input()
result = ""
string = ""
digit = ""
length = len(text)
rotate = True

while rotate:
    for ch in text:

        if ch.isdigit():
            digit += ch

        else:
            if digit != "":
                result += string.upper() * int(digit)
                length -= (len(string) + len(digit))
                if length == 0:
                    rotate = False
                    break

                string = ""
                digit = ""
            string += ch

unique_symbols = len(set(result))
print(f"Unique symbols used: {unique_symbols}")
print(result)
