"""
Reverse the Digit
E.g ->  31 => 13
    -> -123 => -321
"""

def reverse_digit(digit):
    result, temp = 0, abs(digit)

    while temp:
        result = (result * 10) + (temp % 10)
        temp //= 10

    print(-result if digit < 0 else result)
    return


if __name__ == "__main__":
    reverse_digit(7653)
    reverse_digit(-32156)