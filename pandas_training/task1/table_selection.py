import pandas as pd

markers = (f"\n\n{'*' * 150}")
df = pd.read_csv('Test_tasks_in_University_of_AI/pandas_training/task1/california_housing_train.csv')

print(markers)
print(f"Последние 5 строк:\n\n {df.tail(5)}")
print(markers)
print(f"Размер таблицы:\n\n{df.shape}")
print(markers)
print(f"Вывод каждой второй строки:\n\n {df.iloc[1::2]}")
print(markers)
