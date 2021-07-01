words = input().split(", ")
text = input()

res = [word for word in words if word in text]

print(res)