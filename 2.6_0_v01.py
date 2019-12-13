string = [12, 44, -6, 0, 99, -55, 234.4, 1]
numberPosition = 0
numberPosition1 = 1
length = len(string)

while length != 0:
    for i in range(length):
        #print (i)
        #print (string[numberPosition])
        #print (string[numberPosition1])
        if string[numberPosition] > string[numberPosition1] or numberPosition1 < (len(string) - 1):
            string.insert ( -1 , string [ numberPosition ] )
            string.remove ( string[numberPosition] )
            numberPosition += 1
            numberPosition1 += 1
            length -= 1
            print ( string )
        else:
            string.insert ( -1 , string [ numberPosition1 ] )
            string.remove ( string[numberPosition1] )
            numberPosition += 1
            numberPosition1 += 1
            length -= 1




#string.sort()
print (string)