# Write a function, persistence,
# that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.


def persistence(n):
    if n<10:
        return 0
    re=1
    for i in str(n):
        re*=int(i)
    return 1+persistence(re)