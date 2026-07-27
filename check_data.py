import pandas as pd
df = pd.read_csv('public/heart_disease_dataset.csv')
print(df[(df['Age'] == 57) & (df['Cholesterol'] == 200)])
