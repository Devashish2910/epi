"""
Multiply two Arbitrary-Precision Integer
E.g -
[-2, 1], [1, 0, 0] => [2, 1, 0, 0]
[2, 2, 2], [9, 8, 7, 6, 5] => [2, 1, 9, 2, 5, 8, 3, 0]
"""
def multiply_two_arrs(num1, num2):
    # check the sign
    sign = -1 if (num1[0] < 0 ^ num2[0] < 0) else 1

    # make first digit absolute
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))

    # Logic: 21 * 22 => 21 * 2 = 42 and 21 * 2 = 42 -> 42 * 10 = 420
    #        42 + 420 = 462
    for i in reversed(range(0, len(num1))):
        for j in reversed(range(0, len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # remove leading zeros
    i = 0
    while result[i] == 0:
        i += 1

    return [sign * result[i]] + result[i+1:]

multiply_two_arrs([-2, 1], [1, 0, 0])
multiply_two_arrs([1, 2, 3], [9, 8, 7])
multiply_two_arrs([2, 2, 2], [9, 8, 7, 6, 5])
print(multiply_two_arrs([2,1], [2,2]))