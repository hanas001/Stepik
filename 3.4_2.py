'''
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью
кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz"
у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить
файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве
входных данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на
эту задачу.
'''


with open('dataset_3363_2.txt') as inf:
    s1 = inf.readline().strip()

print (s1)

current_letter = s1[0]
current_digit = s1[1]

with open('dataset_3363_2_result.txt', 'w') as inf:
    for i in s1[2:]:
        if i.isdigit():
            current_digit += i

        else:
            print ( current_letter * int ( current_digit ) , end='' , file=inf )
            print ( current_letter * int ( current_digit ) , end='' )
            current_digit = ''
            current_letter = i
    print ( current_letter * int ( current_digit ) , end='' , file=inf )
    print ( current_letter * int ( current_digit ) , end='' )