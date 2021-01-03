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

    pprint(matrix)

    #fill the matrix from bottom to top
    for h in range(n, 1, -1):
        print ("H", h)
        print ("NUMBER", number)
        if matrix[h-1][0] == "*":
            matrix[h-1][0] = number
            number += 1

    loop += 1

#-------------------- one loop ------------------

# pprint(matrix)

#fill the matrix from left to right
for i in range(n):
    # print ("I", i)
    # print ("NUMBER", number)
    if matrix[n-4][i] == "*":
        matrix[n-4][i] = number
        number += 1

# pprint(matrix)

#fill the matrix from top to bottom
for j in range(n):
    # print("J", j)
    # print("NUMBER", number)
    if matrix[j][n-2] == "*":
        matrix[j][n-2] = number
        number += 1

# pprint(matrix)

#fill the matrix from right to left
for k in range(n-1, 1, -1):
    # print ("K", k)
    # print ("NUMBER", number)
    if matrix[n-2][k-1] == "*":
        matrix[n-2][k-1] = number
        number += 1

# pprint(matrix)

#fill the matrix from bottom to top
for h in range(n-1, 1, -1):
    # print ("H", h)
    # print ("NUMBER", number)
    if matrix[h-2][n-4] == "*":
        matrix[h-2][n-4] = number
        number += 1

# pprint(matrix)

#fill the matrix from left to right
for i in range(n):
    # print ("I", i)
    # print ("NUMBER", number)
    if matrix[n-3][i] == "*":
        matrix[n-3][i] = number
        number += 1

# pprint(matrix)

for j in matrix:
    print (*j)