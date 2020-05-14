##가변인자

def datas(num1, *data):
    #가변인자를 파라미터로 받을때, 첫번째로 해야할 작업은 길이 체크
    print(num1, data)
def datas2(num1, **data):
    print(num1, data)

datas(1,2,3,4,5,6,7,8,9)
datas2(1,key=1, name=2, banana='fruit')
