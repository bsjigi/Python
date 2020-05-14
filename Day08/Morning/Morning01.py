num = int(input('정수를 입력하세요 : '))

def fact(num):
    result = 1
    for i in range(1, num+1):
         result = result*i
    return result

print(fact(num))