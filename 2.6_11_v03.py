from pprint import pprint

x = 5


matrix = []

# making matrix filled with zeroes
for i in range(x):
    read = [0 for x in range(x)]
    matrix.append(read)

matrixLength = len(matrix)

pprint(matrix)

currentNumber = 1
currentLine = 0
#matrix [ 0  ] [ 0 ] = 0

for row, j in enumerate(matrix):
    #print ("row", row)
    print ("J", j)
    #matrix = list ( list ( x ) for x in zip ( *matrix ) )[ : :-1 ]
    for column in range(matrixLength):
        nextCell = ((column) - matrixLength) % matrixLength  # next cell normalized
        if matrix[currentLine][nextCell] == 0:
            matrix[currentLine][nextCell] = currentNumber       # writing current number to the cell
            currentNumber += 1      #current number increase by one
            #currentLine, nextCell = nextCell, currentLine

pprint(matrix)