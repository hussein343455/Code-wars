# ask
# You will be given a string of English digits "stuck" together, like this:

# "zeronineoneoneeighttwoseventhreesixfourtwofive"

# Your task is to split the string into separate digits:

# "zero nine one one eight two seven three six four two five"

# Examples
# "three"              -->  "three"
# "eightsix"           -->  "eight six"
# "fivefourseven"      -->  "five four seven"
# "ninethreesixthree"  -->  "nine three six three"
# "fivethreefivesixthreenineonesevenoneeight"  -->  "five three 
def uncollapse(digits):
    x=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for ind,i in enumerate(x):
        digits=digits.replace(i,str(ind))
    return " ".join([x[int(i)] for i in digits])
