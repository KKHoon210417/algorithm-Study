input = "abcba"


def is_palindrome(string):
    for i in range(len(string)):
        if not string[i] == string[len(string)-i-1]:
            return False
    return True

print(is_palindrome(input))