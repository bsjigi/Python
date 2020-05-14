#컴퓨터는 1부터 50까지의 숫자중 하나를 랜덤으로 선택한다.
#사용자는 이 숫자를 맞춰야한다.
#만약 사용자가 랜덤값보다 큰숫자를 입력하면 Down을 출력해주고
#만약 사용자가 랜덤값보다 작은 숫자를 입력하면 UP을 출력한다.
#만약 사용자가 동이란 값을 입력하면 프로그램을 종료한다.(정답입니다!)
#사용자가 맞출때까지 프로그램이 반복되어야하낟.
#리스트 X

from random import random

computerPick = (int(random()*50))+1
print(computerPick)
UserPick = 0
count = 0
while computerPick != UserPick:
    UserPick = int(input('사용자의 Pick : '))
    if UserPick > computerPick:
        print('DOWN')
        count+=1
    elif UserPick < computerPick:
        print('UP')
        count+=1
    else:
        count+=1
        print('정답입니다!')
        print('{}회 만에 맞췄습니다!'.format(count))
        break
