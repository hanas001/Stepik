'''
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком
количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать
 слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого
уникального слова в этой строке число его повторений (без учёта регистра) в формате
"слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно
выводиться только один раз.
'''

#string = ['a', 'aa', 'abC', 'aa', 'ac', 'abc', 'bcd', 'a']
#string = ['a', 'A', 'a']
string = [(i) for i in input().split()]

string1 = []
dictionary = {}

#print (string)
#print (set(string))

for i in string:
    j = i.lower()
    #print (j, end=',')
    string1.append(j)
set = set(string1)
#print (string1)
#print (set)
for i in set:
    count = string1.count(i)
    #print (i)
    #print (count)
    #dictionary = {i:count}
    dictionary.setdefault ( i , [ ] ).append (count )
for key, values in dictionary.items():
    print (key, end=' ')
    print ( *values )
    #if i in string: