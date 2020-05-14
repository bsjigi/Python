num1 = 23
num2 = 19
num3 = 9
num4 = 12

print(num1>num2 and num2>num3)
print((num1>num2 and num2>num3))
#print(num1 and num2)
#논리 연산자는 좌우 피연산자가 모두 True 나 False의 형태를 띄고 있어야 한다.!!

print(not(num1>num2) and (num2>num3))
print(not((num1>num2) and (num2>num3)))
print(not(num1<num2) and (num2>num3))

print(num1<num2 or num2>num3)
