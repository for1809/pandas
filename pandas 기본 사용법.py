# series란?
# pandas의 기본 객체
# index와 value로 구성됨
# dictionary와 유사
import pandas as pd
array = pd.Series(['사과', '바나나', '당근'], index = ['a', 'b', 'c'])
print(array)
print(array['a'])

data = {
    'a': '사과',
    'b': '바나나',
    'c': '당근'
}
# Dict 자료형을 Series로 변환
array = pd.Series(data)
print(array)
print(array['b'])

# 데이터 프레임이란?
# 다수의 시리즈를 모아 처리하기 위한 목적으로 사용
# 엑셀과 유사하게 표 형태로 데이터를 출력

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carror': '당근'
}
frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carror': 7
}
word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
# 이름(Name), 값(Values)
summary = pd.DataFrame({
    'word': word,
    'frequency': frequency
})
print(summary)
'''
       word  frequency
Apple    사과          3
Banana  바나나          5
Carror   당근          7
'''

# 시리즈의 연산
price_dict = {
    'apple': 500,
    'banana': 1000,
    'carrot': 2000
}

quantity_dict = {
    'apple': 10,
    'banana': 3,
    'carrot': 5
}
price = pd.Series(price_dict)
quantity = pd.Series(quantity_dict)
summary = pd.DataFrame({
    '단가': price,
    '수량': quantity,
    '가격': price * quantity
})
print(summary)

# 데이터 프레임 슬라이싱
price_dict = {
    'apple': 500,
    'banana': 1000,
    'carrot': 2000,
    'grape': 5000
}

quantity_dict = {
    'apple': 10,
    'banana': 3,
    'carrot': 5,
    'grape': 2
}
price = pd.Series(price_dict)
quantity = pd.Series(quantity_dict)
summary = pd.DataFrame({
    '단가': price,
    '수량': quantity,
    '가격': price * quantity
})
print(summary)

# 이름을 기준으로 슬라이싱
print(summary.loc['banana':'grape', '수량':])
# 인덱스를 기준으로 슬라이싱
print(summary.iloc[1:3, 0:2])

# DataFrame의 연산
summary.loc['apple', '수량'] = 20 # 데이터 변경
summary.loc['melon'] = [10000, 3, 30000] # 새 데이터 삽입
print(summary)

summary.to_csv('summary.csv', encoding = 'utf-8-sig')
saved = pd.read_csv('summary.csv', index_col = 0)
print(saved)