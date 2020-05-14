icecream = {}
icecream.update({"Melona": 1000})
icecream.update({"Pollapo": 1200})
icecream.update({"Ppangppare": 1800})
icecream.update({"Tankboy": 1200})
icecream.update({"Healthunting": 1200})
icecream.update({"WorldCorn": 1500})
print(icecream)

nameList = icecream.keys()
print(nameList)

'''
formkeys
-리스트로 만들어져 있는 데이터를 딕셔너리로 만들어버림
-리스트의 요소들은 모두다 key값으로 세팅이 됨
'''

new_dic = {}.fromkeys(nameList, 1)
print(new_dic)

for key, value in icecream.items():
    print(key, value)

print(icecream.popitem())

myWord = 'hello programming'

print(myWord.find('pro'))
