#1부터 100까지 3의 배수 이면서 5의 배수인 값을 출력하여라

for idx in range (1,101) :
    if idx%3 == 0 and idx%5 == 0 :
        print (idx)
