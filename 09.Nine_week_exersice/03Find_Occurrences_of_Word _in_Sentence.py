import re

text = input()
word_to_find = input()

pattern = re.compile(rf"\b{word_to_find}\b", re.IGNORECASE)

matches = re.findall(pattern, text)
print(len(matches))
