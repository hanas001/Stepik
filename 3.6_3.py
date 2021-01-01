'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''


import requests

templatePath = 'https://stepic.org/media/attachments/course67/3.6.3/'

nextFile = '699991.txt'.split('.')      #first file
#nextFile = '843785.txt'.split('.')      #file to speed up
#print ("next file", nextFile[0])
#print ("next file", nextFile[1])

counter = 0

while nextFile[1] == 'txt':     #loop untill no txt found
    path = requests.get(templatePath + nextFile[0] + '.txt')        #generating full path
    nextFile = path.text.split('.')     #take next file from the file
    print ("next file", nextFile)      #to see what is going on
    counter += 1

else:
    print (path.text)       #printing result from the file
    print ("Files scanned", counter)    #counter for number of files scanned