import requests

path = requests.get('https://stepic.org/media/attachments/course67/3.6.2/603.txt')
print(path.text)