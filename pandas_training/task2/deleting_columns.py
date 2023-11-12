import pandas as pd

markers = (f"\n\n{'*' * 150}")
df = pd.read_csv('Test_tasks_in_University_of_AI/pandas_training/task1/california_housing_train.csv')

print(markers)
df_2 = df.drop(df.columns[3:], axis=1)
print(f"Таблица с первыми тремя столбцами:\n\n{df_2}")
print(markers)
