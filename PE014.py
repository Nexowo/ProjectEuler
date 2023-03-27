"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

m_dict = {}

m_dict[1] = 0

def get_n_it(n : int):
    val = m_dict.get(n)
    if val != None:
        return val
    nn = n//2 if n%2 == 0 else n*3+1
    m_dict[n] = get_n_it(nn)+1
    return m_dict[n]

for i in range(1,1000001,2):
    get_n_it(i)

print(max(m_dict,key=m_dict.get))
