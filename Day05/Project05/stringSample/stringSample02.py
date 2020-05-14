word = 'level'



listStatus = True

for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        listStatus = False
        break

if listStatus:
    print('앞뒤가 같습니다')
else:
    print('다릅니다')