def digits_product(product):
    top=''
    i=2
    while i<9:
        if product%i==0:
            top+=str(i)
            i=2
            product=int(product/i)
        else:
            i+=1
    if not top:
        return -1
    # top=sorter(top)
    return int(top)
# def sorter(top):
#     while True:
#         if int(top[-2])*int(top[-1])<10 and len(top)>=3:
#             top=top[:-2]+str(int(top[-2])*int(top[-1]))
#         else:
#             return top

print(digits_product(x))