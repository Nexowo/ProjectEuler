"""
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

n = 100
x = 1
for i in range(1,n+1):
    x = x*i

s = 0
for num in str(x):
    s+=int(num)

print(s)
