num = int(input('숫자를 입력하세요 : '))

for i in range(1, num+1):
    if  num % i == 0:
          print(i)


for i in range(2,101):
    check = True
    for j in range(2,i):
        if i%j == 0:
            check = False
            break
    if check:    
        print(i,end =" ")
print()


Lan = int(input('국어성적: '))
Math = int(input('수학성적: '))
Eng = int(input('영어성적: '))

print('국어성적: {}'.format(Lan))
print('수학성적: {}'.format(Math))
print('영어성적: {}'.format(Eng))


print('그래프출력')

print('국어'+'*'* int(Lan/5))
print('수학'+'*'* int(Math/5))
print('영어'+'*'* int(Eng/5))
