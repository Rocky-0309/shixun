import pandas as pd

# 读取CSV文件
file_path = r'E:\shixun\day3\exercise_data\drinks.csv'  # 使用原始字符串避免转义问题
df = pd.read_csv(file_path)

# 1. 哪个大陆平均消耗的啤酒更多？
beer_avg = df.groupby('continent')['beer_servings'].mean()
max_continent = beer_avg.idxmax()
print(f"平均啤酒消耗最多的大陆是: {max_continent} (消耗量: {beer_avg[max_continent]:.2f})\n")

# 2. 打印每个大陆的红酒消耗描述性统计
wine_stats = df.groupby('continent')['wine_servings'].describe()
print("每个大陆的红酒消耗描述性统计:")
print(wine_stats)
print("\n")

# 3. 打印每个大陆每种酒类别的消耗平均值
avg_all = df.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].mean()
print("每个大陆各类酒的平均消耗量:")
print(avg_all)
print("\n")

# 4. 打印每个大陆每种酒类别的消耗中位数
median_all = df.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].median()
print("每个大陆各类酒消耗的中位数:")
print(median_all)