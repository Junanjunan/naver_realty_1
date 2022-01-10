import pandas as pd

df = pd.read_excel('매물.xlsx', sheet_name='임대(주택)')

# print(df['address'])
# print(df['hosil'])
# print(df['owner_phone'])

a = '서울시 광진구 구의동 221-35'
b = '구의동 221-35'


print('구의동 221-35' in a)


print('서울시 광진구 구의동 221-35' in a)
