num = int(input('정수 입력 : '))
def prime_number(checkNum):

    count = 0
    for i in range(1, checkNum):
        if checkNum % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False

if prime_number(num) == True:
    print('소수입니다')
else:
    print('소수가 아닙니다')
