weight = int(input('몸무게를 입력해주세요 : '))
height = int(input('키를 입력해주세요 : '))

BMI = weight/((height/100)**2)

print('BWI : ',round(BMI,2))
