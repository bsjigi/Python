#step 1 : 비밀번호 세팅하기
numList = []

num = 0
Status = True

for i in range(5):
    num = int(input('{}번째 자리 비밀번호를 입력하세요: '.format(i+1)))
    numList.append(num)
print('비밀번호가 완성되었습니다.')
print()
print('도어락을 열어주세요')
while Status:
    Error = 0
    password=[]
    for i in range(5):

        num = int(input('{}번째 자리 비밀번호를 입력하세요: '.format(i+1)))
        password.append(num)

        if numList[i] != password[i]:
            Error = Error + 1

    if Error > 0:
        print('비밀번호가 {}자리 잘못되었습니다. 다시입력해주세요.'.format(Error))

    else :
        Status = False
        print('도어락이 열렸습니다.')

