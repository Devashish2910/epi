"""
Check if Numbers id Palindrome or Not
E.g:
121 => True
112 => False
1 => True
-121 => False
"""
import math

def palindrome_numbder(num):
    if num < 0:
        return False

    if 0 <= num <= 9:
        return True

    ranger, temp = 1, num
    while temp > 9:
        temp //= 10
        ranger *= 10
        
    """
    total_digits = math.floor(math.log10(num)) + 1
    ranger = 10 ** (total_digits - 1)
    """

    while num:
        last_digit = num % 10
        first_digit = num // ranger

        if last_digit == first_digit:
            num = (num % ranger) // 10
            ranger //= 100
        else:
            return False

    return True


if __name__ == "__main__":
    print(palindrome_numbder(121))
    print(palindrome_numbder(112))
    print(palindrome_numbder(3))
    print(palindrome_numbder(-121))