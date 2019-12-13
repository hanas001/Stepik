import codecs

dictHeight = {}
dictAvHeight = {}
dictForms = {}
allForms = []

with codecs.open('dataset_3380_5.txt', mode='r', encoding='utf-8-sig') as file:  # read from file
    for line in file:
        line = line.strip().split('\t')
        form = line[0]
        height = int(line[-1])
        allForms.append(form)  # collect all Forms to a string
        dictHeight [ form ] = 0  # make dictionary with forms with zeroes

# print('All heigth of students:', dictHeight)
allFormsSet = set(allForms)

# print('All:', allForms)
# print('Unique forms:', allFormsSet)

for i in allFormsSet:  # count amount of students in each form
    dictForms[i] = allForms.count(i)

# print('Number of studenets in each form: ', dictForms)

with codecs.open('dataset_3380_5.txt', mode='r', encoding='utf-8-sig') as file:  # read from file
    for line in file:
        line = line.strip().split('\t')
        form = line[0]
        height = int(line[-1])
        # print ('Height:', height)
        dictHeight[form] += height

# print('All heigth of students:', dictHeight)

for item in range(1, 12):
    i = str(item)
    dictAvHeight[i] = float(dictHeight[i])/int(dictForms[i])
    # print ( 'dictHeight' , dictHeight [ i ] )
    # print('dictForms', dictForms[i])
    print(i, dictAvHeight[i])
