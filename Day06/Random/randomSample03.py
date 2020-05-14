from random import random


numList=[]
temp = 0
for i in range(10):
    ranNum = (int(random() * 15) + 1)
    numList.append(ranNum)

print(numList)
numList.sort(reverse=False)
print(numList)
