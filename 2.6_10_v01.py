"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде
последовательности строк, заканчивающихся строкой, содержащей только строку
"end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент в
позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j),
(i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной
стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему
направлению.
"""

#from pprint import pprint

#matrix = [[9, 5, 3], [0, 7, -1], [-5, 2, 9], ['end']]
#matrix = [[1, 1], [1, 1], [1, 1], ['end']]
#matrix = [[1], ['end']]


matrix = []
read = list([i for i in input().split()])
matrix.append(read)

flag = True
while flag == True:
    read = list( [ i for i in input ().split () ] )
    matrix.append(read)
    flag = True
    for counter, value in enumerate(matrix):
        flag = True
        for item in value:
            #print(item)
            if item == 'end':
                flag = False


matrix.pop(-1)

#matrixNew = list(matrix[:]) # does not WORK!!!
#matrixNew = copy.deepcopy(matrix)  # not working
matrixNew = [x[:] for x in matrix]  # deep copy of matrix with no connection between them

lengthMatrix = len(matrix)
lengthRow = len(matrix[0])
#print(lengthMatrix)
#print(lengthRow)

for row, j in enumerate(matrix):

    #print ('j', j)
    #print ( 'row' , row )
    for column, value in enumerate (j):

        #print ( 'row' , row )
        #print ('column', column )

        sum = int ( matrix [ ((row - 1) - lengthMatrix) % lengthMatrix ] [ column ] ) + int (
            matrix [ ((row + 1) - lengthMatrix) % lengthMatrix ] [ column ] ) + int (
            matrix [ row ] [ ((column - 1) - lengthRow) % lengthRow ] ) + int (
            matrix [ row ] [ ((column + 1) - lengthRow) % lengthRow ] )
        #sum = int(matrix[((row - 1) - lengthMatrix) % lengthMatrix][column]) + int(matrix[((row + 1) - lengthMatrix) % lengthMatrix][column]) + int(matrix[row][((column - 1) - lengthMatrix) % lengthMatrix]) + int(matrix[row][((column + 1) - lengthMatrix) % lengthMatrix])
        matrixNew [ row ] [ column ] = sum

for row, j in enumerate(matrixNew):
    if row > 0:
        print('')
    for value in j:
        print(value, end=' ')