#사용자에게 10개의 값을 입력받자

numList = [] #리스트 변수 만들기

for i in range(5):
    temp = int(input('정수를 입력하세요 :'))
    numList.append(temp)

#리스트 출력 방법
for num in numList:
    print(num, end= ' ')
print('\n\n')

#리스트 출력 방법 25


for i in range(5):
    print(numList[i], end=' ')

print('\n\n')

print('1번째 데이터 출력: {}'.format(numList[1]))
print('-1번째 위치한 데이터 출력: {}'.format(numList[-1]))
print('-2번째 위치한 데이터 출력: {}'.format(numList[-2]))
