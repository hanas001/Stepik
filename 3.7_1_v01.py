'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий: В первой строке указано целое число n — количество завершенных игр.

После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
'''
# -*- coding: utf-8 -*-

import codecs

stats = {}
winner = 3
looser = 0
draw = 1
teams = []
teamsAll = set()
game = []
dictPlays = {}
dictWins = {}
dictDraws = {}
dictLooses = {}
dictPoints = {}

# game_number = int(input())
game_number = 3


with codecs.open('dataset_371_1.txt', mode='r', encoding='utf-8-sig') as file:  # read from file
    game = file.read().strip().split()

# for i in range(game_number):  #input teams and score
#     game += input().split()

print('GAME', game)

for j in game:
    # print(j.split(';'))
    line = j.split ( ';' )
    # print('LINE', line)
    teams  += line  # gathering all data to string


teamsNames = []

teamsAll = set(teams)
# print(teamsAll)

for i in teamsAll:
    if i.isdigit():
        pass
        # teamsAll.discard ( i )
    else:
        # print (i)
        teamsNames.append(i)


print ('unique names', teamsNames)
# print ('all data', teams)
# print (type(teams))
# print(stats [ teamA ] [1])

for i in teamsNames:
    dictWins[i] = 0
    dictDraws [ i ] = 0
    dictLooses [ i ] = 0
    dictPoints [ i ] = 0

for i in teamsNames:
    counter = teams.count(i)  # count number of games for each team
    # print(i, ':',  'games played', counter)
    dictPlays[i] = counter  # add to the dictionary

# print(dictPlays)

for k in game:
    line = k.split ( ';' )

    teamA = line[0]
    scoreA = line[1]
    # print (teamA, scoreA, end=' ')

    teamB = line [ -2 ]
    scoreB = line [ -1 ]
    # print ( teamB , scoreB )

    if scoreA > scoreB:
        # print (teamA, 'wins')
        # stats [ teamA ] [1] += winner
        dictWins[teamA] += 1
        dictLooses [ teamB ] += 1
        dictPoints[teamA] += winner
        dictPoints [ teamB ] += looser  # not nessesary
    elif scoreA < scoreB:
        # print(teamB, 'wins')
        dictWins[ teamB ] += 1
        dictLooses [ teamA ] += 1
        dictPoints [ teamB ] += winner
        dictPoints [ teamA ] += looser  # not nessesary
    else:
        # print('draw')
        dictDraws[teamA] += 1
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
