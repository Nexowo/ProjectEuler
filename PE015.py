"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

def fact(n):
    f = 1
    for i in range(1,n+1):
        f= f*i
    return f

print(int(fact(40)/(fact(20)**2))) #Formula to choose 10 in 20 as go from the top left to bottom right remains to move 10 times down and 10 times right arranged as you want
