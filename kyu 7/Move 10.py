# Move every letter in the provided string forward 10 letters through the alphabet.
#
# If it goes past 'z', start again at 'a'.
#
# Input will be a string with length > 0

def move_ten(st):
    alph=[chr(i) for i in range(97,123)]
    return "".join([alph[(alph.index(i)+10)%26] for i in st])