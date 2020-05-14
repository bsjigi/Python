numList = []

#리스트에 데이터 추가하는 방법
numList.append(1)
numList.append(2)
numList.append(3)
print(numList)
#리스트에 특정 데이터 삭제

numList.remove(2)
print(numList)

#리스트 전체 삭제
numList.clear()
print(numList)


#특정 위치에 데이터를 삭제하고 새로운 데이터를 집어넣기
removei = numList.index(5)
numList(5)
numList.insert(removei,12)
print(numList)
