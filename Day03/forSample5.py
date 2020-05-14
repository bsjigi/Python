# 누적 합 : 1+2+3+4+5

maxNum = int(input('숫자를 입력하세요 누적합을 구합니다 : '))
sumNumber = 0
             
for i in range(maxNum):
    sumNumber = sumNumber + i +1

print(sumNumber, end =' ')
