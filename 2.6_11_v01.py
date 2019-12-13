'''
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано
в примере (здесь n=5):
'''


from pprint import pprint

#x = int(input())
x = 5

# making matrix filled with zeroes
matrix = []
for i in range(x):
    read = [0 for x in range(x)]
    matrix.append(read)

matrixLength = len(matrix)

pprint(matrix)

currentNumber = 0

for row, j in enumerate(matrix):
    for column, value in enumerate(matrix):
        nextCell = ((column + 1)- matrixLength) % matrixLength
        # print(nextCell)
        # print(matrix[row][nextCell])
        currentNumber += 1
        matrix [ row ] [ column ] = currentNumber
        matrix = zip ( matrix [ : :-1 ] )

        # print (matrix)
        # if matrix[row][nextCell] != 0:
        #     print('not zero', matrix[row][nextCell])
        #     row, column = column, row
        #     matrix = zip ( matrix [ : :-1 ] )

# pprint (list(matrix))
# matrixRotated = [[]]
# matrix = zip ( matrix [ : :-1 ] )
# pprint (list(matrix))