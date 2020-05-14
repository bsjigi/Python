sentence = 'A pandemic is sweeping the globe, taking the lives of more Americans in just nine weeks than were killed during the Vietnam War.'

word = 'hello'



#머신러닝에 자연어 처리(NLP)
#문자열에서 특정 문자 변경 함수
word = word.replace('e', '*')
print(word)
sentence = sentence.replace('e', '*')
print(sentence)

#문자열 자르기 함수 -> split

print(sentence.split())
print(sentence.split('*'))

print(sentence.upper())
print(sentence.lower())

#공백제거하기
word = ' hello '
print('|{}|'.format(word))
print('|{}|'.format(word.lstrip()))
print('|{}|'.format(word.rstrip()))
print('|{}|'.format(word.strip()))
print('|{}|'.format(word.replace(' ','')))