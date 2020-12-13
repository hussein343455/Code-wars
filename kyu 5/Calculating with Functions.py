# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

# Requirements:
# #There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
# plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))




def zero(num = "x"):
    if num == "x":return 0
    return int(eval(str(0) + num))

def one(num = "x"):
    if num == "x":return 1
    return int(eval(str(1) + num))

def two(num = "x"):
    if num == "x":return 2
    return int(eval(str(2) + num))

def three(num = "x"):
    if num == "x":return 3
    return int(eval(str(3) + num))

def four(num = "x"):
    if num == "x":return 4
    return int(eval(str(4) + num))

def five(num = "x"):
    if num == "x":return 5
    return int(eval(str(5) + num))

def six(num = "x"):
    if num == "x":return 6
    return int(eval(str(6) + num))

def seven(num = "x"):
    if num == "x":return 7
    return int(eval(str(7) + num))

def eight(num = "x"):
    if num == "x":return 8
    return int(eval(str(8) + num))

def nine(num = "x"):
    if num == "x":return 9
    return int(eval(str(9)+num))



def plus(x):
    if type(x)==int:
        return "+"+str(x)
def minus(x):
    if type(x)==int:
        return "-"+str(x)
def times(x):
    if type(x)==int:
        return "*"+str(x)
def divided_by(x):
    if type(x)==int:
        return "/"+str(x)