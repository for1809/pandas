# 데이터 프레임 마스킹
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(1, 10, (2, 2)), index = [0, 1], columns = ['A', 'B'])
print(df)
print(df['A'] <= 5)
print(df.query('A <= 5 and B <= 8'))
print(df.query('A <= 5 or B <= 8')) # 조건부 행 추출
# 데이터 프레임 개별 연산
df = pd.DataFrame([[1, 2, 3, 4], [1, 2, 3, 4]], index = [0, 1], columns = ['A', 'B', 'C', 'D'])
print(df)
df = df.apply(lambda x: x + 1) # 함수 적용
print(df)
def addOne(x):
    return x + 1
df = df.apply(addOne)
print(df)

df = pd.DataFrame([
    ['Apple', 'Banana', 'Melon', 'Grape'],
    ['Watermelon', 'Mango', 'Pear', 'Peach']], index = [0, 1], columns = ['A', 'B', 'C', 'D'])
print(df)
df = df.replace({'Apple': 'Airport'}) # 셀 대체
print(df)

# 데이터 프레임 그룹화
df = pd.DataFrame([
    ['Apple', 7, 'fruit'],
    ['Carrot', 4, 'vegetable'],
    ['Rice', 5, 'grain'],
    ['Beef', 3, 'meat'],
    ['Banana', 10, 'fruit']], columns = ['Name', 'Quantity', 'Type'])
print(df)
print(df.groupby(['Type']).sum()) # 해당 그룹으로 묶기

print(df.groupby(['Type'])['Quantity'].aggregate(['min', 'max', np.average]))
def my_filter(data):
    return data['Quantity'].mean() >= 5
df = df.groupby('Type').filter(my_filter)
print(df)
df = df.groupby('Type').get_group('fruit')
print(df)
df = pd.DataFrame([
    ['Apple', 7, 'fruit'],
    ['Carrot', 4, 'vegetable'],
    ['Rice', 5, 'grain'],
    ['Beef', 3, 'meat'],
    ['Banana', 10, 'fruit']], columns = ['Name', 'Quantity', 'Type'])
df['편차'] = df.groupby('Type')['Quantity'].transform(lambda x: x- x.mean())
print(df)

# 데이터 프레임의 다중화
df = pd.DataFrame(
    np.random.randint(1, 10, (4, 4)),
    index = [['1차', '1차', '2차', '2차'], ['공격', '수비', '공격', '수비']],
    columns = ['1회', '2회', '3회', '4회']
)
print(df)
print(df[['1회', '2회']].loc['2차'])

# 피벗 테이블
df = pd.DataFrame([
    ['Apple', 7, 'fruit'],
    ['Carrot', 4, 'vegetable'],
    ['Rice', 5, 'grain'],
    ['Beef', 3, 'meat'],
    ['Banana', 10, 'fruit']], columns = ['Name', 'Quantity', 'Type'])
df = df.pivot_table(index= 'Quantity', columns = 'Type', values = 'Name', aggfunc = np.max)
print(df)