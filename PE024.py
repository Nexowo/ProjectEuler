"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

n = 999999

def ithperm(f : int, j : int):
    fact = [1]
    for i in range(1,f):
        fact.append(fact[i-1]*i)

    perm = []
    for i in range(f):
        perm.append(j//fact[f-1-i])
        j=j%fact[f-1-i]
    
    for i in range(f-1,0,-1):
        for k in range(i-1, -1, -1):
            if perm[k] <= perm[i]:
                perm[i]+=1
    
    return perm
    

print(''.join(str(i)+ "" for i in ithperm(10, n)))
