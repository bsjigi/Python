
word = ''
wordList = []

while True:
    word = input()
    if len(wordList) > 0:
            if word[0] == wordList[-1][-1]:
                wordList.append(word)
            elif word == 'xx':
                wordList.append(word)
                break
            else:
                print('다시 입력하세요')
    else:
        wordList.append(word)
        continue


for j in wordList:
    print(j, end=' -> ')



