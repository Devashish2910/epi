"""
Increment an Arbitrary-Precision Integer
E.g -
[1, 2, 3] => [1, 2, 4]
[1, 2, 9= => [1, 3, 0]
"""
def increment_by_one(arr):
    num = 0
    for digit in arr:
        num = (num * 10) + digit

    num += 1

    result = []

    while num:
        digit = num%10
        result.insert(0, digit)
        num //= 10

    return result

print(increment_by_one([1, 2, 3]))
print(increment_by_one([1, 2, 3, 9]))
print(increment_by_one([9, 9]))