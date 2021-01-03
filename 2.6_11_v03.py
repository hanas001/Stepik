from pprint import pprint

x = 5


matrix = []

# making matrix filled with zeroes
for i in range(x):
    read = [0 for x in range(x)]
    matrix.append(read)

matrixLength = len(matrix)

#pprint(matrix)

currentNumber = 1
currentLine = 0

for row, j in enumerate(matrix):
    # print ("row", row)
    print ("J", j)

    nextCell = 0

    while nextCell < x:                                     #while next cell is less then 5
        # currentLine = 0
        nextCell += 1
        matrix[currentLine][nextCell] = currentNumber       #writing current number to the cell

        print ("current line", currentLine)

        currentNumber += 1                                  #current number increase by one

        print("next cell", nextCell)

        while nextCell == 4 and currentLine <= 4:

            print ("CURRENT LINE", currentLine)
            matrix[currentLine][nextCell] = currentNumber
            currentLine += 1
            currentNumber += 1
            pprint(matrix)

            while nextCell >= 0 and currentLine == 4:

                # nextCell -= 1
                print("CURRENT LINE", currentLine)
                # if matrix[currentLine][nextCell] < currentNumber:
                    matrix[currentLine][nextCell] = currentNumber
                    currentNumber += 1
                    print ("NEXT Cell", nextCell)
                    nextCell -= 1



pprint(matrix)