#학생들의 수학 성적을 입력받아 학생들의 수학점수 평균을 구한다.
mathScore =[]

#학생들의 성적을 입력받는 부분
while True:
    
    score = int(input('수학 성적을 입력하세요: '))
    
    if score < 0:
        break
    mathScore.append(score)

print(mathScore)

#입력된 성적의 총 합
sum = 0
for score in mathScore:
    sum = sum + score

print('수학 성적의 총 합 : {}'.format(sum))

avg = sum/len(mathScore)
print ('수학 성적의 평균 : {}'.format(avg))
