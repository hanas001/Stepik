''''
Улитка ползёт вверх по столбу высотой 5 метров.
Каждый день она проползает вверх на 3 метра,
а каждую ночь съезжает вниз на 2 метра.
За сколько дней она доползёт до вершины столба.
'''

hight = 5   #hights of the pole
up = 3      #speed up
down = -2   #speed down

days = 0        #number of days
nights = 0      #number of nights, optional
distance = 0    #traveled distance

while distance <= hight:
    distance += up
    days += 1
    if distance >= hight:
        break
    distance += down
    nights += 1

print ("Улитка доползла", hight, "метров за", days, "дня.")
#print (nights)  #optional