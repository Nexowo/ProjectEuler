"""
Euler discovered the remarkable quadratic formula:
n²+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39

The incredible formula n²-79n+1601 was discovered, which produces 80 primes for the consecutive values 0<=n<=79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n²+an+b, where |a|<1000 and |b|<=1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0
"""
s = 1
z = 0
for i in range(1,501):
    for j in range(1,5):
        z+=i
        s+=2*z+1
        
print(s)
