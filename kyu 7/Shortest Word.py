# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    s=s.split()
    sol=s[0]
    for j in s:
        if len(j)<len(sol):
            sol=j
    return len(sol) # l: shortest word length