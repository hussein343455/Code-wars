# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers
# except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def dis(integers):
    k='o'
    top=0
    for i in integers:
        if i%2==0:
            top+=1
        if top==2:
            k="e"
            break
    for i in integers:
        if i%2==0 and k=='o':
            return i
        if  (i-1)%2==0 and k=='e':
            return i
print(dis([2, 4, 0, 100, 4, 11, 2602, 36]))