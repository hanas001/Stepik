string = [12, 44, -6, 0, 99, -55, 234.4, 1]
numberPosition = 0
numberPosition1 = 1
length = len(string)
takeBiggerNumber = 0
stringSorted = []

def takeBiggerNumber():
    takeBiggerNumber = 0
    for i in string :
        if i > takeBiggerNumber :
            takeBiggerNumber = i

    stringSorted.append ( takeBiggerNumber )
    string.remove ( takeBiggerNumber )

#while length != 0:
for i in string:
    if i > takeBiggerNumber:
        takeBiggerNumber = i

stringSorted.append(takeBiggerNumber)
string.remove(takeBiggerNumber)
#length -= 1

takeBiggerNumber = 0
for i in string:
    if i > takeBiggerNumber:
        takeBiggerNumber = i

stringSorted.append(takeBiggerNumber)
string.remove(takeBiggerNumber)

takeBiggerNumber = 0
for i in string:
    if i > takeBiggerNumber:
        takeBiggerNumber = i

stringSorted.append(takeBiggerNumber)
string.remove(takeBiggerNumber)

#print (takeBiggerNumber)
print (string)
print (stringSorted)