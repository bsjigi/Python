numList = [1,2,3,4,5,6,7,8,9]

#slicing
print(numList[0:4])
print(numList[5:7])
print(numList[6:-1])
print(numList[5:])
print(numList[:3])

myword = 'programming'

print(myword[5:])
print(myword[:4])
print(myword[3:5])
print(myword[:])

#뒤집기 -> 정렬과는 무관

numList.reverse()
print(numList)

print(numList.pop())
print(numList)

scopy = numList
print(scopy)
scopy.pop()
print(scopy)
print(numList)

dcopy = list(numList)
print(dcopy)

dcopy.pop()

print(dcopy)
print(numList)