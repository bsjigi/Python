#사용자에게 정수를 입력받는다. 만약 음수를 입력하면 입력을 종료하고
#지금까지 입력된 모든 값을 출력해준다.


numList = []
while True:
    inputData = int(input('정수를 입력하세요: '))

    if inputData < 0:
        break

    numList.append(inputData)

print(numList)
print('리스트의 사이즈 ; {}'.format(len(numList)))

myList = [] #myList라는 리스트형태의 변수를 만들겠습니다.
            #이 변수는 여러개의 값을 담을 수 있습니다.
num1 = 0 # num이라는 변수에 0을 집어 넣겠습니다. 이변수는 값 1개만 담을 수 있습니다


print(myList)

#리스트에 데이터를 추가하는 방법
myList.append(1)
print(myList)
myList.append(2)
myList.append(10)
print(myList)
