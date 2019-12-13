import codecs

allData = []
allDataSet = set()
dictPlays = {}
dictWins = {}
dictDraws = {}
dictLooses = {}
dictPoints = {}
uniqueNames = []

winner = 3  # points for winner
looser = 0  # points for looser
draw = 1  # points for draw

with codecs.open('dataset_371_2.txt', mode='r', encoding='utf-8-sig') as file:  # read from file
    for line in file:
        line = line.strip().split(';')
        allData += line

# print(allData)

allDataSet = set( allData )  # collect only unique data to set
for k in allDataSet:
    if k.isdigit():  # remove digits from the dictionary
        pass
    else:
        uniqueNames.append( k )
# print(teamsNames)

for i in uniqueNames:  # making dictionarys filled with zeroes for every team
    dictWins[i] = 0
    dictDraws [ i ] = 0
    dictLooses [ i ] = 0
    dictPoints [ i ] = 0

for j in uniqueNames:
    counter = allData.count(j)  # count number of games for each team
    # print(i, ':',  'games played', counter)
    dictPlays[j] = counter  # add to the dictionary
# print('unique names' , uniqueNames )
# print('all data' , allData )


with codecs.open('dataset_371_2.txt', mode='r', encoding='utf-8-sig') as file:  # read from file
    for line in file:
        line = line.strip().split(';')

        teamA = line [ 0 ]
        scoreA = line [ 1 ]
        # print (teamA, scoreA, end=' ')

        teamB = line [ -2 ]
        scoreB = line [ -1 ]
        # print ( teamB , scoreB )

        if scoreA > scoreB :
            # print (teamA, 'wins')
            # stats [ teamA ] [1] += winner
            dictWins [ teamA ] += 1
            dictLooses [ teamB ] += 1
            dictPoints [ teamA ] += winner
            dictPoints [ teamB ] += looser  # not nessesary
        elif scoreA < scoreB :
            # print(teamB, 'wins')
            dictWins [ teamB ] += 1
            dictLooses [ teamA ] += 1
            dictPoints [ teamB ] += winner
            dictPoints [ teamA ] += looser  # not nessesary
        else :
            # print('draw')
            dictDraws [ teamA ] += 1
            dictDraws [ teamB ] += 1
            dictPoints [ teamA ] += draw
            dictPoints [ teamB ] += draw

for plays, name in enumerate(dictPlays):
    print ( name, end=': ')  # print team name
    print ( dictPlays[name] , end=' ' )  # print number of plays
    print(dictWins[name], end=' ' )  # print number of wins
    print ( dictDraws [ name ], end=' ' )  # print number of plays in draw
    print ( dictLooses [ name ], end=' ' )  # print number of looses
    print ( dictPoints [ name ]  )  # print number of all points