def alphabet_war(battlefield):
    k = battlefield.count("#")
    b1 = ''
    b2 = ''
    b3 = ''
    print("s=====", battlefield)
    if k >= 2 and battlefield.count("[") == 1:
        return ""
    if k == 0:
        return remove(battlefield)
    if k == 1:
        return cuter(battlefield)

    else:
        t = battlefield.index("[")
        b3 = battlefield.replace("[", "", 1)
        b1 = b3[:b3.index("[")]
        b1 = b1[:t] + '[' + b1[t:]
        b2 = battlefield[battlefield.index("]") + 1:]
        print("sen", b1)
        print("sen", b2)
        return alphabet_war(b1) + alphabet_war(b2)


def cuter(str):
    re = ''
    for i in range(str.count('[')):
        start = str.index("[")
        end = str.index("]")
        re += str[start + 1:end]
        str = str[start + 1:]
    print("re", re)
    return re


def remove(str):
    print("str", str)
    return (str.replace("[", "")).replace("]", '')
