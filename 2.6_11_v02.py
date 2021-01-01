from pprint import pprint

x = 5


matrix = []
for i in range(x):  # making matrix filled with zeroes
    read = [0 for x in range(x)]
    matrix.append(read)

matrixLength = len(matrix)

# pprint(matrix)

currentNumber = 0
currentLine = 1
matrix [ 0  ] [ 0 ] = 0

for row, j in enumerate(matrix):
    # pprint ( matrix )
    matrix = list ( list ( x ) for x in zip ( *matrix ) )[ : :-1 ]

    for column, value in enumerate(matrix):
        nextCell = ((column + 1) - matrixLength) % matrixLength
        print (nextCell)
        if matrix[row][column] == 0 :
            # print(nextCell)
            # print(matrix[row][nextCell])
            currentNumber += 1
            matrix [ 0 ] [ column ] = currentNumber
            pprint ( matrix )
            #print(matrix[nextCell][nextCell])
            #print (nextCell)

        #if matrix[row][column] != 0 :
            #print('Next line')
                # currentNumber += 1
                # currentLine += 1
                # matrix [ currentLine ] [ column ] = currentNumber

        #else:
            #print ( 'step inside' )
            #row += 1
            #matrix[row][column] = currentNumber


pprint(matrix)