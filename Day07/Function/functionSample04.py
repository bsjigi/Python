height = int(input('키를 입력하세요 : '))
weight = int(input('몸무게를 입력하세요 :'))
def BMI(height, weight):
    Meter = height/100
    bmi = weight/(Meter*Meter)
    return bmi

print(BMI(height,weight))