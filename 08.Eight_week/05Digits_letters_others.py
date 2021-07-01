text = input()
digits = []
chars = []
alpha = []


for chr in text:

    if chr.isdigit():
        digits.append(chr)
    elif chr.isalpha():
        alpha.append(chr)
    else:
        chars.append(chr)

print(''.join(digits))
print(''.join(alpha))
print(''.join(chars))