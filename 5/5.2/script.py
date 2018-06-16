"""
Increment an Arbitrary-Precision Integer
E.g -
[1, 2, 3] => [1, 2, 4]
[1, 2, 9= => [1, 3, 0]
"""
def increment_by_one(arr):
    # Kids do this
    """
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
    """
    arr[-1] += 1

    for i in range(len(arr)-1, 0, -1):
        if arr[i] is not 10:
            break
        arr[i] = 0
        arr[i-1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

print(f"[1, 2, 3] => {increment_by_one([1, 2, 3])}")
print(f"[9, 2, 3] => {increment_by_one([9, 2, 3])}")
print(f"[9, 9] => {increment_by_one([9, 9])}")