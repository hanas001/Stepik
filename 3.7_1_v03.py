allData = []
listOfLists = []
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

game_number = int(input('Enter number of games:'))

for i in range(0, game_number):  #input teams and score
    currentData = [input('Enter teams and scores:')]
    # allData += currentData
    listOfLists.append(currentData)

# print('listOfLists', listOfLists)

for i in listOfLists:
    for line in i:
        # print(j)
        allData += line.strip().split(';')

allDataSet = set( allData )  # collect only unique data to set
for k in allDataSet:
    if k.isdigit():  # remove digits from the dictionary
        pass
    else:
        uniqueNames.append( k )

for i in uniqueNames:  # making dictionarys filled with zeroes for every team
    dictWins[i] = 0
    dictDraws [ i ] = 0
    dictLooses [ i ] = 0
    dictPoints [ i ] = 0

for j in uniqueNames:
    counter = allData.count(j)  # count number of games for each team
    # print(j, ':',  'games played', counter)
    dictPlays[j] = counter  # add to the dictionary
# print('unique names' , uniqueNames )
# print('all data' , allData )

for i in listOfLists:
    for line in i:
        line = line.strip().split(';')
        teamA = line [ 0 ]
        scoreA = line [ 1 ]

        teamB = line [ -2 ]
        scoreB = line [ -1 ]

        if scoreA > scoreB :
            dictWins [ teamA ] += 1
            dictLooses [ teamB ] += 1
            dictPoints [ teamA ] += winner
            dictPoints [ teamB ] += looser  # not nessesary
        elif scoreA < scoreB :
            dictWins [ teamB ] += 1
            dictLooses [ teamA ] += 1
            dictPoints [ teamB ] += winner
            dictPoints [ teamA ] += looser  # not nessesary
        else :
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