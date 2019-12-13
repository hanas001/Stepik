# coding=utf-8

string = 'aaaaaaAAabbсaaaa'
string = 'abc'
string = input()

stringLength = len(string)

i = 0
i1 = 1
counter = 1
stringCompact = []

for j in range(i, stringLength - 1):
   if [string[i]] == [string[i1]]:
       counter += 1
       i += 1
       i1 += 1
       #print('counter', counter)
       #print('i', i)
       #print('i1', i1)

       #print(string[i])
   else:
       stringCompact.append(string[i])
       stringCompact.append(str(counter))

       counter = 1
       i += 1
       i1 += 1
       #print(string[i])
stringCompact.append(string[i])
stringCompact.append(str(counter))

#stringCompact = str(stringCompact)
print(type(stringCompact))
#print(stringCompact)
#print(*stringCompact)
for i in stringCompact:
    print(i, end='')