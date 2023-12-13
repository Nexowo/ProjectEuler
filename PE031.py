"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

t=[200,100,50,20,10,5,2,1]

def calc(x,t):
    s=0
    if x == 200:
        return 1

    if t == []:
        return 0
    
    if x > 200:
        return 0
    
    for i in range(len(t)):
        s += calc(x+t[i], t[i:])
    
    return s
    

print(calc(0,t))
