"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

n = 20

def list_primes(x : int):
    if x == 2:
        return [x]
    else:
        y = list_primes(x-1)
        for elem in y:
            if x%elem == 0:
                return y
            
        return y + [x]
    
s_num = 1
for elem in list_primes(n):
    s_num = s_num*elem

i = 2
while(i**2 < n):
    s_num = s_num*i
    i+=1

print(s_num)
