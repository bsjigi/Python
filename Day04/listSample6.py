#리스트에 원하는 만틈 정수를 채운다. (음수를 입력하면 입력 종료)
# 그 후 리스트안에 들어있는 데이터 중 3의 배수만 출력한다.



numList = []
while True:
    inputData = int(input('정수를 입력하세요: '))

    if inputData < 0:
        break

    numList.append(inputData)

for i in numList:
    if i % 3 == 0:
        print(i)
    
