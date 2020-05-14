#미션
#이번 프로그램은 학생의 성적을 입력 받아 성적에 따라 등급을 매기는 프로그램을
#만드는 것이다.
#먼저 사용자에게 성적을 입력 받는다.
#그 다음 사용자의 성적을
#A -> 100~90
#B -> 89~80
#C -> 79~70
#D -> 69~60
#F -> 59~
#위 구간과 비교하여 매칭되는 구간간의 등급을 부여한다.

inputNum = int(input('성적을 입력하세요 :'))

if inputNum >= 90  :
    print('A')
elif inputNum >= 80  :
    print('B')
elif inputNum >= 70  :
    print('C')
elif inputNum >= 60  :
    print('D')
elif inputNum < 60 :
    print('F')
elif inputNum > 100 :
    print('Error')
 
