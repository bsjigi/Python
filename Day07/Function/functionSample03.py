#사용자에게 5개의 정수를 입력받는다.(리스트에 대입)
#리스트 안에 있는 데이터 중 가장 큰 수를 찾아 반환하는 함수를 제작한다
#(파라미터로 리스트를 받는다)
#그 후 함수를 호출하여 결과 값을 받은 후 사용자에게 출력한다.


numList = []
for i in range(5):
    num = int(input('정수를 입력하세요 : '))
    numList.append(num)

def maxNum(numList):
    maxNum = 0
    for i in range(len(numList)):
        if maxNum > numList[i]:
            return maxNum
        else:
            maxNum = numList[i]
    return maxNum



print(maxNum(numList))
