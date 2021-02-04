# In this Kata, you will be given a lower case string and your task will be to remove k characters from that string using the following rule:
#
# - first remove all letter 'a', followed by letter 'b', then 'c', etc...
# - remove the leftmost character first.
# For example:
# solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
# solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
# solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b'
# solve('abracadabra', 8) = 'rdr'
# solve('abracadabra',50) = ''
# More examples in the test cases. Good luck!
def solve(st,k):
    st=st+"."
    for i in range(97,123):
        s=st.count(chr(i))
        if s<k:
            st= st.replace(chr(i),"",s)
            k=k-s
            if st==".":
                return ''
        elif s>=k:
            st= st.replace(chr(i),"",k)
            return st[:-1]
