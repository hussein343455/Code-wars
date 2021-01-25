# Write a simple parser that will parse and run Deadfish.
#
# Deadfish has 4 commands, each 1 character long:
#
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.
#
# parse("iiisdoso")  ==>  [8, 64]
def parse(data):
    k = 0
    re = []
    for i in data:
        if i == 'o':
            re.append(k)
        elif i == 'i':
            k += 1
        elif i == 'd':
            k -= 1
        elif i == 's':
            k = k ** 2
    return re



