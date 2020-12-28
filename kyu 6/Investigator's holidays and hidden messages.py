# History
# You are a great investigator. You are spending Christmas holidays with your family when you receive a series of postcards.
# At first glance the text on the postcards doesn't make sense (why send random quotes?), but after a closer look you notice something strange.
#
# Maybe there is a hidden message!
#
# Technical details
# Your task is to create a class Investigator with at least these two methods:
#
# postcard(self, text) - analyzes text (a string); return value doesn't matter.
# hidden_message(self) - returns the hidden message (a string).
# Typical usage:
#
# investigator = Investigator()
# investigator.postcard(text of first postcard)
# investigator.postcard(text of second postcard)
# investigator.postcard(...)
# investigator.postcard(text of last postcard)
# investigator.hidden_message()  # return value is checked
# # investigator goes out of scope



class Investigator:
    global k
    k = ''

    def __init__(self):
        pass

    def postcard(self, text):
        global k
        k = k + " " + text

        pass

    def hidden_message(self):
        # Return the hidden message you discovered
        global k
        text = k
        print(text)
        k = ""
        for ind, i in enumerate(text):
            if ind == 0:
                continue
            if i.isupper() and text[ind - 1].isalpha():
                k = k + i
            if i == " " and text[ind - 1] == " ":
                k = k + i
        r = k
        k = ""
        return r