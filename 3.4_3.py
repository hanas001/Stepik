'''
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое
частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.
'''

s_new = []
word_count = {}
frequent_word = 0

with open('dataset_3363_3.txt') as inf:
    s1 = inf.readlines()
for i in s1:  # read every line
    s = str(i).lower().strip()  # make string, in lower case and remove end line character
    s = s.split ()  # split string to words
    s_new += s
    s_unique = set(s)  # add unique words to set

    # print (s)
    # print ( i )
for j in s_unique:
    # s_new.count(j)
    # print(j, s_new.count ( j ))
    # print (j)
    word_count[j] = s_new.count ( j )  # add word and number it was found in the text to the dictionary
    if frequent_word < word_count[j]:
        frequent_word = word_count[j]

for k, l in word_count.items():
    if l >= frequent_word:
        print(k, l)

# print('frequent_word', frequent_word)
# print ('s_new', s_new)
# print ('s_unique', s_unique)
# print(word_count)