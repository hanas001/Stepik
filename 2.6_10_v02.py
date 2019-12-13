matrix = [[9, 5, 3], [0, 7, -1], [-5, 2, 9], ['end']]

matrix = []
read = list([i for i in input().split()])
matrix.append(read)
print ( matrix )
flag = True

while flag == True:
    read = list( [ i for i in input ().split () ] )
    matrix.append(read)
    #print ( matrix )
    #print ( read )
    flag = True
    for counter, value in enumerate(matrix):
        flag = True
        #print (counter)
        #print(value)
        for item in value:
            #print(item)
            if item == 'end':
                #print('there is an end')
                flag = False

matrix.pop(-1)
print(matrix)
lengthMatrix = len(matrix)
print(lengthMatrix)
