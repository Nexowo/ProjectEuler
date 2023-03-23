"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(x :int):
    l_x = str(x)
    for i in range(len(l_x)//2):
        if l_x[i]!=l_x[-(i+1)]:
            return False
    return True

largest_palindrome = 0

for x in range(100, 1000):
    for y in range(100, x+1):
        z = x*y
        if is_palindrome(z) and z > largest_palindrome:
            largest_palindrome = z

print(largest_palindrome)
