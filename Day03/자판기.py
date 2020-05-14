# step1 : 사용자에게 메뉴판을 출력하자
print('1. 콜라 (1000원)')
print('2. 사이다 (1200원)')
print('3. 환타 (1500원)')
print('4. 커피 (2400원)')

# step2 : 사용자에게 돈을 입력받자
inputMoney = int(input('돈을 입력하세요 : '))
# step3 : 사용자에게 원하는 음료를 선택받자
while True :
    select = int(input('원하시는 음료의 번호를 입력하세요 : '))
    
#사용자의 잔액에 따라 뽑일 수 잇는 음료를 제한하는 코드
    temp = 0
    if select == 1:
        temp = inputMoney - 1000
       
    elif select == 2:
        temp = inputMoney - 1200
       
    elif select == 3:
        temp = inputMoney - 1500
       
    elif select == 4:
        temp = inputMoney - 2400
        
    if temp < 0:
        print('잔액이 부족하여 음료를 뽑으실 수 없습니다!')
        continue
    
# 연산 부분 : 사용자의 음료 선택에 따라 제거되는 금액이 다라짐
    if select == 1:
        inputMoney = inputMoney - 1000
    elif select == 2:
        inputMoney = inputMoney - 1200
    elif select == 3:
        inputMoney = inputMoney - 1500
    elif select == 4:
        inputMoney = inputMoney - 2400
    else :
        print('음료를 다시 선택해주시기 바랍니다!)
        continue

# step4 : 잔돈 출력
  
    
    print('음료가 나왔습니다')

    if inputMoney < 1000:
        break
    choice = input('더 뽑으시겠습니까? (Y,N) : ')
    
        
    if choice == 'N' :
        break
    
    
print('잔돈은 {}원 입니다!'.format(inputMoney))
print('감사합니다')
