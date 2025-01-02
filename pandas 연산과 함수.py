# 데이터 프레임의 Null 여부 확인
import pandas as pd
import numpy as np
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Grape': '포도'
}
price_dict = {
    'Apple': 500,
    'Banana': 1000,
    'Carrot': 2000,
    'Grape': 5000
}
quantity_dict = {
    'Apple': 5,
    'Banana': 10,
    'Carrot': np.nan,
    'Grape': 3
}
word = pd.Series(word_dict)
price = pd.Series(price_dict)
quantity = pd.Series(quantity_dict)
summary = pd.DataFrame({
    '항목': word,
    '단가': price,
    '개수': quantity,
    '가격': price * quantity
})
print(summary)
print(summary.notnull()) # null 이 아니면 True 반환
print(summary.isnull()) # null이면 True 반환
summary = summary.fillna('데이터 없음') # null 채우기
print(summary)

# 시리즈 자료형 연산
array1 = pd.Series([1, 2, 3], index = ['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index = ['B', 'C', 'D'])
array = array1.add(array2)
print(array)
array = array1.add(array2, fill_value = 0) # 겹치지 않는 데이터에 0 부여
print(array)
print(array1 + array2) # 안 겹치는 데이터가 nan으로 표시됨

# 데이터 프레임 자료형 연산

df1 = pd.DataFrame([[1, 2], [3, 4]], index = ['A', 'B'], columns = ['1차', '2차'])
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index = ['B', 'C', 'D'], columns = ['2차', '3차', '4차'])
print(df1)
print(df2)
df = df1.add(df2, fill_value = 3).fillna(0) # fill_value는 행과 열이 겹치지 않을 땐 효과가 없음
print(df)

# 데이터 프레임 집계 함수
array1 = np.random.randint(0, 10, (2, 2))
array2 = np.random.randint(0, 10, (3, 3))
df1 = pd.DataFrame(array1, index = ['A', 'B'], columns = ['1차시', '2차시'])
df2 = pd.DataFrame(array2, index = ['B', 'C', 'D'], columns = ['1차시', '2차시', '3차시'])
print(df1)
print(df2)
df = df1.add(df2, fill_value = 0)
print(df)
print('2차시 합: ', df['2차시'].sum()) # 열 이름
print('2차시 합: ', df.iloc[:,1].sum()) # 열 번호(인덱스)
print('열별 합', df.sum())

# 데이터 프레임 정렬 함수
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Grape': '포도'
}
price_dict = {
    'Apple': 500,
    'Banana': 1000,
    'Carrot': 2000,
    'Grape': 5000
}
quantity_dict = {
    'Apple': 5,
    'Banana': 10,
    'Carrot': np.nan,
    'Grape': 3
}
word = pd.Series(word_dict)
price = pd.Series(price_dict)
quantity = pd.Series(quantity_dict)
summary = pd.DataFrame({
    '항목': word,
    '단가': price,
    '개수': quantity,
    '가격': price * quantity
})
summary = summary.sort_values('단가') # 단가 기준 오름차순
print(summary)
print(summary.sort_values('개수', ascending = False)) # 개수 기준 내림차순