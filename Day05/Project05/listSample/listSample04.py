word_dataset = ['hello', 'python', 'elephant', 'deep', 'programming' ,'calloc', 'linked', 'killer','depth','drive', 'half', 'triangle']
#미션1 반복문을 사용해서 모든 데이터셋을 출력해보자


for i in range(len(word_dataset)):

    print(word_dataset[i])
print()
#미션2 첫글자가 h인 요소들만 출력해보자
for i in range(len(word_dataset)):
    if word_dataset[i][0] == 'h':
        print (word_dataset[i])

print()
#미션3: 문자열의 길이가 5인 요소들만 출력해보자
for i in range(len(word_dataset)):
    if len(word_dataset[i]) == 5:
        print(word_dataset[i])
#미션 4: 가장 마지막글자가 e로 끝나는 요소들만 출력해보자
print()
for i in range(len(word_dataset)):
    if word_dataset[i][-1] == 'e':
        print (word_dataset[i])

#미션 5: word_dataset 안에 java라는 단어가 있는지 없는지 판별
print()
count = 0
for i in range(len(word_dataset)):
    if 'java' in word_dataset:
        count+=1
if count > 0:
    print('{}개 있습니다'.format(count))
else:
    print('없습니다')

#미션 6 각 단어마다, e가 몇번들어있는지 count 후 출력
print()
for i in range(len(word_dataset)):
    count =0
    for j in range(len(word_dataset[i])):
        if word_dataset[i][j] == 'e':
            count+=1
    print('{}번째 단어 : '.format(i+1), count)

#미션 7 단어 안에 i가 들어 있는 요소들만 출력

print()

for i in range(len(word_dataset)):
    if 'i' in word_dataset[i]:
        print(word_dataset[i])








