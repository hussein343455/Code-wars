x="12 / 2 + 3 * 4 - 6"

def evaluate(string):
    done=True
    while done:
        k1, k2 = -1, -1
        if "/" in string:
            k1=string.index("/")
        if "*" in string:
            k2=string.index("*")
        if k1==-1 and k2==-1:
            done=False
        elif k1>k2 or k1==-1:#string[k2-2:k2+2]
            result=oper(string[k2-2],string[k2+2],"*")
            string = updeter(string,result,k2)
        elif k2>k1 or k2==-1:#string[k1-2:k1+2]
            result=oper(string[k1-2],string[k1+2],"/")
            string = updeter(string,result,k1)
    return string

def updeter(string,result,ind):
    asd=string[:ind-2]+result+string[ind+3:]
    return asd.strip()

def oper(number1,number2,opert):
    number2=int(number2)
    number1=int(number1)
    if opert =="*":
        return str(int(number1*number2))
    if opert == "/":
        return str(int(number1/number2))
    if opert == "+":
        return str(int(number1+number2))
    if opert == "-":
        return str(int(number1-number2))

print(evaluate(x))