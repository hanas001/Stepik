from pprint import pprint

n = int(input())
# n = 5

matrix = []

# making matrix filled with zeroes
for i in range(n):
    read = ['*' for n in range(n)]
    matrix.append(read)


number = 1
loop = 0
minusLoop = -1

for action in range(n):     #looping the actions

    #fill the matrix from left to right
    for i in range(n):
        if matrix[loop][i] == "*":
            matrix[loop][i] = number
            number += 1

    # pprint(matrix)

    #fill the matrix from top to bottom
    for j in range(n):
        if matrix[j][minusLoop] == "*":
            matrix[j][minusLoop] = number
            number += 1

    # pprint(matrix)

    #fill the matrix from right to left
    for k in range(n, 1, -1):
        # print ("K", k)
        # print ("NUMBER", number)
        if matrix[minusLoop][k-2] == "*":
            matrix[minusLoop][k-2] = number
            number += 1

    # pprint(matrix)
    
    #fill the matrix from bottom to top
    for h in range(n, 1, -1):
        # print ("H", h)
        # print ("NUMBER", number)
        if matrix[h-1][loop] == "*":
            matrix[h-1][loop] = number
            number += 1

    # pprint(matrix)

    loop += 1
    minusLoop -= 1

#-------------------- one loop ------------------



for j in matrix:
    print (*j)