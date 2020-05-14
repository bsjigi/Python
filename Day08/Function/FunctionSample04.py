# 재귀 함수(순환 호출)

def print_data(num):
    print('출력 결과 : {}'.format(num))

    print_data(num-1) #재귀 호출
print_data(4)

def sum_all(dataList):
    result = 0

    for data in dataList:
        result = result+data
    return result

def average(dataList):
    result = sum_all(dataList)
    result = result/len(dataList)
    return result

scores = [40,50,60,70,80]
print(average(scores))