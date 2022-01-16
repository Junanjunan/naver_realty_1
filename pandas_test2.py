import pandas as pd

df_total = pd.read_excel('매물 연락처(naver_realty_01).xlsx')

# print(df_total['address'])

# print(df_total.loc[df_total['address'] == '서울시 광진구 구의동 202-12'])

# print(df_total.loc[df_total['address'].isin(['서울시 광진구 구의동 202-12'])])


aa = '서울시 광진구 구의동 202-12'
bb = '서울시 구구구'

# print(df_total.loc[df_total['address'] ==bb])

# print(len(df_total.loc[df_total['address'] == aa]))
# print(len(df_total.loc[df_total['address'] == bb]))
# print(df_total['address'].isin[bb] in df_total)

# print(df_total['address'].isin[bb])

# if df_total.loc[df_total['address'] == aa] in df_total['address']:
#     print('success')
# else:
#     print('fail')


df_excel = pd.DataFrame([
            {
                '주소': 'address', 
                '광고확인일':'update', 
                '거래방식':'type', 
                '가격':'price',
                '방수':'room', 
                '특징':'spec', 
                '중개사': 'agent', 
                '호실':'hosil', 
                '연락처':'phone',
                'url': 'url',
            }
        ])

if len(df_total.loc[df_total['address'] == aa]) != 0:
    # print(df_total.loc[df_total['address'] == aa].reset_index('address'))
    # df_reset = df_total.loc[df_total['address'] == aa].set_index('address')
    # print(df_total.iloc[0]['address'])
    # print(df_total.iloc[0]['owner'])
    df_re = df_total.loc[df_total['address'] == aa]
    # print(df_re.iloc[0]['address'])
    # print(df_re.iloc[0]['hosil'])
    # print(df_re.iloc[1]['hosil'])
    
    for i in range(0, len(df_total.loc[df_total['address'] == aa])):      
        df_new = pd.DataFrame([
            {
                '주소': df_re.iloc[i]['address'],
                '호실': df_re.iloc[i]['hosil'],
                '연락처': df_re.iloc[i]['owner']
            }
        ])
        
        df_excel = df_excel.append(df_new)


print(df_excel)
