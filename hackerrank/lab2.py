# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def common_factors(a, b):
    gcd_ab = gcd(a, b)
    return count_divisors(gcd_ab)

# Read input values
a, b = map(int, input().split())

# Get the result
result = common_factors(a, b)

# Print the result
print(result)
