a = 7
b = 10
c = 5
d = 6

for l in range(c, d + 1):
    print ('', end = '\t')
    print (l, end = '\t')
for i in range(a, b + 1):
    print ('\n')
    for l in range(c, d + 1):
        print (i, end = '\t')
        #print('', end='\t')
        print (i * l, end = '\t')


