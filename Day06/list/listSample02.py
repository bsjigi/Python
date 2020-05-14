for i in range(5):
    for j in range(5):
        print('0', end='')
    print()

zeroBoard = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

zeroSample = []
for line in range(5):
    zeroLine = []
    for data in range(5):
        zeroLine.append(0)
    zeroSample.append(zeroLine)

print(zeroSample)
