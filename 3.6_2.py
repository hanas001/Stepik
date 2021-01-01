import requests

path = requests.get('https://stepic.org/media/attachments/course67/3.6.2/324.txt')
path = path.text
#print(path)
#count = 0

#path = path.split('\p')

#for i in path:
 #   count += 1

#print (count)

pathUpd = path.splitlines()
length = len (pathUpd)
print (pathUpd)
print (length)

