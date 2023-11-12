import pandas as pd

markers = (f"\n\n{'*' * 150}")

columns = ['Наименование товара', 'Цена', 'Остаток']
data = {
    'Наименование товара': ['Ноутбук', 'Смартфон', 'Планшет', 'Наушники', 'Фитнес-трекер'],
    'Цена': [1000, 500, 300, 150, 80],
    'Остаток': [10, 20, 15, 30, 25]}
df3 = pd.DataFrame(data, columns=columns)
df3.loc[5] = 'Умная колонка', 3000, 9

print(markers)
df3 = df3.sort_values('Цена', ascending=False)
df3 = df3.reset_index(drop=True)
print(f"Таблица с сортировкой по убыванию цены:\n\n{df3}")
print(markers)
