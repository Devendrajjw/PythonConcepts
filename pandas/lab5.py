import pandas as pd

data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

df = pd.DataFrame(data)
# print(df)
df.insert(2, "Age", [21, 23, 24, 21], True)
# print(df)
address = ["Delhi", "Bangalore", "Chennai", "Patna"]
df.loc[:, 'Address'] = address
print(df)
# print(len(df.index))
# df.loc[len(df.index)] = ['Karan', 6.1, 25, 'MCA', 'Punjab']
print(df)
