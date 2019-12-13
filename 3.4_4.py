'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в
каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит
его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике,
физике и русскому языку по всем абитуриентам.
В качестве ответа на задание прикрепите полученный файл со средними оценками.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
'''

with open('dataset_3363_4.txt') as file:
    s1 = file.read()

students = s1.strip().split()
length_students = len(students)

students_math = 0
students_phisics = 0
students_russian = 0

with open('dataset_3363_4_result.txt', 'w') as file_write:
    for i in students:
       student = (i.split(';'))
       length_line = len(student)
       name = student[0]
       math = int(student[1])
       phisics = int(student[2])
       russian = int(student[3])

       average_student = (math + phisics + russian)/ (length_line - 1)
       students_math += math
       students_phisics += phisics
       students_russian += russian

       # print(name, math, phisics, russian , 'average', average_student)
       print ( name, 'average', average_student )
       print (average_student, file=file_write)

    average_students_math = students_math/length_students
    print ( 'All students', average_students_math , end=' ')
    print(average_students_math, end=' ', file=file_write)

    average_students_phisics = students_phisics/length_students
    print ( average_students_phisics , end=' ')
    print(average_students_phisics, end=' ', file=file_write)

    average_students_russian = students_russian/length_students
    print ( average_students_russian  )
    print(average_students_russian, file=file_write)