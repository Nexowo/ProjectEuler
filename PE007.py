"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
    
list_primes = [2]
i = 2
while(len(list_primes)<10001):
    for elem in list_primes:
        if i%elem == 0:
            break
        elif elem == list_primes[-1]:
            list_primes.append(i)
            break
    i+=1

print(list_primes[-1])
