# solve The function for x
#differentiate("12x+2-13x", 3): ======> -2159


def differentiate(equation, point):
    point=str(point)
    listx= fineder(equation)
    for ind,i in enumerate(listx):
        point = "*" + point
        if i[0]=="x":
            point=point.replace('*','')
        r=i
        i=listx[ind].replace('^','**')
        k=i.index('x')
        listx[ind]=i[:k]+point+i[k+1:]
        listx[ind]=str(eval(listx[ind]))
        equation=equation.replace(r,listx[ind])
    return eval(equation)
def fineder(equ):
    liste=equ.split('-')
    liste2=[]
    liste3=[]
    for i in liste:
        if "+" in i:
            liste2.extend(i.split('+'))
        else:
            liste2.append(i)
    for i in liste2:
        if 'x' in i:
            liste3.append(i)
    return liste3
print(differentiate("12x+2-13x", 3))
