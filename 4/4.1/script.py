"""
Compute the Parity of Binary Number
- Parity is 1 if total number of 1s are odd, otherwise 0
"""
a = 11011

# Method 1: Time Complexity: O(n), Space Complexity: O(1)
def compute_parity_1(x):
    ones = 0
    while x:
        last_bit = x % 10
        if last_bit is 1:
            ones += 1
        x //= 10

    return 1 if ones % 2 == 1 else 0

#print(compute_parity_1(a))


# Method 2: Time Complexity: O(n), Space Complexity: O(1)
def compute_parity_2(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
#print(compute_parity_2(a))

