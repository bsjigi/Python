num1 = int(input())
num2 = int(input())
if num1> num2:
    maxNum = num1
else:
    maxNum = num2

for i in range(1,maxNum):
    if num1 % i == 0 and num2 % i == 0:
        print(i)

print()   


num3 = int(input())
num4 = int(input())

for i in range(1,(num3*num4)+1):
    if i % num3 ==0 and i % num4 ==0:
        print(i)
        break

num5 = int(input())
num6 = int(input())

if num5< num6:
    minNum = num5
else:
    minNum = num6

for i in range(1,maxNum):
    if num1 % i == 0 and num2 % i == 0:
        print(i)    
    
    
