# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers
# or a range of integers denoted by the starting integer
# separated from the end integer in the range by a dash, '-'. The range includes all
# integers in the interval including both endpoints. It is not considered a range
# unless it spans at least 3 numbers. For example "12,13,15-17"

# Complete the solution so that it takes a list of integers
# in increasing order and returns a correctly formatted string in the range format.

# Example:
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"



def solution(args):
    re=[]
    indre=[]
    args.append("x")
    for ind,val in enumerate(args):
        if val=="x":
            break
        if val+1==args[ind+1]:
            indre.append(val)
        else:
            if  len(indre)>=2:
                indre.append(val)
                T=str(indre[0])+"-"+str(indre[len(indre)-1])
                re.append(T)
                indre.clear()
            elif len(indre)==0:
                re.append(val)
            else:#empty
                indre.append(val)
                re.extend(indre)
                indre.clear()
    k="".join([str(v)+"," for ind,v in enumerate(re)])
    k=k[:-1]
    return k
x=[-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
# x=[1,3,4,6,7,9]
print(solution(x))