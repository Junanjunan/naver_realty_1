import pandas as pd

df = pd.read_excel('매물.xlsx', sheet_name='임대(주택)')

# print(df['address'])
# print(df['hosil'])
# print(df['owner_phone'])

df1 = pd.read_excel('전번매물통합-2022-01-09.xlsx')
df2 = pd.read_excel('전번매물통합-2022-01-12.xlsx')

df3 = df2.append(df1)

df3.to_excel('합치기.xlsx')