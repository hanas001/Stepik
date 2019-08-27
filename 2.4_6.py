'''
Check if the string is palindrome
'''

#s = "agcgtdedtgcga"    #for tests
#s = raw_input()    #for python 2
s = input() #for python 3

s1 = s[:: -1]
if s1 == s:
    print ('Yes')
else:
    print ('No')
