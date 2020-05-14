word = input('문장 입력 :')

def anagram(word):
    Status = True
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            Status = False
            break
    if Status:
        print('anagram이 맞습니다.')
    else:
        print('anagram이 아닙니다.')

anagram(word)