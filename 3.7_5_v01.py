import codecs

avHeight = 0
dictHeight = {}
dictAvHeight = {}
dictForms = {}
allForms = []
counter = 0

with codecs.open('dataset_3380_5.txt', mode='r', encoding='utf-8-sig') as file:  # read from file
    for line in file:
        line = line.strip().split('\t')
        # print(line)
        form = line[0]
        height = int(line[-1])

        # avHeight += height  # ??? smth is wrong here/ need new dictionary with all height collected by the form...
        # print ('avHeight', avHeight)

        # dictHeight[form ] = avHeight  # calculate height for the Form
        allForms.append(form)  # collect all Forms to a string
        # counter += 1

allFormsSet = set(allForms)

# print(allForms)
print('All forms are:', allFormsSet)

for i in allFormsSet:  #
    dictForms[i] = allForms.count(i)

print(dictForms['1'])
# print(dictHeight['1'])

'''
for item in range(1, 12):
    # print(item)
    # print(key)
    # print(value)
    i = str(item)
    # print(i)
    # print(type(i))
    dictAvHeight[i] = float(dictHeight[i])/int(dictForms[i])
    print ( 'dictHeight' , dictHeight [ i ] )
    print('dictForms', dictForms[i])


print('average height is', dictAvHeight )
'''