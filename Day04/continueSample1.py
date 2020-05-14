#contine : continue를 만나면 나를 감싸고 있는 것중 가장 가까운 반복문의
#머리로 올라간다.
#continue문을 만나면 밑에 있는 소스코드는 신경도 쓰지 않고 바로 위로 올라감
'''
while True :
    #inputNum = int(input('5의 배수인 정수를 입력하세요: '))

    if inputNum % 5 != 0:
       continue

    print('잘 입력하셨습니다!')
'''
    
for i in range(10):
    if i%2 ==0:
        continue
    print(i)
