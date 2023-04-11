"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

d = {
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    100 : "hundred",
    1000 : "thousand"
}

def len_nb(n : int):
    i = 0
    if n > 100 and n%100 > 0:
        i+=3
    if n//1000 > 0:
        i+= len(d[n//1000])
        i+= len(d[1000])
        n = n%1000
    if n//100 > 0:
        i+= len(d[n//100])
        i+= len(d[100])
        n = n%100
    if n//10 > 0:
        if n > 20:
            i+= len(d[(n//10)*10])
            n = n%10    
    return i + len(d[n])

s = 0

for i in range(1,1001):
    s+= len_nb(i)

print(s)
