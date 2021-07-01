from collections import defaultdict

synonyms = defaultdict(list)
n = int(input())

for i in range(1, n + 1):
    word = input()
    value = input()
    synonyms[word].append(value)

for k,v in synonyms.items():
    print(f"{k} - {', '.join(v)}")