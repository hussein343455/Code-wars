# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.
def find_it(seq):
    re=cou=0
    for i in seq:
        t=seq.count(i)
        if re<t and t%2!=0:
            re=t
            cou=i
    return cou
