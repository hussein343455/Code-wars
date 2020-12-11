
# Define a function that takes in two non-negative integers aaa and bbb and returns the last decimal digit of a^b
# Note that a and b may be very large!

# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6



def last_digit(n1, n2):
    n1=str(n1)
    if n2==0:
        return 1
    n1=int(n1[len(n1)-1])
    n2=n2%4
    if n2==0:n2=4
    x = str(n1**n2)
    return int(x[len(x) - 1])