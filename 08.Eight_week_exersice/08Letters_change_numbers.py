text = input().split()
string = ""
number = ""
total_before = 0
total = 0

for i in text:
    for ch in i:
        if ch.isalpha():
            string += ch
            if number != "":
                if string[0].isupper():
                    total_before += int(number) / (ord(string[0]) - 64)
                else:
                    total_before += int(number) * (ord(string[0]) - 96)

                if string[1].isupper():
                    total_before = total_before - (ord(string[1]) - 64)
                else:
                    total_before = total_before + (ord(string[1]) - 96)
                total += total_before
                total_before = 0
                number = ""
                string = ""
        else:
            number += ch

print(f"{total:.2f}")
