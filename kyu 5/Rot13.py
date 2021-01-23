# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.


def rot13(message):
    x=[chr(i) for i in range(97,123) ]
    re=''
    for ind,i in enumerate(message):
        l = False
        if i.isupper():
            l=True
        if i.isalpha()==False:
            re +=i
            continue
        t=x.index(i.lower())
        if i.lower() not in x :
            re +=i
        elif t<13:
            if l:
                re += x[t + 13].upper()
            else:
                re += x[t + 13]
        elif t>=13:
            if l:
                re += x[t - 13].upper()
            else:
                re += x[t - 13]
    return re