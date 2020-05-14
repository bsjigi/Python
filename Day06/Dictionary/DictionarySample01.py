weather = {'오늘날씨':'좋음', '내일날씨':'더좋음', '모레날씨':'완전좋음'}

#딕셔너리명 = {key: value, key: value .... }

print(weather['오늘날씨'])
print(weather['내일날씨'])
print(weather['모레날씨'])


weather['오늘날씨']='구름이 많음'

print(weather['오늘날씨'])

##딕셔너리에 새로운 데이터를 추가하는 방법
weather.update({'어제날씨':'완전습함'})
print(weather['어제날씨'])
print(weather)

#딕셔너리에서 데이터 삭제하는 방법
weather.pop('모레날씨')
print(weather)

# 딕셔너리에서 데이터 접근하기
#print(weather['모레날씨']
#get으로 접근했을때 매칭되는 key가 없으면 None으로 value 값이 나온다.

print(weather['모레날씨'])
print(weather.get('모레날씨','정보가 없습니다'))

print(weather.keys())
print(weather.values())

#딕셔너리 전체 삭제
weather.clear()
print(weather)
