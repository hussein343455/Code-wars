# Create function that takes one positive three digit integer and rearranges its digits to get maximum possible number. Assume that argument is integer. Return null (nil for ruby) if argument is not valid.

# maxRedigit(123); // returns 321
def max_redigit(num):
    if num<=0 or num>999 or num<100:
        return None
    num=sorted(str(num))
    num.reverse()
    num="".join([i for i in num])
    return int(num)
