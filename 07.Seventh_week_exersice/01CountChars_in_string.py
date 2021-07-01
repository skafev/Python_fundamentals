from collections import defaultdict

data = input()
count_chars = defaultdict(int)

for char in str(data):
    if not char.isspace():
        count_chars[char] += 1

for k,v in count_chars.items():
    print(f"{k} -> {v}")