# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis,
# input may contain any valid ASCII characters. Furthermore,
# the input string may be empty and/or not contain any parentheses at all.
# Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).



def valid_parentheses(string):
    done=True
    while done:
        k=string
        string,done=deletr(string)
        if k==string:
            break
    return done

def deletr(string):
    for indi,i in enumerate(string):
        if i=="(":
            for indj,j in enumerate(string[indi:]):
                if j==")":
                    t=indj+indi
                    return string[:indi]+string[indi+1:t]+string[t+1:],True
            return string,False
    if ")" in string:
        return string,False
    return string,True