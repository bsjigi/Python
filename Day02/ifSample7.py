#사용자에게 총 금액을 입력받는다.
#사용자에게 총 인운을 입력받는다.
#각각 내야할 금액을 출력한다.

#출력결과 예시
#총 금액을 입력하세요: 5000
#총 인원을 입력하세요: 2
#각각 내야할 금액은 2500원 입니다.
#출력결과 예시
#총 금액을 입력하세요: 5000
#총 인원을 입력하세요: 3
#각각 내야할 금액은 1666원 입니다.

money = int(input('총 금액을 입력하세요 : '))
people = int(input('총 인원을 입력하세요 : '))

result = money//people - (money//people%100)
remain = money-(result*people)
last = remain+result


print('각각 내야할 금액은 {}원 입니다.'.format(result))

if last != result :
    print('마지막 한명은 {}원 내야 합니다.'.format(last))

