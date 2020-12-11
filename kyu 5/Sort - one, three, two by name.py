# Sort these integers for me ...
# By name ...
# Do it now !

# Input:
# Range is 0-999
# There may be duplicates
# The array may be empty

# Example
# Input: 1, 2, 3, 4
# Equivalent names: "one", "two", "three", "four"
# Sorted by name: "four", "one", "three", "two"
# Output: 4, 1, 3, 2

# Notes:
# Don't pack words together:
# e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
# e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"
# Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
# e.g. "one hundred one", "one hundred two"; is same order as "one hundred and one", "one hundred and two"
# e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"

def sort_by_name(arr):
    dec = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
           6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
           11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
           15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
           19: 'nineteen', 20: 'twenty',
           30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
           70: 'seventy', 80: 'eighty', 90: 'ninety'}
    re_unsorted = []
    finel = []
    for i in arr:
        if len(arr) == 0:
            return finel
        k = ""
        if i == 0:
            re_unsorted.insert(len(re_unsorted), dec[i])
            continue
        if i / 100 >= 1:
            hen = int(i / 100)
            k += dec[hen] + " hundred "
            i = i - (hen * 100)
        if i / 10 > 1 and i > 20 and i % 10 != 0:
            tens = int(i / 10)
            k += dec[tens * 10] + " "
            i = i - (tens * 10)
        if i < 20 or i % 10 == 0:
            if i != 0:
                k += dec[i]
            re_unsorted.insert(len(re_unsorted), k)

    re_sorted2 = sorted(re_unsorted)
    for i in re_sorted2:
        k = re_unsorted.index(i)
        re_unsorted.remove(re_unsorted[k])
        finel.insert(len(finel), arr[k])
        arr.remove(arr[k])

    return finel