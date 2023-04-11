"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

days = {
    0: "m",
    1: "t",
    2: "w",
    3: "th",
    4: "f",
    5: "sa",
    6: "s"
}

s_d = 365%7
count = 0
for i in range(100):
    n_d : int
    if (i+1)%4 > 0: #We start from 1901 thus we need +1
        n_d=28
    else:
        n_d=29
    for i in range(12):
        if i in [0,2,4,6,7,9,11]:
            s_d+=31%7
        elif i in [3,5,8,10]:
            s_d+=30%7
        else:
            s_d+=n_d%7
        s_d = s_d%7
        if days[s_d] == 's':
            count+=1

print(count)
