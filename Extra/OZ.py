num = int(input())
str = input()
lst = []
for i in range(num):
    lst.append(str[i])

count = 0
point = 0

lst.reverse()

while True:
    if 'O' in lst:
        point = lst.index('O')
        lst[lst.index('O')] = 'Z'
        count += 1
        if point > 0:
            for i in range(point):
                lst[i] = 'O'
    if 'O' not in lst:
        print(count)
        break
​