# If　a = 1, b = 2, c = 3 ... z = 26
#
# Then l + o + v + e = 54
#
# and f + r + i + e + n + d + s + h + i + p = 108
#
# So friendship is twice stronger than love :-)
#
# The input will always be in lowercase and never be empty.

def words_to_marks(s):
    x=[chr(i)for i in range(97,123)]
    return sum([x.index(i)+1 for i in s])