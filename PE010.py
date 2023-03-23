"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

s=0

def list_primes(x : int):
    primes = [2]
    for i in range(2, x+1):
        for elem in primes:
            if i%elem == 0:
                break
            elif elem == primes[-1]:
                primes.append(i)
                break
    return primes

for elem in list_primes(2000000):
    s+=elem

print(s)
