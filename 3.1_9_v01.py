'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
 удаляет из него все нечётные значения, а чётные нацело делит на два. Функция
 не должна ничего возвращать, требуется только изменение переданного списка
'''
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def modify_list(lst):
    lstNew = []
    lstNew = lst.copy()
    lst.clear ()
    for i in lstNew:
        if i % 2 == 0:
            a = (i // 2)
            lst.append(a)
    return lst

print (modify_list(lst))
