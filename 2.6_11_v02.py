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
    print ("row", row)
    print ("J", j)
    matrix = list ( list ( x ) for x in zip ( *matrix ) )[ : :-1 ]

    for column, value in enumerate(matrix):
        nextCell = ((column + 1) - matrixLength) % matrixLength
        print ("next cell", nextCell)
        if matrix[row][column] == 0 :
            currentNumber += 1
            matrix [ 0 ] [ column ] = currentNumber
            pprint ( matrix )

pprint(matrix)

for row, k in enumerate (matrix):
    print ("K", k)
    for i in k:
        print ("i", i)