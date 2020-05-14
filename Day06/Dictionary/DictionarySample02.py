menu = {'아메리카노': 3000, '카페라떼': 3500, '카라멜마끼아또': 4000, '카푸치노': 4500, '핸드드립':5000}

selectedMenu = {}
# for data in menu:
#     print(menu.get(data))

for key in menu.keys():
    print('{} {}'.format(key, menu.get(key)))
for key in menu.keys():
    selectedMenu.update({key: 0})

print(selectedMenu)

select = input('메뉴를 입력하세요 : ')

if select not in menu.keys():
    print('메뉴가 존재하지 않습니다!')

selectedMenu[select] = selectedMenu[select]+1

print(selectedMenu)