for i in range(1,101):
    if i %10 ==3 :
        print(i)
        
num = 1
num1 =0
while num > 0 :
    if num1 < num:
        num1 = num
    num = int(input('정수를 입력하세요 : '))
    

print(num1)



x = int(input('x좌표: '))
y = int(input('y좌표: '))

if x > 0:
    if y > 0:
        print('1사분면')
    else :
        print('4사분면')
elif x < 0:
    if y >0:
        print('2사분면')
    else :
        print('3사분면')
else:
    print('영점')

    


    
