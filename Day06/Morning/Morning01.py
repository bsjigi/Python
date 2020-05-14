print('메뉴판')
menuName = ['아메리카노', '카페라떼', '카라멜마끼야또', '카푸치노']
menuCost = [3000, 3500, 4000, 2400]
Choice = 0
menuChoice = []
result = [0, 0, 0, 0]

total = 0

for i in range(4):
    print('{}.{} {}'.format(i+1, menuName[i], menuCost[i]))

order = ''
while order != 'n':
    Choice = int(input('메뉴를선택해주세요 :'))
    menuChoice.append(Choice)
    order = input('더 주문하시겠습니까?')

for i in menuChoice:
    if menuChoice[i] == 1:
        result[0] += 1
        total += menuCost[0]
    elif menuChoice[i] == 2:
        result[1] += 1
        total += menuCost[1]
    elif menuChoice[i] == 3:
        result[2] += 1
        total += menuCost[2]
    elif menuChoice[i] == 4:
        result[3] += 1
        total += menuCost[3]


print('주문서')
print()

for i in range(len(result)):
    if result[i] > 0:
        print('{} {}잔 {}원'.format(menuName[i], result[i], (menuCost[i]*result[i])))




print('총 {}원입니다.'.format(total))





