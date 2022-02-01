import pandas as pd

columns = ['a', 'b', 'c']
data = [['alex', 10, 'male'], ['bomi', 15, 'female'], ['lens', 20, 'male']]

df = pd.DataFrame(data, columns = columns)

df.to_excel('test2.xlsx')