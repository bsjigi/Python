def power(num, n=2): #num의 n제곱(승) #default argument
    return num**n



def nn(num1, num2=2, num3=3, num4=4):
    return num1, num2, num3, num4

data1, data2, data3, data4 = nn(1, num4=9)
print(data1, data2, data3, data4)

result = power(3)
print(result)