import pandas as pd
import numpy as np


# index_list = ['a', 'b', 'c', 'd', 'e']

# print(pd.DataFrame(np.random.rand(5,5), columns=['A', 'B', 'C', 'D', 'E'], index=index_list))    


# df1 = pd.DataFrame(np.random.rand(5,5), columns=['A', 'B', 'C', 'D', 'E'], index=index_list)

# df1.to_excel("test.xlsx")

a_dict = {'a': 1, 'b':2, 'c': 3}

# for a in a_dict:
#     print(a)
#     print(a_dict[a])
#     print("-----")
    
    
# df1 = pd.DataFrame(
#         [
#             {a_dict['a']:10, a_dict['b']:20},
#             {a_dict['a']:30, a_dict['b']:40},
#         ]
#     )


    
# df2 = pd.DataFrame(
#         [
#             {a_dict['a']:100, a_dict['b']:200},
#             {a_dict['a']:300, a_dict['b']:400},
#         ]
#     )

# df3 = df1.append(df2)
# pd.concat(df1, df2)
# print(df1)

df1 = pd.DataFrame([{'a': 'start', 'b': 'start'}])

for i in range(10):
    for j in range(10):
        df2 = pd.DataFrame(
            [
                {'a': i, 'b': j}
            ]
        )
        df1 = df1.append(df2)
        
    
print(df1)

df = pd.DataFrame({'Year': [2000, 2001, 2002, 2003]})
df['link'] = '-'

# def make_hyperlink(value):
#     url = "https://custom.url/{}"
#     return '=HYPERLINK("%s", "%s")' % (url.format(value), value)

# df['hyperlink'] = df['Year'].apply(lambda x: make_hyperlink(x))


df.set_value(0, 'link', '=HYPERLINK("https://en.wikipedia.org/wiki/2000", 2000)')
df.set_value(1, 'link', '=HYPERLINK("https://en.wikipedia.org/wiki/2001", 2001)')
df.set_value(2, 'link', '=HYPERLINK("https://en.wikipedia.org/wiki/2002", 2002)')
df.set_value(3, 'link', '=HYPERLINK("https://en.wikipedia.org/wiki/2003", 2003)')
df.to_excel('test.xlsx', index = False)