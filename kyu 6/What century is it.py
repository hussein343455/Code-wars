# eturn the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

# Examples
# "1999" --> "20th"
# "2011" --> "21st"
# "2154" --> "22nd"
# "2259" --> "23rd"
# "1124" --> "12th"
# "2000" --> "20th"
def what_century(year):
    print(year)
    if year[2:] == "00":
        re = str(int(year[:2]))
    else:
        re = str(int(year[:2]) + 1)

    if int(re) > 3 and int(re) < 20:
        return re + "th"
    if re[1] == '1':
        return re + "st"
    if re[1] == '2':
        return re + "nd"
    if re[1] == '3':
        return re + "rd"
    else:
        return re + "th"
