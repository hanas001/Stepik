'''
Имеется реализованная функция f(x), принимающая на вход целое число x
, которая вычисляет некоторое целочисленое значение и возвращает его в
качестве результата работы.
Функция вычисляется достаточно долго, ничего не выводит на экран, не
пишет в файлы и зависит только от переданного аргумента x

Напишите программу, которой на вход в первой строке подаётся число n
— количество значений x, для которых требуется узнать значение функции
f(x), после чего сами эти n значений, каждое на отдельной строке.
Программа должна после каждого введённого значения аргумента вывести
соответствующие значения функции f на отдельной строке.

Для ускорения вычисления необходимо сохранять уже вычисленные значения
функции при известных аргументах.

Обратите внимание, что в этой задаче установлено достаточно сильное
ограничение в две секунды по времени исполнения кода на тесте.
'''


def f(x):
    return x**2

dictionary = {}
result = ()

# x = [5, 5, 12, 9, 20, 12, 3, 5, 12, 3, 5, 1]
n = int( input () )  # input of n elements to calculate
x = []  # empty list of x

for i in range(n):  # repeat input of x elements n-times
    line = int(input())
    x.append(line)

for i in x :  # cache method
    if int(i) not in dictionary :  # if i was not calculated before, we do it
        result = f ( int(i) )
        # print (result)
        print ( dictionary.setdefault ( int(i) , result ) )  # print result and add result to the dic
    else :
        print ( dictionary [ int(i) ] )  # if it was calculated, print result from the dictionary
