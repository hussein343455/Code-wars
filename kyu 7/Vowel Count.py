# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.


def get_count(input_str):
    k=['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    for i in k:
        num_vowels+=input_str.count(i)
    return num_vowels