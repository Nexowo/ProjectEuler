"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for c in range(1000+1):
    for b in range(c):
        for a in range(b):
            if a + b + c == 1000:
                if (a**2 + b**2) == c**2:
                    print(a*b*c)
                else:
                    break
        if b + c >= 1000:
            break
