"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

(Enhanced thanks to C. Obrecht)
"""

def exaustive_primal_test(number:int, primes:list[int]) -> bool:
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

if __name__ == "__main__":
    print(sum(get_n_first_primes(2000000)))

