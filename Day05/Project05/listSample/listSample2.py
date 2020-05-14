##사용자가 0을 입력할때까지의 값을 입력 받는다.
##사용자가 0을 입력하면 지금까지 입력한 모든 숫자들을 출력한다.
##사용자가 입력한 값은 리스트에 담는다)

numList = []
num = 1
while True:
    num = int(input('정수를 입력하세요 : '))
    if num == 0:
        break
    numList.append(num)

print('입력 내용: {}'.format(numList))

# 앞뒤로 읽어도 똑같은지 아닌지에 대한 상태를 알고 잇는 변수: 상태변수
listStatus = True
## 두번째 step : 앞으로 읽어도 똑같은지, 뒤로 읽어도 똑같은지 검사
for i in range (len(numList)//2):
    if numList[i] != numList[-i-1]:
        listStatus = False
        break

if listStatus:
    print('앞뒤가 같습니다')
else:
    print('다릅니다')
