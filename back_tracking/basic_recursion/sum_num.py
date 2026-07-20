# Problem 1: Sum from 1 to n

# Write a recursive function:

# sum_numbers(n)

# It should return:

# 1 + 2 + 3 + ... + n

def sum(n):
    if n == 1 :
        return 1
    
    return n + sum(n-1)

print(sum(3))