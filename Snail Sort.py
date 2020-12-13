# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

# For better understanding, please follow the numbers of the next array consecutively:
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

def snail(snail_map):
    new_array= snail_map
    if len(snail_map)==0:
        return []
    if len(snail_map) == 1:
        return snail_map[0]
    if len(snail_map)*2 == 4:
        return snail_map[0]+[snail_map[1][1]]+[snail_map[1][0]]
    #first row
    re=snail_map[0].copy()
    re.pop()
    # last colman
    for row, sublist in enumerate(snail_map):
        re.append(sublist[len(sublist)-1])
    re.pop()

    # last row
    k=snail_map[len(sublist)-1]
    k.reverse()
    for i in k:
        re.append(i)

    # first colman
    relasr=[]
    for row, sublist in enumerate(snail_map):
        relasr.append(sublist[0])
    relasr=un(relasr)
    new=[]
    for i in relasr:
        re.append(i)
    del(new_array[0])
    del (new_array[len(new_array)-1])
    for i in new_array:
        relasr=un(i)
        new.append(relasr)
        relasr.reverse()
    return re+snail(new)
def un(x):
    x.pop()
    x.reverse()
    x.pop()
    return x