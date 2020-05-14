#미션2
#사용자에게 돈을 입력받고 사용자가 입력한 돈을 현금으로 주려면 1천원짜리 지폐가 몇장필요할까?

money = int(input('돈: '))

count = int(money/1000)

print('{}장'.format(count))
