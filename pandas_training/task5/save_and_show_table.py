import pandas as pd

markers = (f"\n\n{'*' * 150}")

columns = ['Наименование товара', 'Цена', 'Остаток']
data = {
    'Наименование товара': ['Ноутбук', 'Смартфон', 'Планшет', 'Наушники', 'Фитнес-трекер'],
    'Цена': [1000, 500, 300, 150, 80],
    'Остаток': [10, 20, 15, 30, 25]}
df3 = pd.DataFrame(data, columns=columns)
df3.loc[5] = 'Умная колонка', 3000, 9
df3 = df3.sort_values('Цена', ascending=False)
df3 = df3.reset_index(drop=True)


df3.to_csv('gadgets.csv', index=False)
df_gadgets = pd.read_csv('Test_tasks_in_University_of_AI/pandas_training/task5/gadgets.csv')
print(df_gadgets)
