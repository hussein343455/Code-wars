# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace
# the missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']
def solution(s):
    re=[]
    i,j=0,2
    if not s:return []
    while j<len(s):
        re.append(s[i:j])
        i+=2
        j+=2
    if len(s)%2==0:
        re.append(s[-2]+s[-1])
        return re
    re.append(s[-1]+"_")
    return re