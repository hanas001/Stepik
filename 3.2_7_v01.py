x = [5, 5, 12, 9, 20, 12, 3, 5, 12]

def f(x):
    '''
    Function makes square root from the given number
    :param x: is number
    :return: square root from the number
    '''
    return (x**2)

dictionary = {}
result = ()

for i in x:
    if result not in dictionary:
        result = f ( i )
        print (dictionary.setdefault ( i , result ))
    else:
        print ( dictionary[i])
