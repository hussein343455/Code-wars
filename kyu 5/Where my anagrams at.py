# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
# 'abba' & 'baab' == true
#
# 'abba' & 'bbaa' == true
#
# 'abba' & 'abbba' == false
#
# 'abba' & 'abca' == false

# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none. For example:
#     anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) = > ['aabb', 'bbaa']
#
#     anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) = > ['carer', 'racer']
#
#     anagrams('laser', ['lazing', 'lazy', 'lacer']) = > []




###########     method 0   ###########    ###########
def anagrams(word, words):
    word=sorted(word)
    return  [i for i in words if word == sorted(i)]


###########     method 1 ###########
def anagrams(word, words):
    word=sorted(word)
    rus=[]
    for i in words:
        if sorted(i)==word:
            rus.insert(len(rus), i)
    return rus





#####################method 2
# def anagrams(word, words):
#     word_dec=letdec(word)
#     rus=[]
#     for ind,i in enumerate(words):
#         dec=letdec(i)
#         if word_dec==dec:
#             rus.insert(len(rus),words[ind])
#     return rus
# def letdec(i):
#     dec = {"letter": [], "count": []}
#     for j in i:
#         if j not in dec["letter"]:
#             dec["letter"].append(j)
#             dec["count"].append(i.count(j))
#     return dec
# print(anagrams(word,words))