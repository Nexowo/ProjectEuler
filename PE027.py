"""
Euler discovered the remarkable quadratic formula:
n²+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39

The incredible formula n²-79n+1601 was discovered, which produces 80 primes for the consecutive values 0<=n<=79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n²+an+b, where |a|<1000 and |b|<=1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0
"""

def exaustive_primal_test(number:int, primes:list[int]) -> bool:
    if number<0:
        return False
    limit = number ** (1/2)
    for p in primes:
        if p > limit:
            return True
        if number % p == 0:
            return False
    return True

def get_n_first_primes(n:int)-> list[int]:
    primes = [2]
    for i in range(3,n+1,2):
        if exaustive_primal_test(i, primes):
            primes.append(i)

    return primes

b = get_n_first_primes(2000000)
d = {}
for i in b:
    if i > 1000:
        break
    for a in range(-999, 1000):
        k=0
        while exaustive_primal_test(k**2+a*k+i, b):
            k+=1
        d[i*a] = k

print(max(d, key=d.get))
