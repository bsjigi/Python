zeroSample = []
for line in range(5):
    zeroLine = []
    for data in range(5):
        zeroLine.append('*')
    zeroSample.append(zeroLine)

for i in range(5):
    for j in range(5):
        print(' {}'.format(zeroSample[i][j]), end='')
    print()

print()
#사용자가 좌표를 입력하면 입력한 좌표에 해당하는 공간에 *을 삽인한다.


while True:

    for i in range(5):
        for j in range(5):
            print(' {}'.format(zeroSample[i][j]), end='')
        print()

    x = int(input('x좌표 입력 :'))
    y = int(input('y좌표 입력 :'))
    if x > 4 or y > 4:
        continue
    for i in range(5):
        for j in range(5):
            if zeroSample[i][j] == '*':
                break
            break
        break
    break
    zeroSample[y][x] = '*'





