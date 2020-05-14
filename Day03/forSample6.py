# 팩토리얼 : 누적 곱 1*2*3*4*5
#사용자에게 종료값을 입력받은 후 팩토리얼 연산을 진행

factorial = int(input('숫자를 입력하세요 팩토리얼을 구합니다 : '))

num = 1

for i in range(factorial):
    num = num * (i+1)

print(num, end = ' ')
                
