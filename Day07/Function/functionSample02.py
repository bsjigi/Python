##사용자에게 5개의 정수를 입력받는다. (리스트에 대입)
#총 합을 구하는 함수를 제작하여 총 합을 반환한다
#(파라미터로 리스트 변수를 받음)
#평균을 구하는 함수를 제작하여 평균을 반화난다
# (파라미터로 총 합과 리스트의 길이를 받는다)
##결과적으로 평균을 사용자에게 출력해준다.

numList = []
for i in range(5):
    num = int(input('정수를 입력하세요 : '))
    numList.append(num)


def add(numList):
    addResult = 0
    for j in numList:
        addResult = addResult + j
    return addResult

def aver(add, length):
    return add/(length+1)


print(add(numList))
print(aver(add(numList), len(numList)))

