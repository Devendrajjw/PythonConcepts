import numpy as np
import pandas as pd

data = pd.read_csv("C:\\Users\\DJHUNJHU\\Downloads\\student.csv")
# print(data.drop_duplicates(subset='name').shape[0])

# print(data.groupby('mark'))
response = data.groupby('mark')
# print(len(data))
# print(len(response))
# print(response.size())
# print(response.size().sort_values(ascending=False))
# print(response.first())
# print(response.last())
# print(response.groups)
# print(data.iloc[2, :])
print(response.get_group(81))
