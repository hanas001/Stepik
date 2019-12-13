# n = 4
n= int(input())

direction = []
finalDestinationX = 0
finalDestinationY = 0

for i in range(n):
    currentData = input()
    direction.append(currentData.split(' '))

for i in direction:
   if i[0] == 'север':
       finalDestinationY += int(i[1])
   elif i[0] == 'юг':
       finalDestinationY -= int(i[1])
   elif i[0] == 'восток':
       finalDestinationX += int(i[1])
   elif i[0] == 'запад':
       finalDestinationX -= int(i[1])

print(finalDestinationX, finalDestinationY)