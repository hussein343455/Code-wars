# Create a RomanNumerals class that can convert a roman numeral to and
# from an integer value. It should follow the API demonstrated in the examples below.
# Multiple roman numeral values will be tested for each helper method.
#
# Modern Roman numerals are written by expressing each digit separately
# starting with the left most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order:
# MDCLXVI.
#
# Examples
# RomanNumerals.to_roman(1000) # should return 'M'
# RomanNumerals.from_roman('M') # should return 1000
# Help
# | Symbol | Value |
# |----------------|
# | I      |  1    |
# | V      |  5    |
# | X      |  10   |
# | L      |  50   |
# | C      |  100  |
# | D      |  500  |
# | M      |  1000 |



class RomanNumerals():
    def to_roman(number):
        number = str(number)
        while len(number) < 4:
            number = "0" + number
        re = ''
        dec = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
               400: 'CD', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
               40: 'XL', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
               4: 'IV', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', }
        re = re + "M" * int(number[0])

        k = int(number[1] + "00")
        if k <= 300:
            re = re + 'C' * int(k / 100)
        else:
            re = re + dec[k]

        k = int(number[2] + "0")
        if k <= 30:
            re = re + 'X' * int(k / 10)
        else:
            re = re + dec[k]

        k = int(number[3])
        if k <= 3:
            re = re + 'I' * k
        else:
            re = re + dec[k]

        return re

    def from_roman(Roman):
        pos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        re = 0
        for ind, i in enumerate(Roman):
            if ind == len(Roman) - 1:
                re += pos[i]
            elif pos[i] < pos[Roman[ind + 1]]:
                re -= pos[i]
            else:
                re += pos[i]
        return re
