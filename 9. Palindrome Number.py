# Given an integer x, return true if x is a palindrome and false otherwise.

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x > 0:
        return x == int(str(x)[::-1])


print(isPalindrome(1101))
