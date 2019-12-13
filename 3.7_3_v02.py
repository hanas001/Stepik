'''
 Sample Input:

3
a
bb
cCc
2
a Bb aab aBa ccc
c bb aaa AAa aAB
'''

known_words = []

for i in range(int(input())):
    known_words.append(str(input().lower()))

word_lines = []  # make empty line of all words

for i in range(int(input())):
    word_lines += (input().lower().split())  # read line, split to words, add to the word line list
word_lines_unique = set(word_lines)

for i in word_lines_unique:
    # print ('All words:', i)
    if i not in known_words:  # check with our known words list and print only unknown words
        print (i)

