def palindrome(text):
    length = len(text) // 2
    is_palindrome = True

    for i in range(length):
        if text[i] != text[len(text) - 1 - i]:
            is_palindrome = False
            break

    return is_palindrome


def solve(items):

    for item in items:
        print(palindrome(item))


items = input().split(", ")
solve(items)