
# Problem 3: Check whether a string is a palindrome

# A palindrome reads the same forward and backward.

# Examples:

# "level"
# "madam"
# "racecar"

# Write:

# is_palindrome(text)
# Examples
# is_palindrome("level")   # True
# is_palindrome("hello")   # False
# is_palindrome("a")       # True
# is_palindrome("")        # True

# Do not use:

# text[::-1]
# reversed()


"""
Going to initialize two indexes
left and right
if st[left] == str[right]
continue recursion

else false

"""
import time
import sys

def is_pallindrome(str_s):
    
    left = 0
    right = len(str_s) - 1
    
    print(left)
    # time.sleep(1)
    print(right)
    # time.sleep(1)
    print(str_s[left:right+1])
    # time.sleep(1)
    # Passed all the condition to reach this point, it means it is a valid pallindrome
    if(left == right):
        print("inside the base case")
        sys.exit(0)
    
    if not(str_s[left] == str_s[right]):
        sys.exit(1)
    else:
        is_pallindrome(str_s[left+1:right])
    
print(is_pallindrome("level") == 0)
