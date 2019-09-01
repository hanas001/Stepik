# coding=utf-8

string = 'aaAAabbсaa'
#string = raw_input()    #for python 2
#string = input() #for python 3

#s = s.lower()
stringLength = len(string)

i = 0
i1 = 1
counter = 1

for j in range (i, stringLength + 1):
   while [string[i]] == [string[i1]]:
       counter += 1
       i += 1
       i1 += 1
       result = string[i] + (string(counter))
       if [s [ i ]] != [s [ i1 ]]:
           c = 1
           res.append(str(s[i]))
