'''
 Sample Input:

3
a
bb
cCc
2
a Bb aab aBa ccc
c bb aaa AAa
'''

'''
known_words = []

for i in range(int(input())):
    known_words.append(str(input()))

print (known_words)
'''

known_words_lower = []
known_words = ['a', 'bb', 'cCc']  # temporary solution
for i in known_words:
    known_words_lower.append(i.lower())

'''
word_lines = []  # make empty line of all words

for i in range(int(input())):
    word_lines += (input().lower().split())  # read line, split to words, add to the list
'''
word_lines_lower = []
word_lines = ['a', 'Bb', 'aab', 'aBa', 'ccc', 'c', 'bb', 'aaa', 'AAa']  # temporary solution
for i in word_lines:
    # print(i.lower(), end=' ')
    word_lines_lower.append(i.lower())

# print ('All words:', word_lines)
# print ('All words lower:', word_lines_lower)

unique_words = set(word_lines_lower)

# print ('Unique words:', unique_words)

for i in unique_words:
    if i not in known_words_lower:
        print (i)

