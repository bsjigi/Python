#함수 만드는 방법
def add(num1, num2):
    result = num1+num2
    return result

def add_print(num1, num2):
    result = num1+num2
    print('덧셈값 : {}'.format(result))
#곱하기
def multi(num1, num2):
    result = num1*num2
    print('곱셈값 : {}'.format(result))

#대소비교
def maxNum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    




inputNum1 = int(input('정수를 입력하세요 : '))
inputNum2 = int(input('정수를 입력하세요 : '))
numResult = add(inputNum1, inputNum2)

print("더하기 연산 결과 : {}".format(numResult))

add_print(inputNum1, inputNum2) #함수 호출
multi(inputNum1, inputNum2)
print(maxNum(inputNum1, inputNum2))



#함수 정의
#def : 함수 이름(입력데이터들):
