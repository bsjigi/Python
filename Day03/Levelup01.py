print ('1.콜라(1000원)\n2.사이다(1200원)\n3.환타(1500원)\n4.커피(2400원)')



money = int(input('돈을 넣어주세요 : '))
drink = int(input('원하시는 음료를 선택해주세요 : '))



if drink == 1 :
    price = 1000
elif drink == 2 :
    price = 1200
elif drink == 3 :
    price = 1500
elif drink == 4 :
    price = 2400
else :
    print('Error')
        
        

leftMoney = money - price

print('음료가 나왔습니다.\n잔돈은 {}원 입니다.'.format(leftMoney) )

print('감사합니다.')
            
