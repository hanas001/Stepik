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

takeBiggerNumber(string)
